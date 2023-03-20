import numbers


print('Все права защищены')

while True:
    result = []
    a = (input('Перечислите числа через пробел: ')).split()
    for i in a:
        if i.isnumeric() == True:
            result.append(i)
    if len(result) != 0:
        itog = list(map(int, result))
        sr = round(sum(itog) / len(result), 2)
        print('Среднее значение равно: ', sr, '\n', '\n', 'Для продолжения нажмите "Enter"')
    input()
