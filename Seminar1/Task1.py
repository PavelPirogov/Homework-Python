# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 


a = input('Введите трёхзначное число: ')
sum = 0

for i in range(len(a)):
    sum += int(a[i])

print(sum)




a = int(a)
sum2 = 0

while a > 0:
    sum2 += a % 10
    a //= 10

print(sum2)
