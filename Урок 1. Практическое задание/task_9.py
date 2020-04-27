"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

try:
    USER_NUM_1 = float(input("Введите 1 число: "))
    USER_NUM_2 = float(input("Введите 2 число: "))
    USER_NUM_3 = float(input("Введите 3 число: "))

    if USER_NUM_2 < USER_NUM_1 < USER_NUM_3 or USER_NUM_2 > USER_NUM_1 > USER_NUM_3:
        print(f"1 число {USER_NUM_1} является средним")
    elif USER_NUM_1 < USER_NUM_2 < USER_NUM_3 or USER_NUM_1 > USER_NUM_2 > USER_NUM_3:
        print(f"2 число {USER_NUM_2} является средним")
    elif USER_NUM_1 < USER_NUM_3 < USER_NUM_2 or USER_NUM_1 > USER_NUM_3 > USER_NUM_2:
        print(f"3 число {USER_NUM_3} является средним")
    else:
        print(
            f"Введены равные числа {USER_NUM_1:.2f}; {USER_NUM_2:.2f} и {USER_NUM_3:.2f}")
except ValueError as exception:
    print(f"Введены некорректные данные. Вводите только числа!\n"
          f"{exception}")
