
import requests
import collections
import random

Movie = collections.namedtuple('Movie', 'director, duration, genres, imdb_code, imdb_score,'
                                        'keywords, rating, title, year')


def find_movie_by_title(keyword):
    if not keyword or not keyword.strip():
        raise ValueError('No keyword is given. Please enter one to search')

    imdb_url = f'http://movie_service.talkpython.fm/api/search/{keyword}'
    response = requests.get(imdb_url)
    response.raise_for_status()

    result = response.json()
    result = create_random_errors(result)
    movies = []

    for movie in result.get('hits'):
        movies.append(Movie(**movie))

    return movies


def create_random_errors(result):
    num = random.randint(14, 20)
    if 16 < num <= 18:
        return {}

    if 18 < num < 20:
        raise StopIteration()

    return result


