from game import Roll, People
import random


def print_header():
    pass


def build_three_rolls():
    return None


def get_players_name():
    return None


def game_loop(player1, player2, rolls):
    cnt = 1

    while cnt < 3:
        p2_roll = random.choice(rolls)
        p1_roll = rolls[0]

        outcome = p1_roll.can_defeat(p2_roll)

        cnt += 1


def main():
    print_header()
    rolls = build_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player('Computer')

    game_loop(player1, player2, rolls)


if __name__ == '__main__':
    main()
