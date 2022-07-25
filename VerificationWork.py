import random
import string
from random import randint


def cls():
    print("/n" * 100)


def get_quantity_rows():
    while True:
        try:
            num = int(input("Введите количество строк из которых будет состоять массив: "))
            return num
        except ValueError:
            print("Вы ввели нецелочисленное значение. Повторите ввод")


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


m = get_quantity_rows()

Array = []
NewArray = []
lim = 3
i = 0
while i < m:
    n = randint(2, 5)
    Array.append(generate_alphanum_random_string(n))
    i += 1
print(f'Случайный массив: {Array}')

i = 0
while i < m:
    if len(Array[i]) <= lim:
        NewArray.append(Array[i])
    i = i + 1
print(f'Новый массив соответствующий условиям задачи: {NewArray}')
