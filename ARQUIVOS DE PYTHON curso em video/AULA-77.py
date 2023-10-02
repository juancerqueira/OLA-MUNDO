palavras = ('aprender','escrever','programar','estudar', 'python','gratis','praticar','mercado','programador','futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='') 
    '''para quebra linha usar end="" '''
    for letra in p :
        if letra.lower() in 'aeiou':
            print(letra, end=' ' )