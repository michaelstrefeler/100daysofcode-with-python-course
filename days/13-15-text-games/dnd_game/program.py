from actors import Creature, Dragon, Wizard
import random


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------------------')
    print('       AMAZING WIZARD GAME')
    print('---------------------------------')
    print()


def game_loop():
    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 50, scaliness=2, breaths_fire=False),
        Wizard('Evil wizard', 1000),
    ]

    hero = Wizard('Gandalf', 75)  # It's Gandalf not Gandolf

    while True:

        active_creature = random.choice(creatures)

        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print(f"The wizard defeated {active_creature.name}")
            else:
                acn = {active_creature.name}
                print(f"The wizard has been defeated by the powerful {acn}")
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print(f'The wizard {hero.name} looks around and sees:')
            for c in creatures:
                print(f" * {c.name} of level {c.level}")
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


if __name__ == '__main__':
    main()
