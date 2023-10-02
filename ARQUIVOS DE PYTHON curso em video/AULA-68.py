from random import randint
v = 0 
while True:
    jogados = int(input('Digite um numero: '))
    pc = randint(0,10)
    total = jogados + pc
    tipo = ' '
    
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
        print(f'Vc digitou {jogados} e o computador {pc}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0 :
            print(f'Você venceu! O computador escolheu {pc} e você {jogados}, o resultado')
            v += 1
        else : 
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1 :
             print(f'Você venceu! O computador escolheu {pc} e você {jogados}, o resultado')
             v += 1
        else : 
            print('Voce perdeu')
            break
    
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes')
    