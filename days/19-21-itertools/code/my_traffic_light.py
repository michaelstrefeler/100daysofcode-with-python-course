from itertools import cycle
from random import randint
from sys import stdout
from time import sleep


def traffic_lights():
    """Switch from green to amber to red to amber and so on"""
    order = cycle(['Green', 'Amber', 'Red', 'Amber'])
    while True:
        wait_time = randint(2, 7)
        stdout.write('\r' + ' ' * 5)
        stdout.flush()
        stdout.write('\r' + next(order))
        stdout.flush()
        sleep(wait_time)


if __name__ == '__main__':
    traffic_lights()
