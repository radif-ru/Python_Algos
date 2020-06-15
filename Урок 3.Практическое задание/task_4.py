"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import randint

MASSIVE = [randint(-3, 3) for el in range(randint(10, 20))]

print(f"В массиве {MASSIVE} \nчисло {max(MASSIVE, key=lambda x: MASSIVE.count(x))}"
      f" встречается чаще всего")

# Почему ругается Pylint на lambda? Из-за того, что может не оказаться одинаковых чисел?:
# task_4.py:11:67: W0108: Lambda may not be necessary (unnecessary-lambda)
