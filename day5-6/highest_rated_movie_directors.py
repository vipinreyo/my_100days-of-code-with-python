
import os
import csv
from collections import defaultdict, namedtuple, Counter

NUM_OF_TOP_DIRECTORS = 20
MIN_NR_OF_MOVIES = 4
MOVIE_FILE = "movie_metadata.csv"
YEAR_OF_MOVIE = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    '''This function will extract movies from the csv and stores them as dictionary, where the key is
    the director and value a named tuple'''

    directors = defaultdict(list)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', MOVIE_FILE)) as file:
        for row in csv.DictReader(file):
            try:
                title = row['movie_title']
                year = int(row['title_year'])
                score = float(row['imdb_score'])
            except ValueError:
                continue

            if year < YEAR_OF_MOVIE:
                continue

            movie = Movie(title=title, year=year, score=score)
            directors[row['director_name']].append(movie)

    return directors


def get_average_scores(directors):
    '''This function will filter directors with minimum 4 movies and calculate the average scores'''
    return {(director, calc_mean(movies)): movies
            for director, movies in directors.items()
            if len(movies) >= MIN_NR_OF_MOVIES}


def calc_mean(movies):
    ''' This is a helper function, which will return the mean of list of Movies'''

    score = [m.score for m in movies]
    mean = sum(score)/max(1, len(movies))

    return round(mean, 1)


def print_results(directors):
    format_counter_director_score = '{counter}. {director:<52} {avg}'
    sep_line = '-' * 60
    format_year_title_rating = '{year}] {title:<50} {rating}'

    for counter, (director_rating, movie) in \
            enumerate(sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)[:NUM_OF_TOP_DIRECTORS], 1):
            director, avg = director_rating

            print()
            print(format_counter_director_score.format(counter=counter, director=director, avg=avg))
            print(sep_line)

            for mov in sorted(movie, key=lambda m: m.score, reverse=True):
                print(format_year_title_rating.format(year=mov.year, title=mov.title, rating=mov.score))


def main():

    directors = get_movies_by_director()
    director_avg_movies = get_average_scores(directors)
    print_results(director_avg_movies)


if __name__ == '__main__':
    main()
