from random import randint
v = 0
stop = 0
print('{:=^40}'.format(' EVEN OR ODD '))
while True:
    type = ' '
    while type not in 'EO':
        num = int(input('Choose a number between 0 and 10: '))
        if num > 10:
            break
        computer = randint(0, 10)
        total = computer + num
        type = str(input('MAKE YOUR CHOICE - EVEN OR ODD: ')).strip().upper()[0]
        print(f'You choose {num} and the computer choose {computer} the result is {total}')
        if type == 'E' or 'O':
            if type == 'E' and total % 2 == 0:
                print('YOU WIN!')
                v += 1
            elif type == 'O' and total % 2 > 0:
                print('YOU WIN!')
            else:
                stop = 1
                break
        else:
            print('Something is wrong... Try again!!')
    if stop:
        break
print(f'YOU LOOSE! You had {v} victories!')
