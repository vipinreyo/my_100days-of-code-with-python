from api import MovieSearch


def search_by_movie_name():
    name = input('Movie name: ')

    svc = MovieSearch()
    response = svc.search_movie_by_name(name)
    movies = response.json()

    for idx, movie in enumerate(movies.get('hits'), 1):
        print(f"{idx}. Title: {movie.get('title')}, Director: {movie.get('director')}, "
              f"IMDB code: {movie.get('imdb_code')}")

    print()


def search_by_director_name():
    director_name = input('Director name: ')

    svc = MovieSearch()
    response = svc.search_movie_by_director_name(director_name)
    movies = response.json()

    for idx, movie in enumerate(movies.get('hits'), 1):
        print(f"{idx}. Title: {movie.get('title')}, Director: {movie.get('director')}, "
              f"IMDB code: {movie.get('imdb_code')}")
    print()


def search_by_imdb_code():
    imdb_number = input('IMDB number: ')

    svc = MovieSearch()
    response = svc.search_movie_by_imdb_number(imdb_number)
    movie = response.json()

    print(f"Title: {movie.get('title')}, Director: {movie.get('director')}, IMDB code: {movie.get('imdb_code')}")
    print()


def main():

    print('Movie search APP')
    while True:
        print('What do you want to search Movie with?')

        try:
            select = int(input('(1) Name, (2) Director name, (3) IMDB code? (4) Exit '))
        except Exception:
            raise ValueError

        if select == 1:
            search_by_movie_name()
        elif select == 2:
            search_by_director_name()
        elif select == 3:
            search_by_imdb_code()
        elif select == 4:
            print('Exiting.....')
            break
        else:
            print('Wrong number.....')

        print()


if __name__ == '__main__':
    main()
