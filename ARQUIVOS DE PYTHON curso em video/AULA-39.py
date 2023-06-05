from datetime import date
nasc =  int(input('Digite o ano do seu nascimento: '))
'''nao importei a biblioteca '''
idadeDeAlistamento = 18
atual = date.today().year
idade = atual - nasc      

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldox = idade - 18
    saldo = abs(saldox)
    print(f'Voce ainda nao tem 18 anos.\nAinda faltam {saldo} anos para o alistamento ')
    ano = atual + saldo
    print(f'Seu alistamento sera em {abs(ano)}')
elif idade > 18:
    saldox = idade - 18
    saldo = abs(saldox)
    print(f'Voce ja deveria ter se alistado ha {saldo} anos ')
    ano = atual - saldo
    print(f'Seu alistamento deveria ter sido {ano}')