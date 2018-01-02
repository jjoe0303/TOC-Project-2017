from transitions.extensions import GraphMachine
import random

FSM_URL = 'https://98747bff.ngrok.io/show-fsm'
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
        return text.lower() == 'repeat after me'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'search image for me'
   
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'dictionary'
    
    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'i feel sick'
    
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
    
    def on_enter_state4(self, update):
        update.message.reply_text("You should go to see a doctor, my dear")
        update.message.reply_text("I suggest...")
        i = random.randint(1,5)
        if i==1:
            update.message.reply_text("成光中醫診所\n地址:701台南市東區長榮路三段121號\n電話:+88662355366")
        elif i==2:
            update.message.reply_text("達俊診所\n地址:701台南市東區青年路434號\n電話:+88662361337")
        elif i==3:
            update.message.reply_text("佳一家庭診所\n地址:701台南市東區東光路一段132號\n電話:+88662360513")
        elif i==4:
            update.message.reply_text("楊慧斌耳鼻喉科診所\n地址:701台南市東區東寧路389號\n電話:+88662369016")
        else:
            update.message.reply_text("國立成功大學醫學院附設醫院\n地址:704台南市北區勝利路138號\n電話:+88662353535")
        update.message.reply_text("Helpful?") 
        self.advance(update)
       # self.go_back(update)
   
    def is_back_state5(self, update):
        text = update.message.text
        if text.lower() == 'yes':
            return text.lower() == 'yes'  
        elif text.lower() == 'no':
            self.go_back(update)
        return text.lower() == 'thank you'
    
    def on_exit_state5(self, update):
        print('Leaving state5')
