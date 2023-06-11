print('='*41)
print('='*10,'LOJA JUAN CERQUEIRA','='*10 )
print('='*41)
preco = float(input('Preço das compras: R$ '))
print('PRODUTOS DISPONIVEIS')
print('=' * 40)

print('''FORMAS DE PAGAMENTO 
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

print('=' * 40)
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print(f'O valor das compras ficou em {preco - (preco * 10 / 100):.2f}')
elif opcao == 2:
    print(f'O valor das compras ficou em {preco - (preco * 5 / 100):.2f}')
elif opcao == 3:
    print(f'O valor fica em {preco:.2f}')
elif opcao == 4:

    parcela = int(input('Em quantas parcelas ? '))
    
    print(f'O valor das compras de ficou em {parcela} parcelas no valor total de  {(preco * 20 / 100 ) + preco:.2f} ')
    