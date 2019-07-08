from random import randint
import datetime


class Farm:
    def __init__(self):
        self.value = randint(10, 20)
        self.date = datetime.datetime.now().strftime("%c")
        self.name = "farm"

    def farm_gold(self):
        self.date = self.date.strftime("%c")
        return f"Earned {self.value} Gold from the Farm! on {self.date}"

    def new_log(self):
        return {
            'name': self.name,
            'value': self.value,
            'date': self.date
        }


if __name__ == "__main__":
    farm = Farm()
    farm.farm_gold()
