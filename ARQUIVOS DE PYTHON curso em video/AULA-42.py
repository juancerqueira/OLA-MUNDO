
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)
r1 = float(input('Digite o complimento: '))
r2 = float(input('Digite o complimento: '))
r3 = float(input('Digite o complimento: '))

'''lista_das_retas = [r1, r2, r3] 
lista_das_retas.sort()'''

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('A soma dos lados formam um triagulo ', end='')
    if r1 == r2 ==r3:
        print('EQUILATERO')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else :
        print('ISOSCELES')
else:
    print('A soma dos lados nao formam um triangulo')