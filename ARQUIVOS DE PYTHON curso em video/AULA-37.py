num = int(input('DIGITE UM NUMERO INTEIRO: '))
print('''ESCOLHA UMA DAS BASES PARA CONVERSÃO:
[1] CONVERTER PARA BINARIO 
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL''')
op = int(input('DIGITE SUA OPÇÃO: '))
if op == 1 :
    print('O NUMERO {} EM BINARIO É {}'.format(num, bin(num)[2:]))
elif op == 2 :
    print('{} convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('-=-'*20)   
    print('OPÇÃO INVALIDADE TENTE NOVAMENTE ')
    print('-=-'*20)    