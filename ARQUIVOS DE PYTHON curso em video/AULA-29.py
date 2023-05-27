velocidade = int(input('Digite a velocidade : ')) 
if velocidade > 80:
    print('Você foi multado em R$ {}'.format((velocidade - 80) * 7))
 
else :
    print ('Parabens voce nao passou o limite de velocidade')