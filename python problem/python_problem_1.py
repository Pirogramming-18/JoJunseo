class NotInRange(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

num=0

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
    print('playerA : {0}'.format(num))
    count -= 1

