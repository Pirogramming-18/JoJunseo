import random

class NotInRange(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

def brGame():
    num = 0
    player = 'computer'

    while True:
        if player == 'computer':
            count = random.randint(1,3)

        else:
            while True:
                try:
                    count = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
                    if (not (1 <= count <= 3)):
                        raise NotInRange
                except ValueError:
                    print('정수를 입력하세요')
                except NotInRange as e:
                    print(e)
                else:
                    break

        while count > 0:
            num += 1
            print('{0} : {1}'.format(player, num))
            if num == 31:
                break
            count -= 1

        if player == 'computer':
            player = 'player'
        else:
            player = 'computer'

        if num == 31:
            break

    print('{0} win!'.format(player))



brGame()
