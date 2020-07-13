"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

from random import random

print("Случайное целое число:")
try:
    LEFT = input("Минимальная граница: ")
    RIGHT = input("Максимальная граница: ")

    if float(LEFT) % 1 != 0 or float(RIGHT) % 1 != 0:
        raise ValueError("Дробные числа запрещены!")

    LEFT = int(LEFT)
    RIGHT = int(RIGHT)
except ValueError as exception:
    print(f"Ошибка ввода данных. Используйте целые числа \n"
          f"{exception}")
else:
    NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
    print(NUMB)

print("Случайное вещественное число:")
try:
    LEFT = float(input("Минимальная граница: "))
    RIGHT = float(input("Максимальная граница: "))
except ValueError as exception:
    print(f"Ошибка ввода данных. Используйте вещественное число \n"
          f"{exception}")
else:
    NUMB = random() * (RIGHT - LEFT) + LEFT
    print(f"{NUMB:.3f}")

print("Случайный символ:")
try:
    LEFT = ord(input("Символ минимальной границы: "))
    RIGHT = ord(input("Символ максимальной границы: "))
    NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
    print(chr(NUMB))
except TypeError as exception:
    print(f"Вы ввели некорректное значение!\n"
          f"{exception}")
