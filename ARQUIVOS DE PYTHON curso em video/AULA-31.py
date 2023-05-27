'''distancia = float(input('Digite a distancia de viagem :'))
if distancia <= 200 :
     print('O preço da passagem é de : R$ {:.2f}'.format(distancia * 0.50))

else:  
    print('O preço da passagem e de : R$ {:.2f}'.format(distancia*0.45))'''


distacia = float(input( 'Qual e a distancia da sua viagem? ' ) )
print('Voce esta prestes a começar uma viagem de {}'.format(distacia))

if distacia <= 200:
    preço = distacia * 0.50

else:
    preço = distancia * 0.45
print('E o da sua passagem sera de R${}'.format(preço))