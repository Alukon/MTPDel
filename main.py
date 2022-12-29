import random
from random import randrange

print('    Чтобы получить результат решений,\nв конце, вместо ответа [ Q ] потом на [Ё] далее на [ENTER]')
print('    Записывай ответ потом на [ENTER]')

result_loose = ['    Sorry,', '    Упс:(,', '    Подумай,', '    Соберись,', '    Не сдавайся,', '    Запомни,']
score = [0, 0]

while 1:
    mult_devid = randrange(0, 2)
    if mult_devid == 0: # умножение
        x = randrange(2, 10)
        y = randrange(2, 10)
        answr = input('         {} x {} = '.format(x, y))

        if answr == str(x * y):
            score[0] += 1

        elif answr == 'q' or answr == 'Q' or answr == 'й' or answr == 'Й':
            num = sum(score)
            print('    Всего было {} примеров\n    Правильных ответов: {}%'.format(num, int(score[0] / num * 100)) if num else '')

        elif answr == 'ё' or answr == 'Ё' or answr == '`' or answr == '~':
            quit()

        else:
            rl = random.choice(result_loose)
            print(rl, 'правильный ответ {}'.format(x * y))
            score[1] += 1
    if mult_devid == 1: # деление
        x = randrange(2, 10)
        y = randrange(2, 10)
        z = x * y
        answr = input('         {} : {} = '.format(z, y))

        if answr == str(z // y):
            score[0] += 1

        elif answr == 'q' or answr == 'Q' or answr == 'й' or answr == 'Й':
            num = sum(score)
            print(
                '    Всего было {} примеров\n    Правильных ответов: {}%'.format(num, int(score[0] / num * 100)) if num else '')

        elif answr == 'ё' or answr == 'Ё' or answr == '`' or answr == '~':
            quit()

        else:
            rl = random.choice(result_loose)
            print(rl, 'правильный ответ {}'.format(z // y))
            score[1] += 1