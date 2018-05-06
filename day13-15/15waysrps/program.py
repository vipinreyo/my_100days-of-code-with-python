from game import Roll, Person
import os
import random
import csv
from collections import defaultdict


def print_header():
    print('-------------------------------------------------------')
    print('          15 Ways Rocks, Papers & Scissors              ')
    print('-------------------------------------------------------')


def get_player_name():
    return input('Please enter your name: ')


def read_battle_data_from_file_and_create_rolls():
    rolls = defaultdict(Roll)
    rolls['Rock'] = Roll('Rock')
    rolls['Gun'] = Roll('Gun')
    rolls['Lightning'] = Roll('Lightning')
    rolls['Devil'] = Roll('Devil')
    rolls['Dragon'] = Roll('Dragon')
    rolls['Water'] = Roll('Water')
    rolls['Air'] = Roll('Air')
    rolls['Paper'] = Roll('Paper')
    rolls['Sponge'] = Roll('Sponge')
    rolls['Wolf'] = Roll('Wolf')
    rolls['Tree'] = Roll('Tree')
    rolls['Human'] = Roll('Human')
    rolls['Snake'] = Roll('Snake')
    rolls['Scissors'] = Roll('Scissors')
    rolls['Fire'] = Roll('Fire')

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'battle-table.csv')) as f:
        header = next(f).strip().split(',')
        reader = csv.reader(f)

        for row in reader:
            roll_name = row[0].strip()

            for i, item in enumerate(row, start=1):
                if item == 'draw':
                    rolls[roll_name].draw.append(header[i-1])
                if item == 'win':
                    rolls[roll_name].win.append(header[i-1])
                if item == 'lose':
                    rolls[roll_name].lose.append(header[i-1])

    return rolls


def list_rolls():
    rolls_with_index = dict()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'battle-table.csv')) as f:
        header = next(f)

        for index, roll in enumerate(header.split(',')[1:], start=1):
            print(f'{roll.strip()} ({index})  ', end="")
            rolls_with_index[index] = roll

    return rolls_with_index


def game_loop():
    player1 = Person(get_player_name())
    player2 = Person('Computer')

    rolls = read_battle_data_from_file_and_create_rolls()
    p1_win = p2_win = 0

    cnt = 1
    while cnt <= 3:
        p2_roll = random.choice(list(rolls.values()))

        print()
        print('----------------------------------------------------------')
        print(f'   Hello {player1.name}, here are your available rolls   ')
        print('----------------------------------------------------------')
        print()

        rolls_with_index_nr = list_rolls()
        print('\n')
        selection = int(input('Please select your roll: '))
        p1_roll = rolls[rolls_with_index_nr[selection]]
        outcome = p1_roll.can_defeat(p2_roll)

        print(f'{player1.name} selected {p1_roll.name}. {player2.name} selected {p2_roll.name}.')
        if outcome == 'yes':
            p1_win += 1
            print(f'{player1.name} wins this round')
        if outcome == 'no':
            p2_win += 1
            print(f'{player2.name} wins this round!!')
        if outcome == 'draw':
            p1_win += 1
            p2_win += 1
            print(f'Its a tie!!')

        cnt += 1

    print('*************************************************')
    if p1_win == p2_win:
        print('Everyone is a winner!!')
    if p1_win > p2_win:
        print(f'{player1.name} is the final Winner!!!')
    if p2_win > p1_win:
        print(f'{player2.name} is the final Winner!!!')
    print('*************************************************')

def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
