from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )	
 #   def to_help(self,update):
 #       update.message.reply_text("Oh! Dear~ \nWhat can I do for you ?")

    def is_going_to_help(self, update):
        text = update.message.text
        return text.lower() == 'help'

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'repeat after me'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'
   
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'go to state3'
    
    def on_enter_help(self,update):
        update.message.reply_text("Oh! Dear~ \nWhat can I do for you ?")

    def on_enter_state1(self, update):
        update.message.reply_text("OK~ I will repeat what you said")
        #self.go_back(update)
    
    def is_back_state1(self, update):
        text = update.message.text
        if text.lower() == 'go back':
            return text.lower() == 'go back'  
        else:
            update.message.reply_text(text)
            print(update.message)
        return text.lower() == 'go back'

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
    
    def on_enter_state3(self, update):
        update.message.reply_text("I'm entering state3")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
