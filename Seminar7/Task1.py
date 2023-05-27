# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# Ввод:                                                 Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам                Парам пам-пам


str = 'пара-ра-рам рам-пам-папам па-ра-па-дам ывкоуопм вппавп-авпа-вап ывв-ааав'

lst = list(map(lambda x: x, str.split(" ")))

vow = []
for i in lst:
    count = 0
    for j in i:
        if j in 'аеёиоуыэюя':
            count += 1
    vow.append(count)

if len(vow) == vow.count(vow[0]):
    print('Парам пам-пам')
else:
    print('Пам парам')




# def rhythm(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum_w = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum_w += 1
#         list_1.append(sum_w)
#     print(list_1)
#     return len(list_1) == list_1.count(list_1[0])

# str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# if rhythm(str_1):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')




# c = 'пара-ра-рам рам-пам-папам па-ра-па-дам ывкоуопм вапаВп-авпа-вап ывв-ааав'
# st = c.lower().split()
# f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
# if all([f(i) == f(st[0]) for i in st]):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


