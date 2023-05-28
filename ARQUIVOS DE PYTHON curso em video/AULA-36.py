valorDaCasa =  float(input('Valor da casa : R$ '))
salario =  float(input('Salario : R$ '))
anos =  int(input('Anos de financiamento :  '))

prestacao =  valorDaCasa / ( anos * 12 )
minino = salario * 30 / 100
#if prestacao <= (salario * 30 / 100) : nao seria aprovado
if prestacao <= minino :
    print('Seu financiamento foi aprovado! ')
    print('O valor da prestação e de {:.2f}'.format(prestacao))
else:
    print('Seu financiamento não foi aprovado! ')   
    print('O valor da prestação ficaria muito alto {:.2f},  '.format(prestacao) )





'''
if salario <= 1250:
    novo = salario + ( salario * 15 / 100)
else:
    novo = salario + ( salario * 10 / 100)

print (' seu novo salario e {}'.format(novo))'''