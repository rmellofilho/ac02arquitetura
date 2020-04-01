
class Cumprimentacoes:
    def __init__(self, fala=str):
        self.fala = fala

    def saudacao(self):
        self.fala = '''
        Seja Bem-Vindo a calculadora de operações básicas!
        '''
        return self.fala

    def despedida(self):
        self.fala = "\nObrigado por usar nossa calculadora!\nVolte Sempre!"
        return self.fala
