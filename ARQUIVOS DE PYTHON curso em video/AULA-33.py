'''a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

# Saber quem e menor
menor = a 
if (b<a and b<c) :
    maior = b
  
if (c<a and c<b) :
    menor = c
# Saber quem e maior
maior = a
if (b>a and b>c):
    maior = b

if (c>a and c>b):
    maior = c

print(f'menor valor e {menor}')
print(f'maior valor e {maior}')'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))
l = [n1, n2, n3]
# o metodo shot ordena a variavel dentro da lista
l.sort()
print(f'O maior número é {l[2]} e o menor é {l[0]}')