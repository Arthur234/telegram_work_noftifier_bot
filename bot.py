import os
import time

import telebot
from flask import Flask

from utils import get_vacancies
from utils import create_message
from credentials import token


bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def send_instructions(message):
    # TODO: create instructions
    pass


@bot.message_handler(commands=['find'])
def find_work(message):
    chat_id = message.chat.id
    work_find_request = ' '.join(message.text.split(' ')[1:])

    if not work_find_request:
        bot.send_message(chat_id, 'Не понимаю, введите правильный запрос')
        return

    bot.send_message(chat_id, 'Ищем...')

    vacancies = get_vacancies(work_find_request)
    message = create_message(vacancies)

    for msg in message.split('\n\n'):
        if msg:
            time.sleep(0.5)
            bot.send_message(chat_id, msg, disable_web_page_preview=True, parse_mode='markdown')


bot.polling()