import telebot
from telebot import types
import texts
import sys
import re
from telebot.types import InputMediaPhoto
from texts import Easteregg_MESSAGE
import time

DEBUG_MODE = False
if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    DEBUG_MODE = True
    print("Режим DEBUG активирован через sys.argv!")
BOT_TOKEN = '8556406971:AAF-VHxA3kVAqI5ql1FzPUKMoMyH30cn8zw'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    photo_startfile = open('photo_5318766772590680802_x.jpg', 'rb')
    bot.send_photo(message.chat.id, photo=photo_startfile, caption=texts.START_MESSAGE, parse_mode="HTML")

@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, texts.HELP_MESSAGE, parse_mode="HTML")

@bot.message_handler(commands=['about'])
def send_about(message):
    chat_id = message.chat.id
    photo_aboutfile = open('photo_5321486328702638744_y.jpg', 'rb')
    bot.send_photo(chat_id, photo=photo_aboutfile)
    bot.send_message(chat_id, texts.ABOUT_MESSAGE, parse_mode="HTML")

@bot.message_handler(commands=['goal'])
def send_goal(message):
    chat_id = message.chat.id
    photo_goalfile=open('photo_5321486328702638893_y.jpg', 'rb')
    bot.send_photo(message.chat.id, photo=photo_goalfile)
    bot.send_message(message.chat.id, texts.MYGOAL_MESSAGE, parse_mode="HTML")

@bot.message_handler(commands=['history'])
def send_history(message):
    chat_id = message.chat.id
    photo_historyfile=open('photo_5321486328702639041_y.jpg', 'rb')
    bot.send_photo(message.chat.id, photo=photo_historyfile)
    bot.send_message(message.chat.id, texts.MYBEGINNINGS_MESSAGE, parse_mode="HTML")

@bot.message_handler(commands=['mentor'])
def send_mentor(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text=texts.MENTOR_MESSAGE, parse_mode="HTML")

@bot.message_handler(commands=['progress'])
def send_progress(message):
    chat_id = message.chat.id
    photo_progressfile=open('photo_5323692279740439030_y.jpg', 'rb')
    bot.send_photo(chat_id, photo_progressfile)
    bot.send_message(chat_id, text=texts.PROGRESS_MESSAGE, parse_mode="HTML")

@bot.message_handler(commands=['hobbies'])
def send_hobbies(message):
    chat_id = message.chat.id
    photo_hobbiesfile=open('photo_5323692279740439083_x.jpg', 'rb')
    bot.send_photo(chat_id, photo=photo_hobbiesfile)
    bot.send_message(chat_id, text=texts.HOBBIES_MESSAGE, parse_mode="HTML")

@bot.message_handler(commands=['portfolio'])
def send_portfolio(message):
    chat_id = message.chat.id
    photo_firstworkfile=open('photo_5323692279740439122_y.jpg', 'rb')
    photo_firstbotfile=open('photo_5323692279740439121_x.jpg', 'rb')
    photo_projectfile=open('photo_5323692279740439120_y.jpg', 'rb')
    media = [
        InputMediaPhoto(photo_firstworkfile),
        InputMediaPhoto(photo_firstbotfile),
        InputMediaPhoto(photo_projectfile)
    ]
    bot.send_media_group(chat_id, media=media)
    bot.send_message(chat_id, text=texts.WORKS_MESSAGE, parse_mode="HTML")

@bot.message_handler(commands=['github'])
def send_github(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, texts.GITHUB_MESSAGE, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text and message.text.strip().lower() == "тамагочи")
def secret_word_message(message):
    try:
        chat_id = message.chat.id
        with open('photo_5328195879367809119_y.jpg', 'rb') as photo:
            bot.send_photo(chat_id, photo)
        bot.send_message(chat_id, Easteregg_MESSAGE)
    except Exception as e:
        print(f"Ошибка при отправке пасхалки: {e}")
        bot.send_message(message.chat.id, "Упс! Я нашла пасхалку, но не могу загрузить картинку.")

from texts import (Questionone_MESSAGE, Questiontwo_MESSAGE, Questionthree_MESSAGE,
Questionfour_MESSAGE, Questionfive_MESSAGE, Questionsix_MESSAGE)

ANSWERS = ["2011", "Атырау", "Икс", "2021", "Тамерлан", "Камень, ножницы, бумага"]

@bot.message_handler(commands=['quiz'])
def q_start(message):
    bot.send_message(message.chat.id, Startquiz_MESSAGE)
    bot.register_next_step_handler(message, q1)

def q1(message):
    if message.text.strip().lower() == str(ANSWERS[0]).strip().lower():
        bot.send_message(message.chat.id, "Правильно!")
    else:
        bot.send_message(message.chat.id, "Неправильно!")
    bot.send_message(message.chat.id, Questionone_MESSAGE)
    bot.register_next_step_handler(message, q2)

def q2(message):
    if message.text.strip().lower() == str(ANSWERS[1]).strip().lower():
        bot.send_message(message.chat.id, "Правильно!")
    else:
        bot.send_message(message.chat.id, "Неправильно!")
    bot.send_message(message.chat.id, Questiontwo_MESSAGE)
    bot.register_next_step_handler(message, q3)

def q3(message):
    if message.text.strip().lower() == str(ANSWERS[2]).strip().lower():
        bot.send_message(message.chat.id, "Правильно!")
    else:
        bot.send_message(message.chat.id, "Неправильно!")
    bot.send_message(message.chat.id, Questionthree_MESSAGE)
    bot.register_next_step_handler(message, q5)

def q4(message):
    if message.text.strip().lower() == str(ANSWERS[3]).strip().lower():
        bot.send_message(message.chat.id, "Правильно!")
    else:
        bot.send_message(message.chat.id, "Неправильно!")
    bot.send_message(message.chat.id, Questionfour_MESSAGE)
    bot.register_next_step_handler(message, q5)

def q5(message):
    if message.text.strip().lower() == str(ANSWERS[5]).strip().lower():
        bot.send_message(message.chat.id, "Правильно!")
    else:
        bot.send_message(message.chat.id, "Неправильно!")
    bot.send_message(message.chat.id, Questionsix_MESSAGE)
    bot.register_next_step_handler(message, q_final)

def q_final(message):
    if message.text.strip().lower() == ANSWERS[5]:
        bot.send_message(message.chat.id, "Правильно!")
    else:
        bot.send_message(message.chat.id, "Неправильно!")
    bot.send_message(message.chat.id, "Квиз окончен.")

if __name__ == '__main__':
    print("Бот успешно запущен.")
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            print("Упс, произошла ошибка в работе кода. Попробуйте позже или напишите авторке ;):{e}")
            time.sleep(5)