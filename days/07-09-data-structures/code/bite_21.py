# bite_21.py
# Query a nested data structure

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ')
       separated string of jeep models (original order)"""
    return ', '.join([jeep for jeep in cars['Jeep']])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [cars[k][0] for k in cars.keys()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    models = []
    for car_list in cars.values():
        for car in car_list:
            if grep.lower() in car.lower():
                models.append(car)
    return sorted(models)


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    for k, v in cars.items():
        cars[k] = sorted(v)
    return cars
