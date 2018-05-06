import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def defensive_roll(self):
        roll = random.randint(1, 12)
        roll = roll * self.level * self.scaliness

        if self.breathes_fire:
            roll = roll * 2

        return roll


class Wizard(Creature):

    def attack(self, creature):
        my_roll =  self.defensive_roll()
        other_roll = creature.defensive_roll()

        return my_roll >= other_roll
