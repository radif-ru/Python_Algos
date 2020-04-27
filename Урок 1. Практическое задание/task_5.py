"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""

try:
    USER_VAL = input(
        "Введите 2 латинские буквы, через запятую, пробел или подряд: ")
    LETTER_1 = ''
    LETTER_2 = ''

    for val in USER_VAL:
        if val.isalpha() and not LETTER_1:
            LETTER_1 = val.lower()
        elif val.isalpha() and not LETTER_2:
            LETTER_2 = val.lower()

    LETTER_1_NUM = ord(LETTER_1)
    LETTER_2_NUM = ord(LETTER_2)
    LETTERS_BETWEEN = abs(LETTER_2_NUM - LETTER_1_NUM) - 1
except TypeError as exception:
    print(
        f"Введите как минимум 2 латинские буквы, если букв больше - остальные не учитываются!\n"
        f"{exception}")
else:
    print(
        f"Колличество букв между {LETTER_1} и {LETTER_2} раво {LETTERS_BETWEEN}")
