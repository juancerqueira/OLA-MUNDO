soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f'Digite o seu {c} valor:'))
    if numero % 2 == 0 :
        soma += numero 
        cont += 1
print(f'a soma e {soma} a quantidade de numero pares e {cont}')   