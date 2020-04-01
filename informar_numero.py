
class InformarNumeros:
    def __init__(self, primeiro_numero=0, segundo_numero=0):
        self.__primeiro_numero = primeiro_numero
        self.__segundo_numero = segundo_numero

    def numeros_para_operar(self):
        '''Você deve informar os números 
        que você deseja fazer um cálculo''' 
        return float(input('Digite o número: '))

