from chatterbot import ChatBot
bot = ChatBot('Piku')
from chatterbot.trainers import ListTrainer
bot.set_trainer(ListTrainer)
bot.train(['What is your name?', 'My name is Piku'])
bot.train(['How are you ?','I am awesome'])
bot.traine(['Do you know me','Yes , very well','No idea','Misti , right ?'])
from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
bot.get_response("Hello, how are you today?")
while True:
    message=input('\t\t\tYou:')
    if message.strip()!='Bye':
        reply=bot.get_response(message)
        print('Piku:',reply)
    if message.strip()=='Bye':
        print('Piku: Bye')
        break
