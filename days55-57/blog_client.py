import datetime

import requests
import uplink

from uplink_helpers import raise_for_status


@uplink.json
@raise_for_status
class BlogClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://consumer_services_api.talkpython.fm/')

    @uplink.get('/api/blog')
    def all_entries(self) -> requests.models.Response:
        """ Gets all the blog entries from the server """

    @uplink.get('/api/blog/{post_id}')
    def entry_by_id(self, post_id) -> requests.models.Response:
        """ Get's a blog entry from the server"""

    # noinspection PyTypeChecker
    def add_new_entry(self, title: str, content: str, views=0) -> requests.models.Response:
        published = datetime.datetime.now().isoformat()
        return self.__create_a_new_entry(title=title, content=content, view_count=views, published=published)

    @uplink.post('/api/blog')
    def __create_a_new_entry(self, **kwargs: uplink.Body) -> requests.models.Response:
        """ Create a new entry in the server"""

