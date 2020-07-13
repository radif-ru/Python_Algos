"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
try:
    LENGTH_CUT_1 = int(input("Введите длину отрезка №1: "))
    LENGTH_CUT_2 = int(input("Введите длину отрезка №2: "))
    LENGTH_CUT_3 = int(input("Введите длину отрезка №3: "))

    if LENGTH_CUT_1 > 0 and LENGTH_CUT_2 > 0 and LENGTH_CUT_3 > 0:
        if LENGTH_CUT_1 == LENGTH_CUT_2 == LENGTH_CUT_3:
            print("Треугольник является равносторонним")
        elif LENGTH_CUT_1 != LENGTH_CUT_2 != LENGTH_CUT_3 and LENGTH_CUT_1 != LENGTH_CUT_3:
            print("Треугольник является разносторонним")
        else:
            print("Треугольник является равобедренным")
    else:
        print("Три отрезка должны быть больше 0! Иначе это не может быть треугольником")
except ValueError as exception:
    print(f"Вы ввели екорректные данные. Вводить нужно только числа!\n"
          f"{exception}")
