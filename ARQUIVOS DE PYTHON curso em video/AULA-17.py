import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adijacente '))
hi_modulo_sem_importacao = (co ** 2 + ca ** 2) ** (1/2)

hi = math.hypot(co, ca)

print ('O valor de {}'.format(hi))
