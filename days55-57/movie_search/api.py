import requests
import uplink

from uplink_helpers import raise_for_status


@raise_for_status
class MovieSearch(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url="http://movie_service.talkpython.fm/")

    @uplink.get('api/search/{name}')
    def search_movie_by_name(self, name) -> requests.models.Response:
        """ Get the movie details by name from server"""

    @uplink.get('api/director/{director_name}')
    def search_movie_by_director_name(self, director_name) -> requests.models.Response:
        """ Get the movie details by director name from server"""

    @uplink.get('api/movie/{imdb_number}')
    def search_movie_by_imdb_number(self, imdb_number):
        """ Get the movie details by imdb code"""
