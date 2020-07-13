"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def even_odd_num(num, even=0, odd=0):
    """Количество чётных/нечётных чисел

    num - исходное число
    even - чётные числа
    odd - нечётные числа
    """
    if num:
        num_modulo = num % 10
        num //= 10
        if num_modulo % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_odd_num(num, even, odd)
    return even, odd


try:
    NUM = int(input("Введите число: "))
    if NUM < 0:
        raise ValueError("Число должно быть положительным!")
    print(
        f"Количество четных и нечетных цифр в числе равно: {even_odd_num(NUM)}")
except ValueError as exception:
    print(f"Вы ввели не натуральное число! Ошибка ввода данных: {exception}")
