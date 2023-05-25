'''cadeia de caracteres'''


frase = str(input('DIGITE UMA FRASE: ')).strip() .upper()
print ('A LETRA A PARECE {} VEZES NA FRASE '.format(frase.count('A')))
print('A PRIMEIRO LETRA A APARECEU {}'.format(frase.find('A')+1 ),'CASA')
print('A ULTIMA LETRA APARECEU NA {}'.format(frase.rfind('A')+1),'CASA')

# FIND E ENCONTRAR
#COUNT E CONTAR