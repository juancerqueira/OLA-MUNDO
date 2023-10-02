tupla = ('lapis', 1.75 ,
        'borracha', 2 ,
        'caderno', 15.78 ,
        'Estojo', 0.96,
        'transferidor', 4.00,
            )
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range (0, len(tupla)):
    if item % 2 == 0 :
        print(f'{tupla[item]:.<30}', end='')
    elif item % 2 == 1 :
        print(f'R$ {tupla[item]:>7.2f}')