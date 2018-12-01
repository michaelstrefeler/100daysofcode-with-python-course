from os import path
from csv import DictReader
from collections import namedtuple

data = []

Record = namedtuple(
    'Record', 'country, beer_servings, spirit_servings, wine_servings,'
    'total_litres_of_pure_alcohol')


def get_data():
    base_folder = path.dirname(__file__)
    filename = path.join(base_folder, 'data', 'drinks.csv')

    with open(filename, 'r', encoding='utf-8') as file:
        reader = DictReader(file)

        data.clear()
        for row in reader:
            record = format_row(row)
            data.append(record)

    print(data)


def format_row(row):
    row['beer_servings'] = int(row['beer_servings'])
    row['spirit_servings'] = int(row['spirit_servings'])
    row['wine_servings'] = int(row['wine_servings'])
    row['total_litres_of_pure_alcohol'] = float(
        row['total_litres_of_pure_alcohol'])

    return Record(**row)