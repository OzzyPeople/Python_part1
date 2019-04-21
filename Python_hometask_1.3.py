'''
Задание 1

В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

'''


num_m = [x for x in range(2,100)] #массив для проверки
num_c = [x for x in range(2,10)] # список чисел, которые будет проверять на кратность
count_2 = 0
count_3 = 0

for i in num_m:
    for k in num_c:
        if i%2 == 0:
            count_2 +=1
        if  i%3==0:
            count_3 +=1


print ("Количество чисел, кратное 2 = {}".format (count_2))
print ("Количество чисел, кратное 3 = {}".format (count_3))


'''
Задание 2

Во втором массиве сохранить индексы четных элементов первого массива. Например,
если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.

'''

a = int(input ("Введите число - начало массива :"))
b = int(input ("Введите число - конец массива :"))
arr = [x for x in range(a,b+1)]
new_arr =[]

for i in arr:
    if i%2 == 0:
        b = arr.index(i)
        new_arr.append(b)

print (new_arr)

"""
Задание 3

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""
import numpy as np
g = input("введите возможное максимально число в наборе случайных чисел :")
b = np.random.randint(1, high = g, size=100) #создаем массив
max_ =  b.max()
min_= b.min()

print ("первоначальный массив", b)

dr_max = [] # список для индексов всех максимумов
dr_min = [] # список для индексов всех минимумов

for i, j in enumerate(b): #добавляем индекс в список
    if j == max_:
        dr_max.append(i)
    elif j== min_:
        dr_min.append(i)

for k in dr_max: #меняем все максимумы на минимумы
    b[k] = min_

for k in dr_min: #меняем все минимумы на максимумы
    b[k] = max_

print (b)

'''
Задание 4

Определить, какое число в массиве встречается чаще всего.

'''

g = input("введите возможное максимально число в наборе случайных чисел :")
b = np.random.randint(1, high = g, size=100)

f = {}
for i in b:
    x = list(b).count(i)
    f[i] = x
print ("число - количество повторов", f)

"""
Задание 5

В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве

"""

#Возьмем произвольный массив от - 11 до 12 и 100 значений
b = np.random.randint(-11, high = 12, size=100)
d = {}
for i, j in enumerate(b):
    if j < 0:
        d[i] = j

print (sorted(d.items())[0])


# Вариант 2 по комментариям преподователя без функции sorted

#Возьмем произвольный массив от - 11 до 12 и 100 значений
b = np.random.randint(-11, high = 12, size=100)

for i in range(len(b)):
        minimum = i # задаем первое минимальное значение
        for j in range(i + 1, len(b)):
            if b[j] < b[minimum]: # если находим меньшее значение
                minimum = j
        b[minimum], b[i] = b[i], b[minimum] # размещаем минимальное значение впереди значения, которое больше
print (b)

'''
Задание 6

В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

import random

N = 12
b = [random.randint(1, 100) for _ in range(N)]

for i, j in enumerate(b):

    if j == max(b):
        ma_p, ma_v = i, j
    if j == min(b):
        mi_p, mi_v = i, j

print ('позиция минимума {}, значение = {}'.format(mi_p, mi_v))
print ('позиция максимума {}, значение = {}'.format(ma_p, ma_v))


if  ma_p > mi_p :
    print ("Сумма значений между минимумом и максимумом = ", sum(b[mi_p+1: ma_p]))
else:
    print ("Сумма значенений между максимумом и минимумом = ", sum(b[ma_p+1: mi_p]))

'''
Задание 7

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

'''

N = 12
b = [random.randint(1, 100) for _ in range(N)]

a = sorted(b)

f,k =  a[0:2]

if f == k:
    print ("Два последние числа равны = {}".format (f))

else:
    print ("Два наименьших элемента = {}, {}".format (f, k))

'''
Задание 8

Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять
сумму введенных элементов каждой строки  и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

'''

n1 = [int(x) for x in input("1-я стока. Введите последовательность 3-х чисел через пробел: ").split()]
n2 = [int(x) for x in input("2-я стока. Введите последовательность 3-х чисел через пробел: ").split()]
n3 = [int(x) for x in input("3-я стока. Введите последовательность 3-х чисел через пробел:").split()]
n4 = [int(x) for x in input("4-я стока. Введите последовательность 3-х чисел через пробел: ").split()]
n5 = [int(x) for x in input("5-я стока. Введите последовательность 3-х чисел через пробел: ").split()]

n1.append(sum(n1))
n2.append(sum(n2))
n3.append(sum(n3))
n4.append(sum(n4))
n5.append(sum(n5))

n_total = [n1, n2, n3, n4, n5]

matrix = np.array(n_total)
print (matrix)

 '''
 Задание 9

Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Есть столбцы матрицы, каждый столбец содержит минимальное число, например для матрицы 3 × 5 будет 5 таких чисел,
среди этих 5 чисел нужно найти максимальное

Матрица [[1, 2], [3, 4]] у неё столбцы 1, 3 и 2, 4. В первом столбце минимальный элемент 1, во втором 2.
Максимальный элемент между 1 и 2 это 2. Ответ: 2

 '''

 x = np.random.randint(16, size=(3,5)).astype('uint8')
l_min = []
for i in x.T:
    b = i.min()
    l_min.append(b)

print (x)
print (max(l_min))
