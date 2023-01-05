class NotInRange(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

num=0

while True:
    try:
        countA = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
        if(not(1<=countA<=3)):
            raise NotInRange
    except ValueError:
        print('정수를 입력하세요')
    except NotInRange as e:
        print(e)
    else:
        break

while countA>0:
    num += 1
    print('playerA : {0}'.format(num))
    countA -= 1



while True:
    try:
        countB = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
        if(not(1<=countB<=3)):
            raise NotInRange
    except ValueError:
        print('정수를 입력하세요')
    except NotInRange as e:
        print(e)
    else:
        break

while countB>0:
    num += 1
    print('playerB : {0}'.format(num))
    countB -= 1

