#!python3

import json
from pprint import pprint
from os import path

base_folder = path.dirname(__file__)
filename = path.join(base_folder, 'mount-data.json')

with open(filename, 'r', encoding='utf-8') as file:
    data = json.loads(file.read())

for item in data['mounts']:
    pprint(item)

# Only the first level is printed.

for item in data['mounts']['collected']:
    pprint(item)

# Prints ALL the data associated with 'collected mounts'.


for item in data['mounts']['collected']:
    pprint(item['name'])

# Prints just the data associated with the 'name' key.


is_flying = []
for mount in data['mounts']['collected']:
    if mount['isFlying']:
        is_flying.append(mount)

# Collects all of the applicable mounts and stores them as a list of dicts

# You can then work with the data as normal:

len(is_flying)
65

for i in is_flying:
    print(i)

for i in is_flying:
    print(i['name'])
