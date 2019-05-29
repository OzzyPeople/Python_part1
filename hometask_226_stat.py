
''' Задача 1

1.1 Найдите ковариацию этих двух величин: сначала без использования специальных функций, а затем с помощью функции numpy.cov.
Полученные значения должны быть равны.


'''

# Оценим сначала визуально зависимость

matplotlib.style.use('ggplot')
plt.scatter(x, y)
plt.show()

# Считаем к-т ковариации и корреляции без формул

l = len(x)
c = 0
dx = 0 # дисперсия x до вычисления корня
dy = 0 # исперсия y до вычисления корня
for i in range(l):
    f = (x[i] - sum(x)/len(x))*(y[i] - sum(y)/len(y))
    c = c + f
    d_x = (x[i] - sum(x)/len(x))**2/(l-1)
    d_y = (y[i] - sum(y)/len(y))**2/(l-1)
    dx = dx + d_x
    dy = dy + d_y
cov = c/(l-1)
cor = cov/(np.sqrt(dx)*np.sqrt(dy))
print (f'к-т ковариации {cov}, к-т Пирсона корреляции {cor}')

# Считаем к-т ковариации используя numpy

X = np.stack((x, y), axis=0)
print(f'к-т ковариации {np.cov(X)[1][0]} к-т Пирсона корреляции {np.corrcoef(x, y)[1][0]}')

'''
Задача 2

Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
131, 125, 115, 122, 131, 115, 107, 99, 125, 111

Известно, что в генеральной совокупности IQ распределен нормально.
Найдите доверительный интервал для математического ожидания с надежностью 0.95.

'''

xiq = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
l1 = len(xiq ) #объем выборки
x_m = sum(xiq )/l1 # среднее значение
dx_iq = 0 #стандартное отклонение до вычисления корня

for i in range(l1):
    d_x = (xiq[i] - x_m )**2/(l1-1)
    dx_iq = dx_iq + d_x

#выборочное стандартное октлонение
se = np.sqrt(dx_iq)/np.sqrt(l1)

#доверительный интервал для математического ожидания с надежностью 0.95

right = round(x_m + 1.96* se,2)
left = round (x_m - 1.96* se,2)

print (f'доверительный интервал 0.95 находится в промежутке {left} - {right}')

'''
Задача 3

Известно, что рост футболистов в сборной распределен нормально с известной дисперсией 25.
На выборке объёма 27 выборочное среднее составило 174.2. Найдите доверительный интервал для математического ожидания с надежностью 0.95.

'''

d = 25 # дисперсия
n = 27  # объем выборки
x_m1 = 174.2 # выборочное среднее

#выборочное стандартное октлонение
se1 = d/np.sqrt(n)

#доверительный интервал для математического ожидания с надежностью 0.95
right1 = round(x_m1 + 1.96* se1,2)
left1 = round (x_m1 - 1.96* se1,2)

print (f'доверительный интервал 0.95 находится в промежутке {left1} - {right1}')
