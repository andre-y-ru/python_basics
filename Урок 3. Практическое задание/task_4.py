"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

"""
Выполенине! Емельяненко А.А.
"""


def my_fun(x, y):
    return 1 / x ** abs(y)


def my_fun_use():
    print(my_fun(2, -2))


def my_fun_2(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x


def my_fun_2_use():
    print(my_fun_2(2, -2))


print(f'Возведения степени вариантом 1: '
      f'{my_fun(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')

print(f'Возведения степени вариантом 2: '
      f'{my_fun_2(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')
