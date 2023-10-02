nn = list()

while True :
    valores = int(input('DIGITE SEU VALOR: '))
    print('VALOR ADD COM SUCESSO.... ')
    if valores not in nn:
        nn.append(valores)
    
    continuar =  str(input('Quer continuar? [S/N] ')).strip()[0]
    
    if continuar in 'Nn':
        break
    
print(f'--'*30)
print(f'os valoresdigitados foram {nn}')

print(f'--'*30)
print ('FIM...')