print('Все права защищены')
while True:
    a = (input('Перечислите числа через пробел: ')).split()
    list1 = []
    for i in a:
        list1.append(int(i))
    sr = round(sum(list1) / len(a), 2)
    print('Средний балл равен: ', sr, '\n', '\n', 'Для продолжения нажмите "Enter"')
    input()
