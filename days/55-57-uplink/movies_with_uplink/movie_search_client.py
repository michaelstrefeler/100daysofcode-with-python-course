import requests
import uplink


@uplink.response_handler
def raise_for_status(response):
    """Checks whether or not the response was successful."""
    if 200 <= response.status_code < 300:
        # Pass through the response.
        return response

    print('Error unsuccessful request')
    exit()


@uplink.json
@raise_for_status
class MovieSearchClient(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('/api/search/{keyword}')
    def search_by_keyword(self, keyword) -> requests.models.Response:
        """ Returns all movies containing said keyword """

    @uplink.get('/api/director/{director_name}')
    def search_by_director(self, director_name) -> requests.models.Response:
        """ Returns all movies made by said director """

    @uplink.get('/api/movie/{imdb_number}')
    def search_by_code(self, imdb_number) -> requests.models.Response:
        """ Get a movie with the corresponing IMDB code """
