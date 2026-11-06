from random import randint
print('Добро пожаловать в тренажер таблицы умножения!')
while True:
    while True:
        try:
           level = int(input(
               'Выберете уровень сложности: \n'
               '. Легкий: 1\n'
               '. Средний: 2\n'
               '. Сложный: 3\n'
               'Введите номер уровня: '
           ))
           if level ==1:
               start = 1
               end = 10
               break
           elif level == 2:
               start = 10
               end = 20
               break
           elif level == 3:
               start = 20
               end = 30
           else:
               print('Введен неверный уровень!')
        except ValueError:
            print('Введите число!!')
    while True:
        try:
            kolvo_voprosov = int(input('Введите количество вопросов от 1 до 10: '))
            if 1 <= kolvo_voprosov <= 10:
                break
            else:
                print('Нужно ввести число от 1 до 10!!')
        except ValueError:
            print('Введите число!!')
    kolvo_corrects = 0
    kolvo_wrongs = 0
    for i in range(kolvo_voprosov):
        x = randint(start, end)
        y = randint(start, end)
        while True:
            try:
                otvet = int(input(f'Сколько будет {x} * {y}? '))
                break
            except ValueError:
                print('Введите число!!')
        if otvet == x * y:
            kolvo_corrects += 1
            print('Молодец! Правильно!')
        else:
            kolvo_wrongs += 1
            print(f'Неверно( Правильный ответ: {x * y}')
    points = (kolvo_corrects / kolvo_voprosov) * 100
    print(f'\nВаш резудьтат: {points:.2f}')
    print(f'Правильных ответов: {kolvo_corrects}')
    print(f'Ошибок: {kolvo_wrongs}')
    if points == 100:
        print('Умничка! Все правильно!')
    elif points >= 70:
        print('Хорошая работа!')
    else:
        print('Нужно потренироваться еще((')
    snova = input('Хотите ли вы пройти тест заново? (да/нет):').strip().lower()
    if snova != 'да':
        print('Спасибо за участие!!')
        break












