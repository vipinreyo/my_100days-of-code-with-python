from unittest.mock import patch
import random
import pytest

from guess import get_random_number, Game


@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17


@patch("builtins.input", side_effect=[11, '12', 'Vipin', 12, 5, -1, 21, 7, None])
def test_guess(input):
    game = Game()

    # good
    assert game.guess() == 11
    assert game.guess() == 12

    # not a number
    with pytest.raises(ValueError):
        game.guess()

    # number already guessed
    with pytest.raises(ValueError):
        game.guess()

    # good
    assert game.guess() == 5

    # out of range
    with pytest.raises(ValueError):
        game.guess()

    # out of range
    with pytest.raises(ValueError):
        game.guess()

    # good
    assert game.guess() == 7

    # No input
    with pytest.raises(ValueError):
        game.guess()


def test_validate_guess(capfd):
    game = Game()
    game._answer = 2

    assert not game.validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '1 is too low'

    assert not game.validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'

    assert game.validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '2 is correct!'


@patch('builtins.input', side_effect=[4, 22, 9, 4, 6])
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 6

    game()

    assert game._win is True

    out = capfd.readouterr()[0]
    expected = ['4 is too low', 'Number 22 not in range',
                '9 is too high', 'Number 4 already guessed',
                '6 is correct!', 'It took you 3 guesses']

    output = [line.strip() for line in out.split('\n') if line.strip()]

    for line, exp in zip(output, expected):
        assert line == exp


@patch('builtins.input', side_effect=[None, 11, 12, 15, 16, 5])
def test_game_loss(inp, capfd):
    game = Game()
    game._answer = 7

    game()

    assert not game._win

    out = capfd.readouterr()[0]
    expected = ['Please enter a number.', '11 is too high',
                '12 is too high', '15 is too high',
                '16 is too high', '5 is too low',
                'Guessed 5 times, answer was 7']

    output = [line.strip() for line in out.split('\n') if line.strip()]
    for line, exp in zip(output, expected):
        assert line == exp
