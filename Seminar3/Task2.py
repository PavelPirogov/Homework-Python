# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к 
# заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


import random

n = int(input("Введите число элементов списка: "))
lst = []

for i in range(n):
    lst.append(random.randint(0, 30))

x = int(input('Введите искомое число: '))
nearest = abs(lst[0] - x)

for i in range(1, n):
    if abs(lst[i] - x) < nearest:
        # nearest = lst[i]   #  Как было в семинаре не работает. Почему мы в разницу записываем просто число из списка???
        nearest = abs(lst[i] - x)
        num = lst[i]

print(lst)
print(f'К числу {x} ближе всего {num}')




