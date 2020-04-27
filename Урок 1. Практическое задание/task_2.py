"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

NUM_1 = 5
NUM_2 = 6

print(
    f"Побитовые операции над числами {NUM_1} и {NUM_2} \n\n"
    f"Побитовое или: {NUM_1 | NUM_2} \n"
    f"Побитовое исключающее или: {NUM_1 ^ NUM_2} \n"
    f"Побитовое и: {NUM_1 & NUM_2} \n"
    f"Битовый сдвиг влево числа {NUM_1} на 2 знака: {NUM_1 << 2} \n"
    f"Битовый сдвиг вправо числа {NUM_1} на 1 знака: {NUM_1 >> 1} \n"
    f"Инверсия битов: 5 = {~NUM_1}, 6 = {~NUM_2}")
