numero = int(input('Digite um numero: '))
total = 0
for c in range(1, numero + 1 ):
    if numero % c == 0:
        print('\033[31m', end=' ')#VERMELHO
        total += 1
       
    else:   
        print('\033[36m', end=' ')  #AZUL
    print(f'{c}', end=' ')  
print(f'\n \033[m O numero {numero} foi divisivel {total} vezes')

if total == 2 :
    print ('E por isso ele e primo!')
else:
    print ( 'e por isso não é Primo!')  