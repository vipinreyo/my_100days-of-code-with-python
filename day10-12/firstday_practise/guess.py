import random

MAX_GUESSES = 5
START = 1
END = 20


def get_random_number():
    return random.randint(START, END)


class Game:
    def __init__(self):
        self._answer = get_random_number()
        self._guesses = set()
        self._win = False

    def guess(self):
        """
          Ask the user for an input, convert to integer, raise ValueError outputting the following conditions
          Please enter a numbera
          Should be integer
          Number not in range
          Already guessed

          If no error return the guessed integer
        """
        guess = input(f'Guess a number between {START} and {END} ')

        if not guess:
            raise ValueError('Please enter a number.')

        try:
            guess = int(guess)

        except ValueError:
            raise ValueError('Please enter a integer')

        if guess not in range(START, END + 1):
            raise ValueError(f'Number {guess} not in range')

        if guess in self._guesses:
            raise ValueError(f'Number {guess} already guessed')

        self._guesses.add(guess)
        return guess

    @property
    def num_guesses(self):
        return len(self._guesses)

    def validate_guess(self, guess):
        """
        Verify if guess is correct. Print the following if applicable
        {guess} is correct!
        {guess} is too low
        {guess} is too high
        """
        if self._answer == guess:
            print(f'{guess} is correct!')
            return True
        else:
            high_or_low = 'high' if guess > self._answer else 'low'
            print(f'{guess} is too {high_or_low}')
            return False

    def __call__(self):
        while len(self._guesses) < MAX_GUESSES:
            try:
                guess = self.guess()
            except ValueError as ve:
                print(ve)
                continue

            self._win = self.validate_guess(guess)
            if self._win:
                guess_str = self.num_guesses == 1 and "guess" or "guesses"
                print(f'It took you {self.num_guesses} {guess_str}')
                break
        else:
            print(f'Guessed {MAX_GUESSES} times, answer was {self._answer}')


if __name__ == '__main__':
    game = Game()
    game()
