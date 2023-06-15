'''
validador = str(input('Digite Brasil para continuar: '))'''
validador = ''

while validador != 'Brasil':
    print('A palavra chave nao connfere digite novamente')
    validador = input('Digite "Brasil" para continuar : ')
    
    validador = validador.capitalize()
    

    if validador == 'Brasil':
        print('Agora voce dogitou Brasil corretamente.')

        break 

print (' PARABENS')
