# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым билетом
# называют такой билет с шестизначным номером, где сумма первых
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 –
# счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

a = input('Введите шестизначное число: ')
sum1 = 0
sum2 = 0
size = len(a)

if size % 2 != 0:
    print('Число не чётное')
else:
    for i in range(int(size / 2)):
        sum1 += int(a[i])
        sum2 += int(a[(size - i - 1)])

    if sum1 == sum2:
        print('Билет счастливый')
    else:
        print('No')

    
    

    a = int(a)
    sum1 = 0
    sum2 = 0
    sizeConst = size

    while size > 0:
        if size > int(sizeConst / 2):  
            sum2 += a % 10
        else:
            sum1 += a % 10
        a //= 10
        size -= 1

    # print(sum1, sum2)

    if sum1 == sum2:
        print('Билет счастливый')
    else:
        print('No')


