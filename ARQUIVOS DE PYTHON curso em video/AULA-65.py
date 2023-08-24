
resp = 'S'
quantidade = soma = media = maior = menor =  0 

'''while parar != 'Nn' : '''
while resp in 'Ss' : 
    numero = int(input('Digite seu numero: '))
    soma += numero
    quantidade += 1 
    if quantidade == 1 :
        maior = menor = numero
    else:
        if numero > maior :
            maior = numero
        if numero < menor :
            menor = numero
    
    resp = str(input('Voce que continuar ? [S/N]: ')).upper().strip()[0]#DEIXAR MAIUSCULAR .UPPER()// .STRIP()[0] TIRA OS ESPAÇOS E O [0] PEGA O PRIMEIRO INDEX 
 

media = soma / quantidade  
print(f'''
      Quantas vezes voce digitou {quantidade}
      E a media e {media} 
      O numero maior e {maior}
      E o numero menor {menor} ''')
print('FIM!....')
