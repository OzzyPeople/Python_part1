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
