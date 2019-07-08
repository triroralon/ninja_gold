from django.db import models
from random import randint
import datetime


class House:
    def __init__(self):
        self.value = randint(2, 5)
        self.date = datetime.datetime.now().strftime("%c")
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


class Casino:
    def __init__(self):
        self.value = randint(-50, 50)
        self.date = datetime.datetime.now().strftime("%c")
        self.name = 'casino'

    def new_log(self):
        return {
            'name': self.name,
            'value': self.value,
            'date': self.date
        }

    def casino_gold(self):
        self.date = self.date.strftime("%c")
        if self.value >= 0:
            return (f"<p class='positive'>Earned {self.value}"
                    " Gold from the Casino! on {self.date}</p>")
        else:
            return (f"<p class='negative'>Lost {abs(self.value)}"
                    " Gold at the Casino! on {self.date}</p>")


class Cave:
    def __init__(self):
        self.value = randint(5, 10)
        self.date = datetime.datetime.now().strftime("%c")
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
