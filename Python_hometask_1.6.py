from memory_profiler import profile
import collections

num_first = 'A2'
num_second = 'C4F'


#Вариант 1. Тестируем алгоритм с уже встроенной функцией hex

class HexOperation:
    def __init__(self, num_first, num_second):
        self.num_first = num_first
        self.num_second = num_second

    @profile
    def __add__(self ,other):
        return list(hex(int(''.join(self.num_first), 16 ) +int(''.join(other.num_second), 16)))[2:]

    @profile
    def __mul__(self ,other):
        return list(hex(int(''.join(self.num_first), 16 ) *int(''.join(other.num_second), 16)))[2:]


#Вариант 2. Тестируем алгоритм без встроенной функции hex


# Шаг 1. Создаем словарь ключа и значений 16-ти значной системы

index_list= ["0","1","2","3", "4", "5", "6", "7","8","9","A","B","C","D", "E", "F", "10"]
value_list = [x for x in range(17)]
s ={}
for i in range(17):
    s[index_list[i]] = i

def inputd(num_first, num_second):

    # Переводим 16-е числа в обратный порядок расчета
    first = num_first[::-1]
    second = num_second[::-1]
    dl1 = len(first)
    dl2 = len(second)

    # Делаем одинаковую длину списков у всех аргументов и добавляем 0, где меньше
    if dl1 > dl2:
        dif1 = dl1 - dl2
        for i in range(dif1):
            second.append('0')

    elif dl1 < dl2:
        dif2 = dl2 - dl1
        for k in range(dif2):
            first.append('0')

    return (first, second)



#Функция сложения 2-х 16-ти значных чисел
@profile

def sum16 (s):

    both = inputd(list(num_first), list(num_second))
    first = both[0]
    second = both[1]

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



if __name__ == "__main__":
    print(f'Вариант 1 с функции hex{HexOperation(num_first, num_second) + HexOperation(num_first, num_second)}')
    print (f'Вариант 2 без функции hex {sum16(s)}')

'''
Резюме  - разница между первым и вторым вариантом составляет 2.6 MiB. По данным profile это происходит только за счет
самого профайлера. Сам алгоритм оценки памяти тяжелее для варианта 2, чем для 1-го. 
А так разница в коде неочевидна, кроме его длины :)
'''
