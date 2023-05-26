'''import random
numero = [0,1,2,3,4,5]
escolhido = random.choice(numero)

seunumero = int(input('Digite um numero de 0 a 5: '))
if seunumero == escolhido:
    print('Parabéns, você acertou')
    print ('--FIM--')  
else:
     print(f'veu ganhei o numero que pensei foi {escolhido}.')   '''


from random import randint
computador = randint(0, 5)  
 #FAZ O COMPUTADOR SORTEAR UM NUMERO
jogador = int(input('Escolar um numero de 0 a 5: '))
if jogador == computador:
    print('-=-'*20)
    print('Parabéns, você acertou') 
    print('-=-'*20)
    print ('--FIM--')
else:
    print('-=-'*20)
    print('GAME OVER')
    print('-=-'*20) 