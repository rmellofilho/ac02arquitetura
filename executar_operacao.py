from escolher_operacao import EscolherOperacoes
from menu import MenuOpcoes
from operacao_matematica import OperacoesBasicas
from cumprimentar import Cumprimentacoes


class ExecutarOperacoes:
    def __init__(self, operacao=int):
        self.operacao = operacao

    def executar_operacao_basica(self):
        '''Executa a operação básica sendo as que
        estão em opção no menu'''
        self.operacao = EscolherOperacoes().digitar_operacao()
        while self.operacao not in [1, 2, 3, 4, 0]:
            print("Está opção não está no menu digite novamente")
            self.operacao = EscolherOperacoes().digitar_operacao()
        if self.operacao == 0:
            return Cumprimentacoes().despedida()
        elif self.operacao not in [1, 2, 3, 4]:
                raise TypeError("Essa opção não está no Menu!")#informa que não está no menu a opção desejada
        elif self.operacao == 1:
            return OperacoesBasicas().somar()
        elif self.operacao == 2:
            return OperacoesBasicas().subtrair()
        elif self.operacao == 3:
            return OperacoesBasicas().multiplicar()
        elif self.operacao == 4:
            return OperacoesBasicas().dividir()
