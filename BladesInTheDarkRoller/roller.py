from random import randint


class Roller:
    """Main object of the module."""

    def actionRoll(self, dice):
        """This is the basic action roll.
        Takes an integer number of dice as argument."""

        if dice < 1:
            rolled0 = True
            print()
            pool = [randint(1, 6), randint(1, 6)]
            NoDieWarning = "*Rolling two dice but taking the lowest.*"
        else:
            rolled0 = False
            pool = [randint(1, 6) for die in range(dice)]

        if rolled0:
            if min(pool) == 6:
                return (
                    f"""Success / Good Result.  
            {NoDieWarning}""",
                    pool,
                )
            elif min(pool) in [4, 5]:
                return (
                    f"""Partial Success / Mixed Result.  
                    {NoDieWarning}""",
                    pool,
                )
            else:
                return (
                    f"""Failure / Bad Result.  
            {NoDieWarning}""",
                    pool,
                )
        else:
            if pool.count(6) > 1:
                return "Critical Success! Exceptional Result!", pool
            elif max(pool) == 6:
                return "Success / Good Result", pool
            elif max(pool) in [4, 5]:
                return "Partial Success / Mixed Result.", pool
            else:
                return "Failure / Bad Result.", pool

    def resistanceRoll(self, dice):
        """This is the roll used to resist the consequences you don't like.
        Takes a integer number of dice as argument and returns a string about
        stress suffered (or gained)."""
        pool = [randint(1, 6) for die in range(dice)]
        if pool.count(6) > 1:
            return "Critical Success! Clear 1 Stress.", pool
        else:
            stress = 6 - max(pool)
            return f"Suffer {stress} stress. (6 minus best die.)", pool

    def fortuneRoll(self, dice):
        """When you need a simple fortune roll."""
        return self.actionRoll(dice)

    def engagementRoll(self, engagementDice):
        return self.actionRoll(engagementDice)


if __name__ == "__main__":
    roller = Roller()
    print(roller.actionRoll(3))
