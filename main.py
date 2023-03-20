import numbers

print('Все права защищены')

while True:
    result = []
    a = (input('Перечислите числа через пробел: ')).split()
    for i in a:
        try:
            if isinstance(int(i), numbers.Number) == True:
                result.append(i)
            else:
                print(1)
        except:
            er = i
    if len(result) != 0:
        itog = list(map(int, result))
        sr = round(sum(itog) / len(result), 2)
        print('Среднее значение равно: ', sr, '\n', '\n', 'Для продолжения нажмите "Enter"')
    input()
