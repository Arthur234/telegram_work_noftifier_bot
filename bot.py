import os
import time

import telebot

from credentials import TOKEN
from flask import Flask, request
from utils.get_vacancies import get_vacancies
from utils.create_message import create_message

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def main_menu(message):
    bot.send_message(message.from_user.id, 'Выберите группу:')


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     chat_id = message.chat.id
#     print(chat_id)
#
#     msg = bot.send_message(chat_id, 'Введите название вакансии')
#     bot.register_next_step_handler(msg, get_vacancy)


# def get_vacancy(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, 'Ищем...')
#
#     vacancies = get_vacancies(message.text)
#     message = create_message(vacancies)
#
#     for msg in message.split('\n\n'):
#         if msg:
#             time.sleep(0.5)
#             bot.send_message(chat_id, msg)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegram-work-notifier-bot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
