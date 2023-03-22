from random import randint

i1 = 0
i2 = 0
while i2 < 3:
    a = int(randint(0, 10))
    b = int(randint(0, 10))
    c = int((input(str(a) + ' + ' + str(b) + ' = ')))
    if c != a + b:
        i2 += 1
        print('Ответ неверный')
    else:
        i1 += 1
        print('Правильно!')
print('Игра окончена.\nПравильных ответов: ', i1)
