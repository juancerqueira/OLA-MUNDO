'''cadeia de caracteres'''


num = int(input('Informe seu numero: '))
'''n = str(num)'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena:{} '.format(d))
print('Centene:{} '.format(c))
print('Milhar:{} '.format(m))
