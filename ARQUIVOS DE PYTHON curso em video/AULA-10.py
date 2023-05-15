# criar um programa que ler quantos dolares a pessoa tem  na carteira 
## e quantos dólares ela pode comprar//
##e quantos dólares ela tem na carteira //
real = float(input('Quanto de dinheiro vc tem na carteira ? R$'))
dolar = real / 3.27
print('Com R${:.2f} voce pode compra U${:.2f}'.format(real, dolar))