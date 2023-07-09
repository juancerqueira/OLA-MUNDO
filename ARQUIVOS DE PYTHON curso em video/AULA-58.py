from random import randint
computador = randint(0, 11)
acertou = False
cont = 0
print(''' Sou seu computador ...Acabei de pensar em um numero entre 0 e 10, sera que voce consegue adivinhar qual foi ? ''')
while not acertou:

  
    #FAZ O COMPUTADOR SORTEAR UM NUMERO
    jogador = int(input('Escolhar um numero de 0 a 10: '))
    if jogador == computador:
        acertou = True
        print('-=-'*20)
        print('Parabéns, você acertou') 
        print('-=-'*20)
        print ('--FIM--')
    else:
        cont += 1 
        print('-=-'*20)
        print('VOCE ERROU TENTE DE NOVO ')
        print('-=-'*20) 
        if jogador < computador:
            print('Mais...Tente Novamente.')
        elif jogador > computador:
            print('Menos.. Tente Novamente.')

print(f'Acertou com {cont} tentativas Parabens ')