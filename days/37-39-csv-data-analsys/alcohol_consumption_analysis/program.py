import analyse


def main():
    print("Alcohol consumption by country, 2014")
    print("The data is sorted by servings per person")
    analyse.get_data()
    countries = analyse.get_countries()

    choice = input("Choose a country to see it's stats: ")

    while choice not in countries:
        choice = input("Invalid input, try again: ")

    data = analyse.get_country_stats(choice)[0]
    print(f'\n{data.country} consumed:')
    print(f'{data.beer_servings} servings of beer')
    print(f'{data.spirit_servings} servings of spirits')
    print(f'{data.wine_servings} servings of wine')
    print('Which all adds up to a total of')
    print(f'{data.total_litres_of_pure_alcohol} Liters of alcohol per person')
    print('In 2014')

    print('\n\nTop 5 countries by servings of beer per person')
    beeriest = analyse.beeriest_countries()
    for idx, c in enumerate(beeriest[:5]):
        print(f'{idx + 1}. {c.country}: {c.beer_servings}')

    print('\n\nTop 5 countries by servings of spirits per person')
    highest_spirit = analyse.hightest_spirit_countries()
    for idx, c in enumerate(highest_spirit[:5]):
        print(f'{idx + 1}. {c.country}: {c.spirit_servings}')

    print('\n\nTop 5 countries by servings of wine per person')

    winiest = analyse.winiest_countries()
    for idx, c in enumerate(winiest[:5]):
        print(f'{idx + 1}. {c.country}: {c.wine_servings}')

    print('\n\nTop 5 countries by total amount of alchol consumed')
    alcoholics = analyse.alcohlic_countries()
    for idx, c in enumerate(alcoholics[:5]):
        print(f'{idx + 1}. {c.country}: {c.total_litres_of_pure_alcohol}')


if __name__ == '__main__':
    main()