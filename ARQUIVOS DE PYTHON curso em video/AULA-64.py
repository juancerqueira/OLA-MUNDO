


contador = numero = total = 0 
numero = int(input('Digite seu numero, ou 999 para parar? '))
while numero != 999 :
        contador += 1 
        total = total + numero  
        numero = int(input('Digite seu numero, ou 999 para parar? '))
print (f'Soma dos numeros deu {total} e voce digitou {contador} ')

print ('Fim do programa')

'''contador = numero = total = 0 

while numero != 999 :
    numero = int(input('Digite seu numero, ou 999 para parar? '))

    if numero <= 998 : 
        contador += 1 
        total = total + numero  
print (f'Soma dos numeros deu {total} e voce digitou {contador} ')

print ('Fim do programa')'''