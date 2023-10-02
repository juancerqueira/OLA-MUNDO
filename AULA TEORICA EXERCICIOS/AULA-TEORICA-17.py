'''LISTAS 
LANCHE = ['BURGE','BEER','PIZZA','PUMDIM']
PARA ADD O QUINTO ITEM COMANDO USADO 

..................

LANCHE.APPEND('COOKI')

LANCHE = ['BURGE','BEER','PIZZA','PUMDIM','COOKI']
..................

LANCHE.INSERT(0,'HOTDOG') 

LANCHE = ['HOTDOG','BURGE','BEER','PIZZA','PUMDIM','COOKI']

...................

FORMAR DE APAGAR O ITEM 

DEL LANCHE[3]
OU 
LANCHE.POP(3)
OU 
LANCHE.REMOVE9=('PIZZA') AQUI VC TEM QUE INDICAR O VALOR CONTEUDO 
 
LANCHE = ['HOTDOG','BURGE','BEER','ESSE QUE APAGOU','PUMDIM','COOKI']

........................

VALORES = [8,7,8,9,7,7,8,8,95,4,5,6,6,5,2]

VALORES.SORT()
ELE VAI ORDERNAR OS VALORES

VALORES.SORT(REVERSE=TRUE)

VAI ORDENAR OS VALORES DO FORMA REVERSA 

..........................

VALORES = [8,2,5,4,3,2,0]
LEN(VALORES)IGUAL A 7


'''

num = [ 2,5,9,1]
num[2] = 7 
num.append(7)
num.append(9)
num.append(6)
num.sort()
num.sort(reverse=True)
num.insert(2,333322) # posição , valor \ em lista  
print(num)
num.pop(4)
print (num)
print(f'essa lista tem {len(num)} elementos.')

valores= [5,9,8]
for v in valores:
    print(f'os valores de v  são {v}')

for c , v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('fim...')

for cont in range(0,1):
    valores.append(int(input(f'Digite um valor a mais {valores}: ')))



a = [ 2,3,4,7]
b = a[:]
b[2] = 8 
print(f'A lista a {a}')
print(f'A lista b {b}')

'''para fazer uma copia '''

