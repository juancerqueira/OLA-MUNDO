#Faça um algoritmo qua laia o salário da um Funcionário a mostra sau
#novo salário, com 15% da aumento.
salario = float(input(' Qual e o salario do funcionario ? R$'))
novo_salario = salario + (salario * 15 / 100)
print(' O novo salario e de R$ {:.2f}'.format(novo_salario))

produto = float(input('Qual o valor do produto ? R$'))

produto_desconto5 = produto - (produto * 5 / 100)
print('O valor do produto com desconto de 5% {:.2f}'.format(produto_desconto5))

produto_parcelado6x = produto + (produto * 6 / 100)
valor_de_parcela6x = produto_parcelado6x / 6
print('O produto parcelado em 6 x fica no valor total de {:.2f} e o valor de cada parcela fica {:.2f} '.format(produto_parcelado6x, valor_de_parcela6x ))

