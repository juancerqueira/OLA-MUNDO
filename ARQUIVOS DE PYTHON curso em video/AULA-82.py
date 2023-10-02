lista = []
par = []
impar = []
numero = 0
todos = []
while True :

    numero = int(input('Digite seu numero: '))
    todos.append(numero)

    lista.append(numero)
    if numero % 2 == 0 :
        par.append(numero)
    elif numero % 2 == 1 : 
        impar.append(numero)
    continuar = str(input('Quer continuar ?[S/N] ')).strip()[0].upper()
    if continuar in 'Nn':
        break

print(f' Todos os numero {todos} ')
print(f'Os numeros de impar {impar} ')
print(f'Os numeros de par {par} ')

print ('FIM...')