from actors import Creature, Dragon, Wizard
import random


def print_header():
    print('-------------------------------------------------')
    print('                  WIZARD GAME                    ')
    print('-------------------------------------------------')


def game_loop():
    creatures = [Creature('Bat', 5),
                 Creature('Toad', 1),
                 Creature('Tiger', 12),
                 Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False),
                 Wizard('Evil Wizard', 1000)]

    hero = Wizard('Gandalff', 75)

    while True:
        active_creature = random.choice(creatures)

        print(f'A {active_creature.name} of {active_creature.level} has arrived from the forest.')
        selection = input('What do you want to do? attack (a), run away (r), look around (l): ')

        if selection == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print(f'{hero.name} defeated {active_creature.name}.')
        elif selection == 'r':
            print(f'Wizard {hero.name} ran away safely.')
        elif selection == 'l':
            print(f'Wizard {hero.name} looks around and sees the following:')
            for c in creatures:
                print(c.name)
        else:
            print('Exiting the game....Bye')
            break


def main():
    print_header()
    game_loop()

if __name__ == '__main__':
    main()
