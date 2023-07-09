
'''r = 'S'
while r in 'Ss':
    n = int(input('Digite: '))
    r = str(input('Que continuar [S/N]:'))

print('SIM')'''
n = 1
par = 0 
impar =  0
while n != 0:
    n = int(input('Digite seu valor: ')) 
    if n != 0:
        if n % 2 == 0:
            print('Esse numero e par')
            par = par + 1
        if n % 2 == 1 :
            print('Esse numero e impar')
            impar +=1
print(f'voce digitou {par} numero pares e {impar} numeros impares')