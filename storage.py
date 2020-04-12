import pickle
import os


def write_sent_films(films_info):
    """Func writes names of films, which bot sent.
    films_info  = {film_name:[film_url,img_url,year,genre]}"""
    FILE_NAME = 'sent_films.pickle'
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(films_info, file)


def read_sent_films():
    """Func reads name of films, which bot sent"""
    FILE_NAME = 'sent_films.pickle'
    with open(FILE_NAME, 'rb') as file:
        sent_films = pickle.load(file)
    return sent_films


def check_file_with_films():
    """Check file with sent films in curr directory"""
    FILE_NAME = 'sent_films.pickle'
    cur_directory = os.getcwd()
    files = os.listdir(cur_directory)
    if FILE_NAME in files:
        return True
    else:
        return False


if __name__ == '__main__':
    list_films = ['assa']
    write_sent_films(list_films)
    print(check_file_with_films())
