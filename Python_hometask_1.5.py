import numpy as np

'''
Задание 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
предприятий, чья прибыль ниже среднего.

'''

fin =  collections.namedtuple('finance','profit average') # Создаем шаблон
d = {} #складываем в словарь все данные
list_average = []
for i in range(4):
    name = input ("Введите название компании: ")
    profit_4 = [int(x) for x in input ("Введите данные о прибыли 4-е квартала через пробел: ").split()]
    fin_parts = fin ( #создаем экземпляр шаблона
                profit = profit_4,
                average = np.mean(profit_4))
    d[name] = fin_parts
    list_average.append(fin_parts.average)

total_av = np.mean(list_average) # общее среднее

for i, k in d.items():
    if k[1] > total_av:
        print ('Прибыль в размере {} выше среднего значения {} у компании {}'.format(k[1],total_av, i))
    else:
        print ('Прибыль в размере {} ниже среднего значения {} у компании {}'.format(k[1], total_av, i))

'''

Задание 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

Число, которое соответствует десятичному 16 — первое, которое нельзя записать одной цифрой. Проиллюстрируем это рядами чисел:
Таблица 1. Соответствие десятичных чисел шестнадцатеричным

Десятичные	       0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16
Шестнадцатеричные	0	1	2	3	4	5	6	7	8	9	a	b	c	d	e	f	10

'''

# Шаг 1 Ввод и обаботка данных

dd = input ("Введите 2 шестнадцатеричных числа через пробел: ").split()

# передаем данные в список списков
ff = []
for i in dd:
    b= [x for x in i]
    ff.append(b)
print (ff)

#Разделяем полученные аргументы на первый и второй, переводим их в обратный порядок расчета
first = ff[0][::-1]
second = ff[1][::-1]

dl1=len(first)
dl2=len(second)

#Делаем одинаковую длину списку у всех аргументов и добавляем 0
if dl1 > dl2:
    dif1 = dl1 - dl2
    for i in range (dif1):
        second.append('0')

elif dl1 < dl2:
    dif2 =  dl2 - dl1
    for k in range (dif2):
        first.append('0')

# Шаг 2. Создаем словарь ключа и значений 16-ти значной системы

index_list= ["0","1","2","3", "4", "5", "6", "7","8","9","A","B","C","D", "E", "F", "10"]
value_list = [x for x in range(17)]
s ={}
for i in range(17):
    s[index_list[i]] = i

#Шаг 3. Функция сложения 2-х 16-ти значных чисел

def sum16(first, second, s):

    result = []
    plus_one = collections.deque([0]) #сколько держим в уме целых чисел для прибавления, когда больше 16

    for i in range (len(first)):
        t1 = first[i]
        t2 = second[i]
        g = s[t1] + s[t2] + plus_one[0] #добавляем сколько держали в уме, если было больше 16 в предыдущем цикле
        plus_one.appendleft(0) #добавляем ноль, чтобы в следующий раз не добавлять единицу

        if g in s.values():
            h1 = [*s][g]  # [*s] распаковываем словарь по ключам, как список
            result.append(h1)

        elif g > 16:
            d = g // 16
            d1 = g - d*16
            plus_one.appendleft(d)
            h2 = [*s][d1]
            result.append(h2)
    return (result[::-1])

print (sum16(first, second, s)) # Результат сложения

# Шаг 4. Умножение  ['2', 'A', '0']  * ['F', '4', 'C'] = [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

result1 = collections.defaultdict(list)
plus_one1 = collections.deque([0])

#умножаем сначала каждую цифру из меньшего списка на больший по количество список цифр и записываем результат

for i in range (len(first)):
    t1 = first[i] # надо сначала пройтись по одному

    for k in range (len(second)):
        t2 = second[k] # проходимся по всем
        g = s[t1] * s[t2] + plus_one1[0]
        plus_one1.appendleft(0) #добаялем ноль, чтобы в следующий раз не добавлять единицу

        if g in s.values():
            # [*s] распаковываем словарь по ключам как список
            h1 = [*s][g] #и добавляем единицу, если было больше 16 в предыдущем цикле и удаляем ее из списка
            result1[i].append(h1)

        elif g > 16:
            d = g // 16
            d1 = g - d*16
            plus_one1.appendleft(d)
            h2 = [*s][d1]
            result1[i].append(h2)

        # если цикл закончился, а у нас есть в уме единица, записываем ее в результат и потом добавляем 0,
        #чтобы это не повлияло на след цикл

        if len(result1[i]) == len(second):
            result1[i].append(str(plus_one1[0]))
            plus_one1.appendleft(0)

print (result1[0], result1[1])

#Шаг5. Складываем полученные списки с учетом сдвига влево, начиная со второго
#для этого добавляем 0 в начало первого аргумента и в конец второго

arg1 = collections.deque(result1[0][::-1])
arg2 = collections.deque(result1[1][::-1])
arg1.appendleft(str(0))
arg2.append(str(0))

# Шаг 6. финальный шаг - складываем два числа, которые получили при умножении
print (sum16(arg1,arg2, s)[::-1])
