valores = []

for cont in range(0,5):

    valores.append(int(input(f'Digite um valor a mais {valores}: ')))

print(f'O valores digitados foram {valores}')

print(f'O maior valor foi {max(valores)}')
print(f'O menor valor foi {min(valores)}')
