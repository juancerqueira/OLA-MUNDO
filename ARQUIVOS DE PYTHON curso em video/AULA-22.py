'''cadeia de caracteres'''


nome = str(input('QUAL SEU NOME: ')).strip()
## strip para contar os espaços
print ('ANALISANDO SEU NOME {}'.format(nome))
print('SEU NOME EM MAIUSCULAS E {}'.format(nome.upper()))
'''upper para saber ser a letra e maiuscula '''
print('SEU NOME EM MINUSCULAS E {}'.format(nome.lower()))
'''lower para deixa seu nome em minusculas'''
print('SEU NOME TEM AO TODO {} LETRAS '.format(len(nome) - nome.count(' ')))
'''PARA CONTAR SEU NOME INTEIRO'''

#print ('SEU PRIMEIRO NOME TEM {} LETRAS'.format(nome.find(' ')))

'''PARA ENCONTRAR QUAL É A POSIÇÃO DO PRIMEIRO ESPAÇO'''
separa = nome.split()
print('SEU PRIMEIRO NOME E {} E ELE TEM {} LETRAS'.format(separa[0], len(separa[0])))