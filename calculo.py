
class Calculadora:

    def __init__(self, primeiro_numero, segundo_numero):
        self.primeiro_numero = primeiro_numero
        self.segundo_numero = segundo_numero

    def somar(self):
        return float(self.primeiro_numero + self.segundo_numero)

    def subtrair(self):
        return float(self.primeiro_numero - self.segundo_numero)

    def multiplicar(self):
        return float(self.primeiro_numero * self.segundo_numero)

    def dividir(self):
        if self.segundo_numero == 0:
            return "Não pode se dividir por 0!"
        return float(self.primeiro_numero / self.segundo_numero)


class CalculadoraCientifica(Calculadora):

    def pi(self):
        return 3.14159

    def porcentagem(self):
        percentual = self.primeiro_numero
        total = self.segundo_numero
        multiplicacao = Calculadora(percentual, total).multiplicar()
        divisao = Calculadora(multiplicacao, 100).dividir()
        return divisao

    def potencia(self):
        base = self.primeiro_numero
        elevado = self.segundo_numero
        resultado = base
        for numero in range(1, elevado):
            resultado = Calculadora(base, resultado).multiplicar()
        return resultado
