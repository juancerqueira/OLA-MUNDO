
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)
reta1 = float(input('Digite o complimento: '))
reta2 = float(input('Digite o complimento: '))
reta3 = float(input('Digite o complimento: '))

lista_das_retas = [reta1, reta2, reta3] 
lista_das_retas.sort()

if lista_das_retas[2] > lista_das_retas[0 + 1]:
    print('A soma dos lados nao formam um triagulo ')
else:
    print('A soma dos lados formam um triangulo')


