from random import randint
import datetime


class House:
    def __init__(self):
        self.value = randint(2, 5)
        self.date = datetime.datetime.now()
        self.name = 'house'

    def new_log(self):
        return {
            'name': self.name,
            'value': self.value,
            'date': self.date
        }

    def house_gold(self):
        self.date = self.date.strftime("%c")
        print(f"Earned {self.value} Gold from the House! on {self.date}")
