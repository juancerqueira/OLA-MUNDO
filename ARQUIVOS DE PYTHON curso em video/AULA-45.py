from random import randint  
from time import sleep

for c in range(0, 3):

    itens = ('Pedra' , 'Papel' , 'Tesoura')
    computador = randint(0,2)
    print('-='*11)
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input('Qual e a sua jogada ? '))
    print(' JO')
    sleep(1)
    print('KEN')
    sleep(0.5)
    print('PO!!!')

    print('-='*11)
    print('O COMPUTADOR jogou {}'.format(itens[computador]))
    print('O JOGADOR jogou {}'.format(itens[jogador]))
    print('-='*11)
    if computador == 0: #PC JOGOU PEDRA
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2: 
            print('COMPUTADOR GANHOU')
        else:
            print('OPÇÃO INVALIDA')

    elif computador == 1: # PC JOGOU PAPEL
        if jogador == 0:
            print('COMPUTADOR GANHOU')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR GANHOU')
        else:
            print('OPÇÃO INVALIDA')
    elif computador == 2: # PC JOGOU TESOURA    
        if jogador == 0 :
            print ('JOGADOR GANHOU')

        elif jogador == 1 :
            print('COMPUTADOR GANHOU')
                
        elif jogador == 2 :
            print('EMPATE')
        else:
            print('OPÇÃO INVALIDA')

    
            











'''print(f'O computador escolheu {itens[computador]}')'''