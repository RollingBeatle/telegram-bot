import os
import telebot

import credentials.api as cred

print(cred.api_key)
bot = telebot.TeleBot(cred.api_key)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Ready to play?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()