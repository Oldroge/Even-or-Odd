from random import randint
print('{:=^40}'.format(' PAR OU ÍMPAR '))
r = num = computador = 0
vitorias = 0
while True:
    computador = randint(1, 10)
    jogador = str(input('VOCÊ ESCOLHE ÍMPAR OU PAR [I/P]: ')).upper().strip()[0]
    if jogador == 'P':
        num = int(input('Escolha um número de 1 à 10: '))
        if computador % num == 0:
            print(f'O computador jogou {computador} e você jogou {num}, deu PAR! VOCÊ VENCEU!!')
            vitorias += 1
        else:
            print(f'O computador jogou {computador} e você jogou {num}, deu ÍMPAR! perdeu :(')
            if vitorias < 2 > 0:
                print(f'Você teve {vitorias} vitória!')
            else:
                print(f'Você teve {vitorias} vitórias!')
            break
    elif jogador == 'I':
        num = int(input('Escolha um número de 1 à 10: '))
        if computador % num == 0:
            print(f'O computador jogou {computador} e você jogou {num}, deu PAR! perdeu :(')
            if vitorias < 2 > 0:
                print(f'Você teve {vitorias} vitória!')
            else:
                print(f'Você teve {vitorias} vitórias.')
            break
        else:
            print(f'O computador jogou {computador} e você jogou {num}, deu ÍMPAR! VOCÊ VENCEU!!!')
            vitorias += 1
    else:
        print('Jogada inválida!')
