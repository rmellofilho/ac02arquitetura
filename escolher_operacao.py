class EscolherOperacoes:
    def __init__(self, escolha=int):
        self.escolha = escolha

    def digitar_operacao(self):
        self.escolha = int(input("Digite a opção: "))
        return self.escolha

