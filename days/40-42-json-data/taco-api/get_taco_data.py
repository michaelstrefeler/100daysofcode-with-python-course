from json import loads
from os import makedirs, path
from requests import get


def get_taco():
    '''Gets random taco from the API'''
    r = get('http://taco-randomizer.herokuapp.com/random')
    taco = loads(r.text)
    print('Welcome to the random taco generator!!\n')
    print("Here's your randomly generated taco. Enjoy!")
    return taco


def get_shell(taco):
    '''Prints and returns the taco shell'''
    print(f"Shell: {taco['shell']['name']}")
    return taco['shell']


def get_base_layer(taco):
    '''Prints and returns the taco's base layer'''
    print(f"Base layer: {taco['base_layer']['name']}")
    return taco['base_layer']


def get_mixin(taco):
    '''Prints and returns what you mix in with the base layer'''
    print(f"Mixin: {taco['mixin']['name']}")
    return taco['mixin']


def get_condiment(taco):
    '''Prints and returns the condiment to use'''
    print(f"Condiment: {taco['condiment']['name']}")
    return taco['condiment']


def get_seasoning(taco):
    '''Prints and returns the seasoning to use'''
    print(f"Seasoning: {taco['seasoning']['name']}")
    return taco['seasoning']


def wants_full_recipe(taco):
    '''Asks user if they want the recipe. If yes runs get_full_recipe()
       If not exits script'''
    answer = input('\nWould you like the full recipe? (Y/N) ')
    answer = answer.upper()
    if answer == 'Y':
        print('\nOk here it comes')
        get_full_recipe(taco)
    else:
        print('\nOh well. Your loss')
        exit()


def get_full_recipe(taco):
    '''Writes full recipe in file
       and puts it in the same folder as the python script'''

    base_folder = path.dirname(__file__)

    shell = taco['shell']['name']
    main = taco['base_layer']['name']
    mixin = taco['mixin']['name']
    c = taco['condiment']['name']
    s = taco['seasoning']['name']

    recipe_path = path.join(base_folder, 'recipes')

    if not path.exists(recipe_path):
        makedirs(recipe_path)

    recipe_name = f"{shell}+{main}+{mixin}_taco.md"
    filename = path.join(recipe_path, recipe_name)

    with open(filename, 'w+', encoding='utf-8') as recipe:
        title = f'# {main} & {mixin} with {c} and {s} in/in a {shell}'
        recipe.write(title)
        recipe.write(f"\n\n## {taco['shell']['recipe']}")
        recipe.write(f"\n\n## {taco['base_layer']['recipe']}")
        recipe.write(f"\n\n## {taco['mixin']['recipe']}")
        recipe.write(f"\n\n## {taco['condiment']['recipe']}")
        recipe.write(f"\n\n## {taco['seasoning']['recipe']}")


if __name__ == '__main__':
    taco = get_taco()
    shell = get_shell(taco)
    base_layer = get_base_layer(taco)
    mixin = get_mixin(taco)
    condiment = get_condiment(taco)
    seasoning = get_seasoning(taco)
    answer = wants_full_recipe(taco)
