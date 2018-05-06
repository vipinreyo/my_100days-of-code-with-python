
class Roll:

    def __init__(self, name):
        self.name = name
        self.win = []
        self.lose = []
        self.draw = []

    def can_defeat(self, other_roll):
        if other_roll.name in self.win:
            return 'yes'

        if other_roll.name in self.lose:
            return 'no'

        if other_roll.name in self.draw:
            return 'draw'


class Person:

    def __init__(self, name):
        self.name = name
