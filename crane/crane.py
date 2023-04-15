number = int(input("Введите число журавликов"))
if not number % 6:
    x = number // 6
    print (f'Катя сделала{x*4}',f'Петя сделал{x}',f'Миша сделал{x}')
