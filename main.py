print('Все права защищены')
while True:
    a = list((input('Перечислите оценки через пробел: ')).split())
    result = list(map(int, a))
    sr = round(sum(result) / len(a), 2)
    print('Средний балл равен: ', sr, '\n', '\n', 'Для продолжения нажмите "Enter"')
    input()
