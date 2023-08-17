import os
import telebot
from telebot import types
import credentials.api as cred
from Game import Game 
print(cred.api_key)
bot = telebot.TeleBot(cred.api_key)

#board pieces
emptyPlaces = '⚪'
player1Places = '🔴'
player2Places = '🔵'

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup = buttonGenerator(['Play', 'Repeat'], markup)
    message = bot.reply_to(message, "Welcome! Ready to play?",reply_markup=markup)
    bot.register_next_step_handler(message, initGame)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def buttonGenerator(btns, markup):
    for btn in btns:
        markup.add(types.KeyboardButton(btn))

def initGame(message):
    currentG = Game(1,2)
    
    completeString = ""
    for i in range(0,6):
        rowStr = ""
        for j in range(0,7):
            rowStr= rowStr+currentG.gui_board[i][j]
        rowStr= rowStr+"\n"
        print(rowStr)
        completeString=completeString+rowStr
    

    bot.reply_to(message, "Ok! Your chips are blue, mine are red. \nSend me commands indicating on which column you want to place your chip! \n")
    bot.reply_to(message, "This is the board! \n \n" + completeString)
    


bot.infinity_polling()