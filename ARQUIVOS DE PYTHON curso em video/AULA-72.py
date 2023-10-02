cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True: 
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <=20:
        print(f'Voce digitou o numero {cont[num]} ')
    continuar = str(input('Vc quer continuar?[S/N] ')).strip()[0].upper()
    if continuar in 'Nn':
        break
    if continuar in 'Ss':
        print('Otimo.. Escolha outro numero.')
    else:
        print('Tente novamente...')
    
