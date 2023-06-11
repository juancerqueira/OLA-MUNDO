'''def converter_numero(numero):
    if isinstance(numero, int):
        return numero / 100.0
    else:
        return numero 


peso = float(input('Qual e seu peso ?(kg) '))
altura = float(input('Qual e a sua altura? (metros ex 175) '))

altura = converter_numero(altura)

print(altura)

imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa e de {imc:.2f}')'''

'''numero = input("Digite um número: ")
if numero.isdigit():
    numero = float(numero) / 100.0
    print(f"O número convertido para float é: {numero}")
else:
    print(f"O número não é inteiro e permanece como: {numero}")'''


altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso :  "))

if altura > 10:
    altura = altura / 100.0

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print('Voce esta abaixo do peso ')
elif imc >= 18.5 and imc < 25:
    print('voce esta no peso normal')
elif imc <= 30 :
    print('voce esta com sobrepeso')
elif imc <= 40 :
    print('voce esta com obesidade')
else : 
    print('voce esta com OBESIDADE MORDIDA')
