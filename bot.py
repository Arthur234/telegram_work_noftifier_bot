import time

import telebot

from utils import create_work_message, create_freelance_message, get_queried_data
from credentials import token
from parsers import wp, fp


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

    vacancies = get_queried_data(work_find_request,
                    [wp.WorkUaParser, wp.RabotaUaParser, wp.HHParser, wp.DjinniParser])
    message = create_work_message(vacancies)

    for msg in message.split('\n\n'):
        if msg:
            time.sleep(0.5)
            bot.send_message(chat_id, msg, disable_web_page_preview=True, parse_mode='markdown')


@bot.message_handler(commands=['find_freelance'])
def find_freelance(message):
    chat_id = message.chat.id
    freelance_find_request = ' '.join(message.text.split(' ')[1:])

    if not freelance_find_request:
        bot.send_message(chat_id, 'Не понимаю, введите правильный запрос')
        return

    bot.send_message(chat_id, 'Ищем...')

    vacancies = get_queried_data(freelance_find_request,
                                 [fp.FreelanceUaParser])
    message = create_freelance_message(vacancies)

    for msg in message.split('\n\n'):
        if msg:
            time.sleep(0.5)
            bot.send_message(chat_id, msg, disable_web_page_preview=True, parse_mode='markdown')


bot.polling()