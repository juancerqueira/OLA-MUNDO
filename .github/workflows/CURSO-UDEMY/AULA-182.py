class BaseDeDados:

    def __init__(self):
        self.dados = {}
       # self._dados = {}
        '''Declarado como protegido ( ainda acessivel de fora da class)'''

      #  self.__dados = {}
        ''' decladoro como privado (inacessivel e imutavel de fora da class )'''

base = BaseDeDados( )


print(base.dados)   