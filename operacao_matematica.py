from informar_numero import InformarNumeros

class OperacoesBasicas(InformarNumeros):
    '''Essa Classe comporta as operacoes de
    soma | subtração | multiplicação | divisão'''

    def __init__(self, primeiro_numero=0, segundo_numero=0):
        super().__init__(primeiro_numero, segundo_numero)

    def somar(self):
        '''Função para fazer uma soma dos números passados
        na função fale_seus_números da classe Numeros'''
        self.primeiro_numero = super().numeros_para_operar()
        self.segundo_numero = super().numeros_para_operar()
        return float(self.primeiro_numero + self.segundo_numero)

    def subtrair(self):
        '''Função para fazer uma subtração dos números passados
        na função fale_seus_números da classe Numeros'''
        self.primeiro_numero = super().numeros_para_operar()
        self.segundo_numero = super().numeros_para_operar()
        return float(self.primeiro_numero - self.segundo_numero)

    def multiplicar(self):
        '''Função para fazer uma multiplicação dos números passados
        na função fale_seus_números da classe Numeros'''
        self.primeiro_numero = super().numeros_para_operar()
        self.segundo_numero = super().numeros_para_operar()
        return float(self.primeiro_numero * self.segundo_numero)

    def dividir(self):
        '''Função para fazer uma multiplicação dos números passados
        na função fale_seus_números da classe Numeros'''
        self.primeiro_numero = super().numeros_para_operar()
        self.segundo_numero = super().numeros_para_operar()
        if self.segundo_numero == 0:#verifica se o divisor é zero
            raise TypeError("Não pode se dividir por zero")#informa que não pode fazer a divisão por zero
        return float(self.primeiro_numero / self.segundo_numero)

'''
2 + 5 = 7 (soma)
4 - 2 = 2 (subtração)
5 * 5 = 25 (multiplicação)
6 / 3 = 2 (divisão)
'''
