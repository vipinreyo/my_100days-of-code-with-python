
class Roll:
    def __init__(self, name):
        self.name = name
        self.rolls_which_can_be_defeated = None
        self.rolls_which_can_defeat_me = None

    def can_defeat(self, roll):
        if self.rolls_which_can_be_defeated.name == roll.name:
            return 'yes'
        elif self.rolls_which_can_defeat_me.name == roll.name:
            return 'no'
        else:
            return 'tie'


class Person:
    def __init__(self, name):
        self.name = name

