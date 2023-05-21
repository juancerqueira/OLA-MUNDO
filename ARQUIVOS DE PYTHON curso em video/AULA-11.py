#Faça um programa qua laia a largura a a altura da uma parada am
#matros. calcula a sua área a a quantidada da tinta nacassária para
#pintá—la, sabendo qua cada litro da tinta, pinta uma área da 2m2.
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede :'))
area = larg * alt
print('Sua parede tem a dimensão {} x {} e sua area e de {}m2 .'.format(larg, alt, area))
tinta = area / 2 
print('Para pinta essa parede voce precisa de {}l de tinta'.format(tinta))