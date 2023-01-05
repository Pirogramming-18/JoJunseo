class NotInRange(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

num=0
player = 'A'

while True:
    while True:
        try:
            count = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
            if(not(1<=count<=3)):
                raise NotInRange
        except ValueError:
            print('정수를 입력하세요')
        except NotInRange as e:
            print(e)
        else:
            break

    while count>0:
        num += 1
        if num>31 :
            break
        print('player{0} : {1}'.format(player,num))
        count -= 1

    print()

    if player == 'A':
        player = 'B'
    else :
        player = 'A'

    if num>31:
        break

print('player{0} win!'.format(player))


