'''def format_string(input_string):
    input_string = input_string.strip()
    input_string = ' '.join(input_string.split())
    return input_string'''
'''def format_string(input_string):
    input_string = input_string.upper()
    input_string = ' '.join(input_string.split())
    return input_string'''



'''frase = format_string(input('Digite sua frase: ')).upper()'''
frase = str(input('Digite uma frase: ')).upper().split()

#.strip elimina os espaços antes e depois 

# split eu separo os elementos de uma string em uma lista 
#''.join eu juntos os elementos e uma string so 



junto = ''.join(frase)
'''inverso = '''''
inverso= junto[::-1]


'''for letra in range(len(junto) -1, -1,-1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} e {inverso}')
if junto == inverso:
        print('Termos um palindromo')
else:
     print('Frase não e palindromo!')