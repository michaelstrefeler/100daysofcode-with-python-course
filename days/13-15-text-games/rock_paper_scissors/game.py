# game.py
# a basic rock paper scissors game in python
from classes import Player, Roll
from data_reader import read_rolls
from random import choice


def print_header():
    print('\n---------------------------------')
    print('       Rock Paper Scissors')
    print('---------------------------------')
    print()


def build_all_the_rolls():
    results = read_rolls()
    rolls = []
    for k, v in results.items():
        rolls.append(Roll(k, v[0], v[1]))
    return rolls


def get_players_name():
    name = input("What's your name? ")
    while name.isdigit():
        print("Names don't have numbers in them")
        name = input("What's your name? ")
    return name


def game_loop(player1, player2, rolls):
    count = 0
    while count < 3:
        options = [roll.name for roll in rolls]
        p2_roll = choice(rolls)
        p1_roll = input(f"\nChoose your roll \nYour options are {options} ")

        while p1_roll not in [roll.name for roll in rolls]:
            p1_roll = input(f"Try again: ")

        for roll in rolls:
            if p1_roll == roll.name:
                p1_roll = roll

        outcome = p1_roll.can_defeat(p2_roll)

        print(f'You chose {p1_roll.name}. The computer chose {p2_roll.name}')

        if p1_roll == p2_roll:
            print("It's a tie!")
        else:
            if outcome:
                print(f'{player1.name} wins the round!')
                player1.add_point()
            else:
                print(f'{player2.name} wins the round!')
                player2.add_point()

        if p1_roll != p2_roll:
            count += 1

    # Winner of the game
    if player1.get_points() == player2.get_points():
        print("\nIt's a tie!")
    else:
        if player1.get_points() > player2.get_points():
            print(f"\n{player1.name} wins with {player1.get_points()} points!")
        else:
            print(f"\n{player2.name} wins with {player2.get_points()} points!")


def main():
    print_header()
    rolls = build_all_the_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player('The Computer')

    game_loop(player1, player2, rolls)


if __name__ == '__main__':
    main()
