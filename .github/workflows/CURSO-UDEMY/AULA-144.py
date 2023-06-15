usuarios = {'JOAO': {'EDIFITICADOR':'0001',
                    'CARGO':'PORTEIRO',
                    'SALARIO':'2000'},       
            'MARIA':{'EDIFITICADOR':'0002',
                     'CARGO':'AUX LIMPERA',
                     'SALARIO':'1900'},
            'JOSE':{'EDIFITICADOR':'0003',
                     'CARGO':'TECNICO',
                     'SALARIO':'2500'} }


for chaves , valores in usuarios.items():
    print(f'FUNCIONARIOS:{chaves}')

    for i , j in valores.items():
        print(f'\t {i} - {j}')