import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '541641202:AAH2_ZEMoea0Bb9mq-qMf2XuM9wIrj9APxQ'
WEBHOOK_URL = 'https://54e122af.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
		'help',
        'state1',
        'state2',
		'state3'
    ],
    transitions=[
		{
            'trigger': 'advance',
            'source': 'help',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'help',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'help',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },

        {
		    'trigger':'advance',
			'source':'state1',
			'dest':'help',
			'conditions':'is_back_state1'
		},

        {
            'trigger': 'go_back',
            'source': [
              #  'state1',
                'state2',
				'state3'
            ],
            'dest': 'help'
        }
    ],
    initial='help',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
