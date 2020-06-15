"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Подсказка: используйте вложенный цикл

Пример:
В диапазоне 2-99: 49 чисел кратны 2
В диапазоне 2-99: 33 чисел кратны 3
В диапазоне 2-99: 24 чисел кратны 4
В диапазоне 2-99: 19 чисел кратны 5
В диапазоне 2-99: 16 чисел кратны 6
В диапазоне 2-99: 14 чисел кратны 7
В диапазоне 2-99: 12 чисел кратны 8
В диапазоне 2-99: 11 чисел кратны 9
"""


def num_of_multiples(multiples, before):
    """ Кратность чисел

    multiples - кратно этому числу
    before - максимальное значение диапазона, т.е. кратные от входного в ф-ю multiples до before
    """
    nums = [num for num in range(2, 100) if num % multiples == 0]
    print(f"В диапазоне 2-99: {len(nums)} чисел кратны {multiples}",
          f"Это числа: {nums}", sep="\n", end="\n\n")
    if multiples < 10:
        return num_of_multiples(multiples + 1, before)


num_of_multiples(2, 9)


# Так и не понял как тут избавиться при проверке в Pylint от?:
# task_1.py:19:0: R1710: Either all return statements in
# a function should return an expression, or none of them should. (inconsistent-return-statements)
