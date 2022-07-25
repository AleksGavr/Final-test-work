import random
import string
from random import randint


def cls():
    print("\n" * 100)


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


cls()
print('Задача: Написать программу. которая из имеющегося массива строк формирует массив из строк, длина которых\n '
      'меньше либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры, либо задать на старте\n '
      'выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями, лучше обойтись\n исключительно '
      'массивами. ')
print('\n' * 4)
m = get_quantity_rows()
print('\n')
Array = []
NewArray = []
lim = 3
i = 0
while i < m:
    n = randint(2, 5)
    Array.append(generate_alphanum_random_string(n))
    i += 1
print(f'Случайный массив: {Array}')
print('\n')
i = 0
while i < m:
    if len(Array[i]) <= lim:
        NewArray.append(Array[i])
    i = i + 1
print(f'Новый массив соответствующий условиям задачи: {NewArray}')
