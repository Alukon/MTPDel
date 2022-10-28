import random
from random import randrange

result_right = ['Светлая голова','Хвалю', 'Умничка', 'Молодчина', 'Умница-разумница','Браво','Белисимо']
result_loose = ['Sorry', 'Упс:(', 'Пардон', 'Не обессудь', 'Не прогневайся', 'Прости великодушно']
score = [0, 0]

while 1:
    mult_devid = randrange(0, 2)
    if mult_devid == 0: # умножение
        x = randrange(2, 10)
        y = randrange(2, 10)
        answr = input('{} x {} = '.format(x, y))
        while not answr.isdigit() and answr != 'exit':
            answr = input('Введите число!\n')

        if answr == str(x * y):
            rr = random.choice(result_right)
            print(rr)
            score[0] += 1

        elif answr == 'exit':
            num = sum(score)
            print('Всего было {} примеров\nПравильных ответов: {}%'.format(num, int(score[0] / num * 100)) if num else '')
            break

        else:
            rl = random.choice(result_loose)
            print(rl, 'правильный ответ {}'.format(x * y))
            score[1] += 1
    if mult_devid == 1: # деление
        x = randrange(2, 10)
        y = randrange(2, 10)
        z = x * y
        answr = input('{} : {} = '.format(z, y))
        while not answr.isdigit() and answr != 'exit':
            answr = input('Введите число!\n')

        if answr == str(z // y):
            rr = random.choice(result_right)
            print(rr)
            score[0] += 1

        elif answr == 'exit':
            num = sum(score)
            print(
                'Всего было {} примеров\nПравильных ответов: {}%'.format(num, int(score[0] / num * 100)) if num else '')
            break

        else:
            rl = random.choice(result_loose)
            print(rl, 'правильный ответ {}'.format(z // y))
            score[1] += 1