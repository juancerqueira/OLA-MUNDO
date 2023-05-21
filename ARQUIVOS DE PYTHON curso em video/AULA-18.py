
import math

an = float(input('Digite o angulo : '))

seno = math.sin(math.radians(an))
print('O angulo de {} tem o seno de {:.2f} '.format (an, seno))

coseno = math.cos(math.radians(an))

print('O angulo de {} tem o coseno de {:.2f} '.format (an, coseno))

tange = math.tan(math.radians(an))

print('O angulo de {} tem a tangente de {:.2f}'.format(an,tange))