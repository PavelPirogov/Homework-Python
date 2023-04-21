# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
# выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

n = int(input('Введите количество кустов: '))
a = []
for i in range(n):
    a.append(randint(1, 9))

print('Кусты урожайностью', a)

max = a[0] + a[1] + a[-1]
max1 = a[0] + a[-1] + a[-2]
if max < max1: max = max1

for i in range(1, len(a) - 1):
    sum = a[i] + a[i - 1] + a[i + 1]
    if sum > max: max = sum

print(max)

