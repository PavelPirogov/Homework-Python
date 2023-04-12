# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество 
# монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2

import random

n = int(input('Количество монеток: '))
arr = []

for i in range(n):
    arr.append(random.randint(0, 1))

print(arr)

eagle = 0
tails = 0

for i in arr:
    if i == 0:
        eagle += 1
    elif i == 1:
        tails += 1    

if eagle > tails:
    print(n - eagle)
else:
    print(n - tails)
