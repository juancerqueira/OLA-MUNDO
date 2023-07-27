print('GERADOR DE PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo),end='->')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos temos a voce que mostrar a mais? '))
print('ACABOU')
'''estudar mais isso '''