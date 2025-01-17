"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

"""
Выполенине! Емельяненко А.А.
"""


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'3


try_except = Error(1)
print(try_except.my_input())

#Альтернативное решение

class ControlType(Exception):
    pass


my_Hop = []
while True:
    try:
        value = input('Введите число в список, для выхода введите ?  :')
        if value == '?':
            break
        if not value.isdigit():
            raise ControlType(value)
        my_Hop.append(int(value))
    except ControlType as ex:
        print(f'{ex} - не число ?')
print(my_Hop)
