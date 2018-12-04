#!python3

import json
from pprint import pprint
from os import path

base_folder = path.dirname(__file__)
filename = path.join(base_folder, 'mount-data.json')

with open(filename, 'r', encoding='utf-8') as file:
    data = json.loads(file.read())

for item in data.items():
    print(item)

# Hard to read

for item in data.items():
    pprint(item)

# easier to read
