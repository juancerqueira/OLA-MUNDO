'''for c in range(1 , 51):
    divisao = c % 2
    if divisao == 0:
        print (c, end=' ')'''

for c in range(2 , 51, 2):    
    print('.', end='')
    if c % 2 == 0 :
        print (c, end=' ')