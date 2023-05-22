## PROGRAMA PARA ESCOLHERO ALUNO PARA APAGAR UM QUADRO



import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))

lista = [n1,n2,n3]
escolhido = random.choice(lista)
print('O aluno foi o {}'.format(escolhido))