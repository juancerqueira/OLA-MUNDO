print('----SEQUENCIA DE FIBONACCI----')
print('=='*30)
termo = int(input('Quantos termos vc quer mostrar? '))
print('=='*30)
contador = 3 
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
soma = int(0)
while contador <= termo : 
    t3 = t1 + t2
    print(f'->{t3}', end='')
    contador += 1
    t1 = t2
    t2 = t3

print("-> FIM")    