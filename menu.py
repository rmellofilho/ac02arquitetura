
from calculo import CalculadoraCientifica, Calculadora


class PassarNumero:

    def digitar_numero(self, mensagem): 
        '''Método para receber os números'''
        return float(input(mensagem))

    def escolher_opcao(self):
        '''Método listar opções e receber opção do usuário'''
        return int(input("1 para soma\n"+
                        "2 para subtração\n" +
                        "3 para multiplicação\n" +
                        "4 para divisão\n" +
                        "5 para potência\n" +
                        "6 para porcentagem\n" +
                        "7 para PI\n" +
                        "0 para SAIR\n" +
                        "Digite uma das opções acima: "))


class ExecutarMenuOperacoes:

    def apresentar_resultado(self):

        while True:#Enquanto for verdadeiro irá fazer o bloco abaixo
            print("************** CALCULAR **************")
            opcao = PassarNumero().escolher_opcao()
            if opcao == 1:
                print(ExecutarOperacao().executar_soma())
            elif opcao == 2:
                print(ExecutarOperacao().executar_subtracao())
            elif opcao == 3:
                print(ExecutarOperacao().executar_multiplicacao())
            elif opcao == 4:
                print(ExecutarOperacao().executar_divisao())
            elif opcao == 5:
                print(ExecutarOperacao().executar_potencia())
            elif opcao == 6:
                print(ExecutarOperacao().executar_porcentagem())
            elif opcao == 7:
                print(ExecutarOperacao().executar_pi())
            elif opcao == 0:
                exit()#Fecha o python
            else:
                print("Opção inválida!")
    

class ExecutarOperacao:

    def executar_soma(self):
        print("************** SOMA **************")
        primeiro_numero = PassarNumero().digitar_numero("Informe o primeiro número: ")
        segundo_numero = PassarNumero().digitar_numero("Informe o segundo número: ")
        resultado = Calculadora(primeiro_numero, segundo_numero).somar()
        return f'Resultado: {resultado}'
    
    def executar_subtracao(self):
        print("************** SUBTRAÇÃO **************")
        primeiro_numero = PassarNumero().digitar_numero("Informe o primeiro número: ")
        segundo_numero = PassarNumero().digitar_numero("Informe o segundo número: ")
        resultado = Calculadora(primeiro_numero, segundo_numero).subtrair()
        return f'Resultado: {resultado}'
    
    def executar_multiplicacao(self):
        print("************** MULTIPLICAÇÃO **************")
        primeiro_numero = PassarNumero().digitar_numero("Informe o primeiro número: ")
        segundo_numero = PassarNumero().digitar_numero("Informe o segundo número: ")
        resultado = Calculadora(primeiro_numero, segundo_numero).multiplicar()
        return f'Resultado: {resultado}'
    
    def executar_divisao(self):
        print("************** DIVISÃO **************")
        primeiro_numero = PassarNumero().digitar_numero("Informe o primeiro número: ")
        segundo_numero = PassarNumero().digitar_numero("Informe o segundo número: ")
        resultado = Calculadora(primeiro_numero, segundo_numero).dividir()
        return f'Resultado: {resultado}'
    
    def executar_potencia(self):
        print("************** POTÊNCIA **************")
        base = int(PassarNumero().digitar_numero("Informe o número percentual: "))
        elevado = int(PassarNumero().digitar_numero("Informe o elevado: "))
        resultado = CalculadoraCientifica(base, elevado).potencia()
        return f'Resultado: {resultado}'
    
    def executar_porcentagem(self):
        print("************** PORCENTAGEM **************")
        percentual = PassarNumero().digitar_numero("Informe o número percentual: ")
        total = PassarNumero().digitar_numero("Informe o total: ")
        resultado = CalculadoraCientifica(percentual, total).porcentagem()
        return f'Resultado: {resultado}'

    def executar_pi(self):
        return f'A costante de PI é: {CalculadoraCientifica(0,0).pi()}'
    
