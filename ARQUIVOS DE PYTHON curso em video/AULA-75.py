n1 = int(input('DIGITE UM NUMERO: '))
n2 = int(input('DIGITE OUTRO NUMERO: '))
n3 = int(input('DIGITE MAIS UM NUMERO:'))
n4 = int(input(' DIGITE O ULTIMO NUMERO: '))
lista = (n1, n2 , n3, n4) #criando uma lista com os valores digitados.
print(f'VOCE DIGITOU OS VALORES {lista}')
print(f'O VALOR 9 AARECEU {lista.count(9)} vezes')
if 3 in lista:
    if 3 in lista:
        print ('o valor 3 apareceu na posição {}'.format(lista.index(3)+1))#mostra a pos
    else:
        print('VOCE NAO DIGITOU NEM UM VALOR 3  ')
print('OS VALORES PARES DIGITADOS FORAM ', end='')
for n in lista :
    if n % 2 ==0:# mostrando se o numero é par ou impar           
        print( n , end='-')
    
print( end='.')