class MenuOpcoes:
    def __init__(self, fala=str, lista_operacoes=list):
        self.fala = fala
        self.lista_operacoes = lista_operacoes

    def menu_operacoes_basicas(self):
        '''Menu de operações matemáticas'''
        self.fala = "\n---- Calculadora iniciada ----\nSelecione a opção desejada\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n0 - Sair da calculadora\n"
        return self.fala


