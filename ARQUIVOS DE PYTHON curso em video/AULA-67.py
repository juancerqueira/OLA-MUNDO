while True :
    
    print('--'*30)
    num= int(input('Digite o numero de sua tabuaba: \nOu numero negativo para sair : '))
    print('--'*30)
    if num < 0 :
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num * c}')

print('FIM DO PROGRAMA')
    