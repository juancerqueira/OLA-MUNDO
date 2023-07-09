from datetime import date
atual = date.today().year
totalmaior = 0 #contar a condição
totalmenor = 0 #Contar a condição
for c in range( 1 , 3):
    nasc = int(input(f'Digite o {c} ano de nascimentos:'))
    idade = atual - nasc
    if idade >= 21 :
        print(' Essa pessoa e maior de idade')
        totalmaior += 1 
    
    else: 
        print('Essa pessoa e menor')
        totalmenor += 1


print(f'O numero de maiores de idade foi de {totalmaior} e o numero de menor de idade foi {totalmenor}')