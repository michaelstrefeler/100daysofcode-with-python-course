from os import path
from csv import DictReader
from collections import namedtuple
from typing import List

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

    return data


def get_countries():
    return [c.country for c in data]


def format_row(row):
    row['beer_servings'] = int(row['beer_servings'])
    row['spirit_servings'] = int(row['spirit_servings'])
    row['wine_servings'] = int(row['wine_servings'])
    row['total_litres_of_pure_alcohol'] = float(
        row['total_litres_of_pure_alcohol'])

    return Record(**row)


def get_country_stats(choice) -> List[Record]:
    return [c for c in data if c.country == choice]


def beeriest_countries() -> List[Record]:
    return sorted(data, key=lambda r: -r.beer_servings)


def hightest_spirit_countries() -> List[Record]:
    return sorted(data, key=lambda r: -r.spirit_servings)


def winiest_countries() -> List[Record]:
    return sorted(data, key=lambda r: -r.wine_servings)


def alcohlic_countries() -> List[Record]:
    return sorted(data, key=lambda r: -r.total_litres_of_pure_alcohol)
