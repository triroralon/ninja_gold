from random import randint
import datetime


class Cave:
    def __init__(self):
        self.value = randint(5, 10)
        self.date = datetime.datetime.now()
        self.name = 'cave'

    def new_log(self):
        return {
            'name': self.name,
            'value': self.value,
            'date': self.date
        }

    def cave_gold(self):
        self.date = self.date.strftime("%c")
        print(f"Earned {self.value} Gold from the Cave! on {self.date}")
