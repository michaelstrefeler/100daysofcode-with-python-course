# list_movies_by_actor.py
# Takes data from movies.csv and lists movies
# that have a specific main actor in them
from collections import defaultdict, namedtuple
import csv
from urllib.request import urlretrieve

movie_data = 'https://bit.ly/2SniwTk'  # Shortened link
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title director year score')


def get_movies_by_actor(data=movies_csv):
    """Extracts all movies from a csv and stores them in a dictionary
        where keys are actors, and values is a list of movies"""
    actors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                actor = line['actor_1_name']
                title = line['movie_title'].replace('\xa0', '')
                director = line['director_name']
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            m = Movie(title=title, director=director, year=year, score=score)
            actors[actor].append(m)
    return actors


actors = get_movies_by_actor()
available_actors = actors.keys()

choice = input('Choose an actor to see what movies they lead in: ')

while choice not in available_actors:
    print('\nThe actor you chose is not in the list, try again')
    print('Make sure you are spelling there name correctly')
    choice = input('Choose an actor to see what movies they lead in: ')

movies = actors[choice]

for movie in movies:
    print(f'\n{movie.title}\n\
  Director: {movie.director}\n\
  Year: {movie.year}\n\
  IMDB score: {movie.score}')
