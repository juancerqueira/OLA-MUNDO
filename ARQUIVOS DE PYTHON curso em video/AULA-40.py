nota2 = float(input('Nota 1 : '))  
nota3 = float(input('Nota 2 : '))  

media = (nota3 + nota2 ) / 2
print(f'a media do aluno e {media} entao ele esta')
if 7 > media > 5 :
    print('RECUPERAÇÃO')
'''elif media >= 5.0 and media <= 6.9 :
    print('RECUPERAÇÃO')'''
if media < 5 :
    print('REPROVADO')

elif media >= 7 :
    print('APROVADO')