nn = list()
simNao = ''

while True :
    valores = int(input('DIGITE SEU VALOR: '))
    print('VALOR ADD COM SUCESSO.... ')
    if valores not in nn:
        nn.append(valores)
    
    continuar =  str(input('Quer continuar? [S/N] ')).strip()[0]
    nn.sort(reverse=True)
    if continuar in 'Nn':
    
        break
    
    while True:
        if 5 in nn :
            simNao = 'Sim'
            break
        if 5 not in nn :
            simNao = "Não"
            break

    
print(f'--'*30)
print(f'os valoresdigitados foram {nn}')

print(f'O valor 5 foi digitado ? {simNao}')
print(f'--'*30)
print ('FIM...')