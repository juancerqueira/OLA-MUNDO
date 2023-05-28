salario = float(input('Digite seu salario: R$ '))

'''ERREI TUDO, FUI EU QUE FIZ  

if salario => 1250 or (salario * 10) / 100:
    print (' seu valor agora e {}'.format((salario * 10) / 100 + salario ))
else salario <= salario1 or (salario * 15) / 100:
    print (' seu valor agora e {}'.format((salario * 15) / 100 + salario ))'''

#PARA CALCULAR PORCENTAGEM 


if salario <= 1250:
    novo = salario + ( salario * 15 / 100)
else:
    novo = salario + ( salario * 10 / 100)

print (' seu novo salario e {}'.format(novo))