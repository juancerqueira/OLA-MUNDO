cont  = numero = soma = 0 

while True :
        
        
         
        numero = int(input('Digite seu numero, ou 999 para parar? '))
        if numero == 999:
                break
        cont +=1 

        soma += numero

        
    
print (f'Soma dos numeros deu {soma}. ')

print ('Fim do programa')