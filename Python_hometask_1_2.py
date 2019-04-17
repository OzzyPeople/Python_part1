'''
№1

Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.

Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


Ограничения:

Постарайтесь решить задачи без использования массивов. Им будет посвящён следующий урок.

'''

import operator

list_operators = {
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}

def calculator (a, b, z):
    a =  int(input("Введите первое число: "))
    b =  int(input("Введите второе число: "))

    if b == 0:
        print ("Ошибка ввода, нельзя делить на 0 ")
        b =  int(input("Введите второе число: "))

    z = input("Введите знак умножения *, деления / или вычитания :")

    while z !='0' and z not in list_operators :
        print ("Ошибка ввода")
        z = input("Введите знак умножения *, деления / или вычитания :")

    if z == '0': # Пишем базовый случай рекурсии
        print ('Конец игры')
    else: # Рекурсивное условие
        print (list_operators[z](a,b))
        return (str(calculator (a, b, z)))
print (calculator (a, b, z))

'''
2

Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

'''

a =  input("Введите число: ")
chet = []
nechet = []
for i in a:
    if int(i)%2 ==0:
        chet.append(i)
    else:
        nechet.append(i)
print (*chet)
print (*nechet)

'''
3

Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.

'''
n=int(input("Введите число: "))
rev_n =0
while(n>0): # циклим пока n не будет равен 0
    dig=n%10 # делим на 10 и получаем остаток после запятой
    rev_n=rev_n*10+dig # складываем его в rev
    n=n//10 # сокращаем n на десяток
print("Обратное число:",rev_n)

'''
4
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
'''

n=int(input("Введите количество элементов: "))
num = [1, (-0.5), 0.25, (-0.125)]
sum_l = []
for i in num[:n]:
    sum_l.append(i)
print (sum(sum_l))

'''
5

Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

'''

import pandas as pd
from tabulate import tabulate

l_n = []
kl={}
for i in range(32, 128):
    par = i, chr(i)
    l_n.append(par)
b=1
n=10
j=0

for i in l_n:
    if len(kl) < len(l_n)/10:
     # это индекс списка или самое значение ?
        kl[b]=l_n[j:n]
        b+=1 #номер пары
        j+=10 #старт отсчета пары
        n+=10 #конец отсчета пары
print (tabulate(kl,["code-symbol"], tablefmt="plain")) #showindex="always"

'''
Задание 6

В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.

'''

import random
p = random.randint(1,101)
print (p)

def guess(k): # k - это количество попыток, в базовом варианте = 0

    n=int(input("Введите число от 0 до 100: "))
    i = 1+k

    # Пишем базовый случай рекурсии
    if i ==10:
        print ("Загаданное число = ", p)

    if n==p:
            print ("Вы угадали!")

    # Рекурсивное условие

    while i !=10 and n!=p:

        if n >p:
            print ("Ваше число больше")
            return (str(guess(k+1)))
        if n <p:
            print ("Ваше число меньше")
            return (str(guess(k+1)))

'''
Задание 7

Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

'''

n1=int(input("Введите первое натуральное число множества: "))
n_u=int(input("Введите последнее натуральное число множества: "))

i=0

for k in range(n1, n_u+1):
    i+=k
c = (n_u*(n_u+1))/2
if i == c:
    print ('равенство выполняется', i, " = ", c)

else:
    print ('нет')

'''
Задание 8

Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

'''

n = [int(x) for x in input("Введите последовательность чисел через пробел: ").split()]
n1=int(input("Введите число, которое необходимо подсчитать: "))

i_count = 0
for i in n:
    if i==n1:
        i_count+=1
print (i_count)

 '''
 Задание 9

 Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
 Вывести на экран это число и сумму его цифр.

 '''

 n = [x for x in input("Введите последовательность натуральных через пробел: ").split()]

c = {}
for i in n:
    one_sum = 0
    for k in i:
        one_sum +=int(k)
    c.setdefault(i, one_sum)
print (sorted(c.items(), reverse = True, key = lambda t: t[0])[0] ) #выводим первую пару из отросортированного по убыванию словаря (уже tuple)
