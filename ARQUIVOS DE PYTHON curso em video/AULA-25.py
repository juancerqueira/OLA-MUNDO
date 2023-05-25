'''cadeia de caracteres'''



nome = str(input('qual seu nome completo: ')).strip()
print('Seu nome tem silva? {}'.format('silva' in nome.lower()))