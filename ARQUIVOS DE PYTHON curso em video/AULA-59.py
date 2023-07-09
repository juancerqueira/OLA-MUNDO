n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opcao = 0
print('-*'*20)
print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
print('-*'*20)
opcao = int(input('Qual é a sua opção? '))
while opcao != 5 :
    print('-*'*20)
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    print('-*'*20)
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1: 
        print('-*'*20)
        resultado= n1 + n2
        print(f"A soma de {n1} e {n2} é {resultado}")
        print('-*'*20)
    if opcao == 2 :
        print('-*'*20)
        resultado= n1 * n2
        print(f"A multiplicação de {n1} e {n2} é {resultado}")
        print('-*'*20)
    if opcao == 3 :
        if n1 > n2 :
            maior = n1
        else:
            maior = n2
        print('-*'*20)
        print(f'O resultado de {n1} e {n2} o maior e {maior}')
        print('-*'*20)
    if opcao == 4 :
        print('informe os numeros novamente :')
        print('-*'*20)
        n1 = int(input('Primeiro numero: '))
        print('-*'*20)
        n2 = int(input('Segundo numero: '))
        print('-*'*20)
    if opcao > 5 :
        print('-*'*20)
        print('Opção invalida...Digite um numero do menu')
        print('-*'*20)
print('Fim do programa ! volte sempre!')