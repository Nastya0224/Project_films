from webbrowser import get
import random
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup
import requests
from bs4 import BeautifulSoup as BS, BeautifulSoup
import pandas
import random
from urllib3.util import url

URL = 'https://www.film.ru/online'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36 '
}

bot = telebot.TeleBot('5591646651:AAFTe59uPCwe2890pcgau7mxZmwNe4woW_w')

URL_animation = 'https://www.film.ru/online/animation'
URL_horror = 'https://www.film.ru/online/horror'
URL_comedy = 'https://www.film.ru/online/comedy'
URL_crime = 'https://www.film.ru/online/crime'
URL_action = 'https://www.film.ru/online/action'
URL_science_fiction ='https://www.film.ru/online/science_fiction'
URL_fantasy = 'https://www.film.ru/online/fantasy'
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='film_list')
    films = []
    urls = []
    for item in items:
        films.append((item.find('strong').get_text(),
            'https://www.film.ru'+item.find('a').get('href')))

    return films


animations  = get_html(URL_animation)
horror  = get_html(URL_horror)
comedy  = get_html(URL_comedy)
crime  = get_html(URL_crime)
action  = get_html(URL_action)
science_fiction  = get_html(URL_science_fiction)
fantasy  = get_html(URL_fantasy)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ужасы")
    btn2 = types.KeyboardButton("Комедия")
    btn3 = types.KeyboardButton("Фантастика")
    btn4 = types.KeyboardButton("Мультфильм")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,
                     text='Привет, я могу поискать для тебя интересный фильм. Но для начала выбери жанр.'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    if (message.text == "Ужасы"):
        bot.send_message(message.chat.id, 'Вы выбрали раздел ужасы')
        maks_rand = len(get_content(horror.content))
        x = random.randint(1, maks_rand)
        content = get_content(horror.text)
        for i in enumerate(content):
            if i[0] == x:
                bot.send_message(message.chat.id, 'Фильм называется : ' + i[1][0])
                bot.send_message(message.chat.id, i[1][1])

    elif message.text == "Комедия":
        bot.send_message(message.chat.id, 'Вы выбрали раздел комедия')
        maks_rand = len(get_content(comedy.content))
        x = random.randint(1, maks_rand)
        content = get_content(comedy.text)
        for i in enumerate(content):
            if i[0] == x:
                bot.send_message(message.chat.id, 'Фильм называется : ' + i[1][0])
                bot.send_message(message.chat.id, i[1][1])
    elif message.text == "Фантастика":
        bot.send_message(message.chat.id, 'Вы выбрали раздел фантастика')
        maks_rand = len(get_content(fantasy.content))
        x = random.randint(1, maks_rand)
        content = get_content(fantasy.text)
        for i in enumerate(content):
            if i[0] == x:
                bot.send_message(message.chat.id, 'Фильм называется : ' + i[1][0])
                bot.send_message(message.chat.id, i[1][1])
    elif message.text == "Мультфильм":
        bot.send_message(message.chat.id, 'Вы выбрали раздел мультфильмы')
        maks_rand = len(get_content(animations.content))
        x = random.randint(1, maks_rand)
        content = get_content(animations.text)
        for i in enumerate(content):
            if i[0] == x:
                bot.send_message(message.chat.id, 'Фильм называется : ' + i[1][0])
                bot.send_message(message.chat.id, i[1][1])

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)
