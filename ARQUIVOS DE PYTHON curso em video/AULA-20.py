'''programa para embaralhar'''
import random
n1 = str(input('DIGITE O NOME DO ALUNO: '))
n2 = str(input('DIGITE O NOME DO ALUNO:'))
n3 = str(input('DIGITE O NOME DO ALUNO:'))
n4 = str(input('DIGITE O NOME DO ALUNO:'))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)