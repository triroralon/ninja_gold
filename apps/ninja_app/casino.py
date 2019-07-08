from random import randint
import datetime


class Casino:
    def __init__(self):
        self.value = randint(-50, 50)
        self.date = datetime.datetime.now()
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


if __name__ == "__main__":
    casino = Casino()
    casino.casino_gold()
