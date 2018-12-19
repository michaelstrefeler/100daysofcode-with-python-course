from movie_search_client import MovieSearchClient


def main():

    print("How would you like to search for a movie?")
    choice = input("By [k]eyword, by [d]irector or my [c]ode ")

    if choice.lower() == 'k':
        search_by_keyword()
    elif choice.lower() == 'd':
        search_by_director()
    elif choice.lower() == 'c':
        search_by_code()
    else:
        print('Inchoiceid input')
        exit()


def search_by_keyword():
    keyword = input('Enter a keyword to seach for movies ')

    client = MovieSearchClient()

    response = client.search_by_keyword(keyword)
    movies = response.json()

    for movie in movies.get('hits'):
        print(f"{movie.get('title')} - {movie.get('year')}")

    if movies.get('hits') == []:
        print('No results found')
    return 'It worked'


def search_by_director():
    director = input('Choose a director to search for his/her movies ')

    client = MovieSearchClient()

    response = client.search_by_director(director)
    movies = response.json()

    for movie in movies.get('hits'):
        print(f"{movie.get('title')} - {movie.get('year')}")

    if movies.get('hits') == []:
        print('No results found')
    return 'It worked'


def search_by_code():
    # tt0096754
    code = input('Enter an IMDB code to see what movie it corresponds to ')

    client = MovieSearchClient()

    response = client.search_by_code(code)
    movie = response.json()

    if movie:
        print(movie.get('imdb_code'))
        print()
        print(f"{movie.get('title')} by {movie.get('director')}")
        print(f"Came out in {movie.get('year')}")
        print(f"With an IMDB score of {movie.get('imdb_score')}")
    else:
        print('No results found')

    return 'It worked'


if __name__ == '__main__':
    main()
