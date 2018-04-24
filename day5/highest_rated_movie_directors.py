
import os
import csv
from collections import defaultdict, namedtuple, Counter

Movie = namedtuple("Movie", "title year score")

def get_movies_by_director(movie_data_file):
    '''This function will extract movies from the csv and stores them as dictionary, where the key is
    the director and value a named tuple'''

    directors = defaultdict(list)
    with open(movie_data_file) as file:
        movie_data = csv.DictReader(file)

        for row in movie_data:
            mov = Movie(title=row['movie_title'], year=int(row['title_year']), score=float(row['imdb_score']))
            directors[row['director_name']].append(mov)

    return directors


def get_average_scores(directors):
    '''This function will filter directors with minimum 4 movies and calculate the average scores'''
    cnt = Counter()

    for director, movies in directors.items():
        cnt[director] += len(movies)

    director_avg_scores = defaultdict(float)
    for director in cnt.most_common(4):
        director_avg_scores[director] = calc_mean(directors[director])



def calc_mean(movies):
    ''' This is a helper function, which will return the mean of list of Movies'''
    count = len(movies)
    score = 0.0
    for m in movies:
        score += m.score

    return score/count

def main():
    movie_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'movie_metadata.csv')

    print(get_movies_by_director(movie_data_file))




if __name__ == '__main__':
    main()
