import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from requests.exceptions import HTTPError


def check_connect(site_url):
    try:
        response = requests.get(site_url)
    except HTTPError as http_err:
        print('Http error{0}'.format(http_err))
        return False
    except Exception as exc:
        print('Error {0}'.format(exc))
        return False
    if response.status_code == 404:
        print('Page not found')
        return False
    return response.text


def get_films_info():
    SITE_URL = 'http://pic-top.online/'
    films_info = defaultdict(list)
    response = check_connect(SITE_URL)
    if response:
        soup = BeautifulSoup(response, 'html.parser')
        END_YEAR_INDEX = 9
        START_GENRE_INDEX = 14
        films = soup.find_all('div', class_="col-12 col-sm-6 col-md-4 pt-4 one_film_block pb-4")
        for film in films:
            film_url = film.find('a', class_='a_no_d').get('href')
            full_film_url = SITE_URL + film_url
            img_url = film.find('img').get('src')
            full_img_url = SITE_URL + img_url
            title_block = film.find('div', class_='title_list_film pt-3 pt-md-0 text-center')
            title = title_block.find('a').text
            year_genre = film.find('div', class_='char_list_film text-center').text
            year = year_genre[:END_YEAR_INDEX]
            genre = year_genre[START_GENRE_INDEX:]
            films_info[title].append(full_film_url)
            films_info[title].append(full_img_url)
            films_info[title].append(year)
            films_info[title].append(genre)
        return dict(films_info)


if __name__ == '__main__':
    get_films_info()
