import os
import telebot
from telebot import types
import credentials.api as cred

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
    bot.reply_to(message, "This is to test the chips " + emptyPlaces + player1Places+player2Places)


bot.infinity_polling()