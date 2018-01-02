from transitions.extensions import GraphMachine

FSM_URL = 'https://96e06baf.ngrok.io/show-fsm'
str1 = "+"
str2 = "-"

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
        return text.lower() == 'repeat'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'image'
   
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'dictionary'
    
    def on_enter_help(self,update):
        update.message.reply_text("Oh! Dear~ \nWhat can I do for you ?")

    def on_enter_state1(self, update):
        update.message.reply_text("OK~ I will repeat what you said")
        #self.go_back(update)
    
    def is_back_state1(self, update):
        text = update.message.text
        if text.lower() == 'go back':
         #   update.message.img = "https://127.0.0.1:5000/show-fsm"
            return text.lower() == 'go back'  
        else:
            update.message.reply_text(text)
  #          print(update.message)
        return text.lower() == 'go back'

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("Which image you're looking for ??")
#        self.go_back(update)

    def is_back_state2(self, update):
        text = update.message.text
        if text.lower() == 'show fsm':
            update.message.reply_text(FSM_URL)
            update.message.reply_text("Which image you're looking for ??")
        elif text.lower() == 'go back':
            return text.lower() == 'go back'
        else:
            text = str1.join(text.split(" "))
            update.message.reply_text("https://www.google.com.tw/search?q="+text+"&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjimaK9zLnYAhXEkJQKHZ-6BGQQ_AUICigB&biw=1615&bih=950")
            update.message.reply_text("Which image you're looking for ??")
        return text.lower() == 'go back'

    def on_exit_state2(self, update):
        print('Leaving state2')
       	
    def on_enter_state3(self, update):
        update.message.reply_text("Which word you want to search for ?")
       # self.go_back(update)
   
    def is_back_state3(self, update):
        text = update.message.text
        if text.lower() == 'go back':
            return text.lower() == 'go back'  
        else:
            text = str2.join(text.split(" "))
            update.message.reply_text("http://www.dictionary.com/browse/"+text+"?s=t")
            update.message.reply_text("Which word you want to search for?")
    #        print(update.message)
        return text.lower() == 'go back'
    
    def on_exit_state3(self, update):
        print('Leaving state3')
