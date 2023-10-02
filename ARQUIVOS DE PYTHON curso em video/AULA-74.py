from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
valorMaior = max(n)
valorMenos = min(n)
print (f'Eu sorteei o valor {n}')
print (f'O valor maior do sorteio {valorMaior}')
print (f'O valor menos do sorteio {valorMenos}')