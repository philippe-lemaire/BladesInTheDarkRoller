from random import randint
import pyinputplus as pyip


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
        advantageDice = pyip.inputInt(prompt="How many major advantages?\n")
        disadvantageDice = pyip.inputInt(prompt="How many major disadvantages?\n")
        dice = dice + advantageDice - disadvantageDice
        return self.actionRoll(dice)

    def engagementRoll(self):
        """This is the engagement roll. No argument. Asks questions
        about the operation to constitute a dice pool."""
        # dice starts at 1 for sheer luck
        dice = 1
        bold = pyip.inputYesNo("Is the operation particularly bold or daring? ")
        if bold == "yes":
            dice += 1
            print("+1 advantage dice.")
        complex = pyip.inputYesNo(
            "Is the operation overly complex or contingent on many factors? "
        )
        if complex == "yes":
            dice -= 1
            print("-1 advantage dice.")
        vulnerable = pyip.inputYesNo(
            "Does the plan's detail expose a vulnerability of the target or hit them where they're weakest? "
        )
        if vulnerable == "yes":
            dice += 1
            print("+1 advantage dice.")
        defended = pyip.inputYesNo(
            "Is the target strongest against this approach, or do they have particular defenses or special defenses or special preparations? "
        )
        if defended == "yes":
            dice -= 1
            print("-1 advantage dice.")
        aid = pyip.inputYesNo(
            "Can any of your friends or contacts provide aid or insight for this operation? "
        )
        if aid == "yes":
            dice += 1
            print("+1 advantage dice.")
        interference = pyip.inputYesNo(
            "Are any enemies or rivals interfering in the operation? "
        )
        if interference == "yes":
            dice -= 1
            print("-1 advantage dice.")
        otherFactors = pyip.inputInt(
            "Is there any other factor to consider? Input 0, or a positive/negative integer for advantage / disadvantage respectively. "
        )
        dice += otherFactors

        print(f"The dice pool is {dice}. Let's roll…")

        # the dice pool is ready, we will reuse actionRoll() with our dice pool.
        return self.actionRoll(dice)


if __name__ == "__main__":
    roller = Roller()
    print(roller.actionRoll(3))
