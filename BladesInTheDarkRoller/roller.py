from random import randint


class Roller:
    """Main object of the module."""

    def actionRoll(self, dice):
        """This is the basic action roll.
        Takes an integer number of dice as argument."""
        if dice < 1:
            pool = [min([randint(1, 6), randint(1, 6)])]
        else:
            pool = [randint(1, 6) for die in range(dice)]
        if pool.count(6) > 1:
            return "Critical Success! Exceptional Result!"
        elif max(pool) == 6:
            return "Success / Good Result"
        elif max(pool) in [4, 5]:
            return "Partial Success / Mixed Result"
        else:
            return "Failure / Bad Result"

    def resistanceRoll(self, dice):
        """This is the roll used to resist the consequences you don't like.
        Takes a integer number of dice as argument and returns a string about
        stress suffered (or gained)."""
        pool = [randint(1, 6) for die in range(dice)]
        if pool.count(6) > 1:
            return "Critical Success! Clear 1 Stress."
        else:
            stress = 6 - max(pool)
            return f"Suffer {stress} stress."

    def fortuneRoll(self, dice):
        """When you need a simple fortune roll."""
        return self.actionRoll(dice)

    def engagementRoll(self, engagementDice):
        return self.actionRoll(engagementDice)


if __name__ == "__main__":
    roller = Roller()
    print(roller.actionRoll(3))
