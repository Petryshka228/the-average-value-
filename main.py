print('Все права защищены')
i = 1
while i != 0:
    b2 = 0
    b3 = 0
    b4 = 0
    b5 = 0
    er = 0
    a = str(input('Перечислите оценки: ')).split()
    for i in a:
        if i == '2':
            b2 += 1
        elif i == '3':
            b3 += 1
        elif i == '4':
            b4 += 1
        elif i == '5':
            b5 += 1
        else:
            er += 1
    if er == 0:
        kol = b2 + b3 + b4 + b5
        b2 *= 2
        b3 *= 3
        b4 *= 4
        b5 *= 5
        sr = round(((b2 + b3 + b4 + b5) / kol), 2)
        print('Средний балл равен: ', sr)
        print('Для продолжения нажмите "Enter"')
    else:
        print('Ошибка, введите корректные данные')
        print('Для продолжения нажмите "Enter"')
    input()

