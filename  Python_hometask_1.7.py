# Задание 1

'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).

'''

import random

def bubble_sort3(orig_list):
    n = 1
    f = True #вводим переменную флаг
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] > orig_list[i+1]:
                f = False #меняем флаг и выполняем условия
                orig_list[i],orig_list[i+1] = orig_list[i+1],orig_list[i]
            if f: #если все ок, ничего не делаем
                break
        n += 1
    return orig_list

# массив
dd1 = [random.randint(-100, 100) for _ in range(100)]

print(f'оригинальный массив {dd1}\nотсортированный массив {bubble_sort3(dd1)}')
#Задание 2

'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.

'''

def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list

# замеры
d1 = [random.uniform(0, 50) for _ in range(500)]


print(f'оригинальный массив {d1}\nотсортированный массив {merge_sort(d1)}')


#Задание 3
'''
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется
элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках.
'''


m = int(input('введите натуральное число '))
rm = [random.randint(0,100) for _ in range(2*m+1)]

'''
Сортировка подсчетом – один из базовых алгоритмов, служит основой для многих сортировок, но сам используется только для
ознакомления с темой. Его суть в том, чтобы подсчитать сколько раз число встречается в массиве,
а затем заполнить массив этими числами в соответствии с количеством.

'''


def countingsort(aList, k):
    counter = [0] * (k + 1)
    for i in aList:
        counter[i] += 1

    b = 0
    for i in range(len(counter)):
        while 0 < counter[i]:
            aList[b] = i
            b += 1
            counter[i] -= 1
    d = len(aList) // 2
    return aList, aList[d]

print (countingsort(rm, max(rm)))
