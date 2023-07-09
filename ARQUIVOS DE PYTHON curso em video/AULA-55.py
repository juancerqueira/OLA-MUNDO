maior = 0 
menor = 0
for c in range(1,6):
    peso = float(input('Digite seu peso '))
    if c == 1 :
        maior= peso 
        menor= peso  
    elif maior > peso:
        maior = peso
    elif  menor < peso:
        menor = peso
    
print(f'O maior peso foi {maior} e o menor peso foi {menor}')