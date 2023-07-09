sexo = str(input('DIGITE SEU SEXO [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = input('OPÇÃO INVÁLIDA! DIGITE M OU F:').strip().upper()[0]
print('FIM..')