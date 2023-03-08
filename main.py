print('Все права защищены')
while True:
    a = list((input('Перечислите числа через пробел: ')).split())
    result = list(map(int, a))
    sr = round(sum(result) / len(a), 2)
    print('Среднее значение равно: ', sr, '\n', '\n', 'Для продолжения нажмите "Enter"')
    input()
