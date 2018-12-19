import requests
import uplink


@uplink.json
class MovieSearchClient(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('/api/search/{keyword}')
    def search(self, keyword) -> requests.models.Response:
        """ Returns all movies containing said keyword """

    @uplink.get('/api/director/{director_name}')
    def get_director(self, director) -> requests.models.Response:
        """ Returns all movies made by said director """

    @uplink.get('/api/movie/{imdb_number}')
    def get_imdb_code(self, code) -> requests.models.Response:
        """ Get a movie with the corresponing IMDB code """
