import telebot
import logic
import os
from boto.s3.connection import S3Connection

token = S3Connection(os.environ['telegram-token'])

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, send me nick or id instagram user for convertation')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower().isdigit():
        bot.send_message(message.chat.id, logic.id_to_nick(message.text.lower()))
    else:
        bot.send_message(message.chat.id, logic.nick_to_id(message.text.lower()))

bot.polling()