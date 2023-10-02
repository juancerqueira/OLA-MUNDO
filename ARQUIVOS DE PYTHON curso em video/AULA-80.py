
lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('ADICIONADO AO FINAL DA LISTA...')
     # para saber o ultimo elemento da lista -1 ou nn[-1]
     # or e igual a OU 
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:    
                lista.insert(pos , n )
                print(f'ADICIONADO A POSSIÇÃO {pos} da lista ')
                print('BREAK ATIVOU...')
                break
            pos +=1


print('-='*20)
print(f'OS VALORES DIGITADOS FORAM {lista}')