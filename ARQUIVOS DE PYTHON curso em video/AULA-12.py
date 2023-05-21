#Faça um algoritmo qua leia o preço da um produto a mostra seu novo preço, com 5% da dasconto. >>>10x5/100
preco = float(input('Preço real do produto: R$ '))
novo_preco = preco - (preco * 5 / 100)
print ('O desconto de 5% em cima do valor de {} e igual a {}'.format(preco, novo_preco))
