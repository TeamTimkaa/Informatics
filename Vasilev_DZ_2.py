#На СДО не даёт прикрепить более 1 файла. Задания отделил двумя пустыми строками. Васильев Тимур, 4931101/30002.


'''
1.Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран, 
сообщая об ошибке в случае деления на ноль.
'''
print('Введите числитель.')
a = float(input())
f = 0
while f < 1:
    print('Введите знаминатель.')
    b = float(input())
    if b == 0:
        print('Error: На ноль делить нельзя!')
    else:
        f += 10
print('Результат: ', a / b)


'''
Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю, если сумма покупки превышает 20 у.е. 
Сумму покупки ввести с клавиатуры, а результаты округлить до сотых (копейки, центы и т.д.). 
Вывести на экран итоговую стоимость и размер предоставленной скидки.
'''
from math import *
print('Введите стоимость покупки.')
s = float(input())
s2 = 0
s3 = 0
if s > 20:
    s2 = s - (s * 35 / 100)
    s3 = s * 35 / 100
else:
    s2 = s 
print('Итоговая стоимоть покупки: ' + str(round(s2, 2)), 'Размер предоставленной скидки: ' + str(round(s3, 2)), sep = '\n')


'''
Напишите скрипт, который по введенному пользователем числу от 1 до 12, будет выводить на экран сообщение в виде названия месяца и времени года. 
Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.
'''
print('Введите число от 1 до 12')
a = int(input())
f = 0
while f < 1:
    if 0 < a < 13:
        f += 10
    else:
        print('Error: Введите корректное число!')
        a = int(input())
s = ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
s2 = [''] + ['Зима'] * 2 + ['Весна'] * 3 + ['Лето'] * 3 +['Осень'] * 3 + ['Зима']
print('Месяц: ' + s[a], 'Время года: ' + s2[a], sep = '\n')