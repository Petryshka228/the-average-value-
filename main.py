while True:

    def get_average_value():
        result = []
        a = (input('Перечислите числа через пробел: ')).split()
        for i in a:
            if i.isnumeric():
                result.append(i)
        if len(result) != 0:
            itog = list(map(int, result))
        return round(sum(itog) / len(result), 2)


    print('Среднее значение равно: ', get_average_value(), '\n', '\n', 'Для продолжения нажмите "Enter"')
    input()
