from threading import Thread
import time


class Knight(Thread):
    """Класс для создание рыцаря"""
    POWER = 100

    def __init__(self, name: str, counter: int):
        super().__init__()
        self.name = name
        self.counter = counter

    def run(self):
        days = 0
        while self.POWER:
            print(f'{self.name} на нас напали')
            print(f'{self.name} сражается {days + 1} день(дня)..., осталось {self.POWER - self.counter} воинов')
            days += 1
            self.POWER = self.POWER - self.counter
            time.sleep(0.01)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_khight = Knight('Sir Lancelot', 10)
second_khight = Knight('Sir Galahad', 20)

first_khight.start()
second_khight.start()

first_khight.join()
second_khight.join()

print('Все битвы закончились!')
