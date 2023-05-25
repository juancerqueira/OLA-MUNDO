import random
numero = [0,1,2,3,4,5]
escolhido = random.choice(numero)

seunumero = int(input('Digite um numero de 0 a 5: '))
if seunumero == escolhido:
    print('Parabéns, você acertou')
else:
     print(f'voce errou, o numero escolhido foi {escolhido}.')    