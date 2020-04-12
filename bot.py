import telebot
from config import token
from parse import get_films_info
import requests
from storage import write_sent_films
from storage import read_sent_films
from storage import check_file_with_films

bot = telebot.TeleBot(token)


def send_films():
    CHAT_ID = '-1001227377680'
    IMG_URL_INDEX = 1
    FILM_URL_INDEX = 0
    YEAR_INDEX = 2
    GENRE_INDEX = 3
    output_file = check_file_with_films()
    sent_films = read_sent_films() if output_file else {}
    films_info = get_films_info()
    if films_info is not False:
        films_name = films_info.keys()
        for film in films_name:
            if film in sent_films:
                break
            else:
                img_url = films_info[film][IMG_URL_INDEX]
                img = requests.get(img_url).content
                film_url = films_info[film][FILM_URL_INDEX]
                year = films_info[film][YEAR_INDEX]
                genre = films_info[film][GENRE_INDEX]
                bot.send_photo(chat_id=CHAT_ID, photo=img,
                               caption=f'{film}\n{year}\n{genre}\nСмотреть: {film_url}')
        else:
            write_sent_films(films_info)


if __name__ == '__main__':
    send_films()
