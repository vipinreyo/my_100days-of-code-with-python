from game import Roll, Person
import random


def print_header():
    print('-------------------------------------------------')
    print('         Rock, Paper, Scissors!!!!               ')
    print('-------------------------------------------------')


def build_three_rolls():
    """
    Building a list of three rolls (Rock, Paper and Scissor). Setting the properties too.
    :return:
    """
    rock = Roll('Rock')
    scissor = Roll('Scissor')
    paper = Roll('Paper')

    rock.rolls_which_can_be_defeated = scissor
    rock.rolls_which_can_defeat_me = paper
    scissor.rolls_which_can_be_defeated = paper
    scissor.rolls_which_can_defeat_me = rock
    paper.rolls_which_can_be_defeated = rock
    paper.rolls_which_can_defeat_me = scissor

    return [rock, scissor, paper]


def get_players_name():
    """
    Getting the name of the player. No error check is done.
    :return:
    """
    name = input('Hello, what is your name? ')
    return name


def game_loop(player1, player2, rolls):
    """
    Game loop.
    No error check is done for the user input
    :param player1:
    :param player2:
    :param rolls:
    :return:
    """
    cnt = 1
    p1_score = 0
    p2_score = 0

    while cnt <= 3:
        p2_roll = random.choice(rolls)
        print(f'Round: {cnt}')
        selection = input('Select your roll. Rock (r), Paper (p) or Scissors (s): ')

        name = None
        if selection == 'r':
            name = 'Rock'
        if selection == 'p':
            name = 'Paper'
        if selection == 's':
            name = 'Scissors'

        for r in rolls:
            if r.name == name:
                p1_roll = r
                break

        outcome = p1_roll.can_defeat(p2_roll)

        if outcome == 'yes':
            winner = f'{player1.name}'
            p1_score += 1
        elif outcome == 'no':
            winner = f'{player2.name}'
            p2_score += 1
        else:
            winner = 'No one'
            p1_score += 1
            p2_score += 1

        print(f'{player1.name} rolled {p1_roll.name}. {player2.name} rolled {p2_roll.name}.')
        print(f'Winner of this round is: {winner}')

        cnt += 1

    if p2_score > p1_score:
        print(f'Winner of the game is {player2.name}')
    elif p1_score > p2_score:
        print(f'Winner of the game is {player1.name}')
    else:
        print('Everyone is a winner!!')


def main():
    print_header()
    rolls = build_three_rolls()

    name = get_players_name()

    player1 = Person(name)
    player2 = Person('Computer')

    game_loop(player1, player2, rolls)


if __name__ == '__main__':
    main()
