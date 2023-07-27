'''from math import factorial'''
n = int(input('DIGITE O NUMERO QUE VC QUER SABER O FATORIAL: '))
'''f = factorial(n)
print (f'O fatorial de {n} e `{f}')'''
c = n 
f = 1
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
