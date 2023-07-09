
somaIdade = 0 
mediaIdade = 0
maiorIdadeDeHomem = 0 
nomeVelho = ''
mulheresMenor = 0 
for p in range(1,4):
    print(f'----- {p} PESSOA ------')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]:  ')).strip().upper()
    somaIdade += idade
    if p == 1 and sexo in 'Mn':
        maiorIdadeDeHomem = idade
        nomeVelho = nome

    if sexo in'Mm' and idade > maiorIdadeDeHomem:
        maiorIdadeDeHomem = idade
        nomeVelho = nome
    elif sexo in 'Fm' and idade < 20:
        mulheresMenor = +1

mediaIdade = somaIdade / 3
print('--'*20)
print(f'A media de idade do grupo e de {mediaIdade:.1f} anos ')
print('--'*20)
print(f'O nome do homem mais velho e {nomeVelho} e a idade e {maiorIdadeDeHomem}')
print('--'*20)
print(F'O total de mulheres com menos de 20 anos e {mulheresMenor}')
print('--'*20)