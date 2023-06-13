from .ContaLuz import ContaLuz

class Contas:
    def __init__(self):
        self.__contasLuz = []

    def addContaLuz(self,conta:ContaLuz):
        self.__contasLuz.append(conta)

    def mediaConsumoValor(self):
        media = 0
        for conta in self.__contasLuz:
            media += conta.getValorPagar()
        return f"A media das Contas R$ {media/len(self.__contasLuz):.2f}"

    def verificarContas(self):
       
        conta_mais_alta = None
        conta_mais_baixa =  None

        for i in range(len(self.__contasLuz)-1):
            a = self.__contasLuz[i].getValorPagar()
            b = self.__contasLuz[i+1].getValorPagar()
            if a > b:
                conta_mais_alta = self.__contasLuz[i]
            else:
                conta_mais_alta = self.__contasLuz[i+1]

            if a < b:
                conta_mais_baixa = self.__contasLuz[i]
            else:
                conta_mais_baixa = self.__contasLuz[i+1]

        

        return f"Menor conta R$ {conta_mais_baixa.getValorPagar()} Maior conta R$ {conta_mais_alta.getValorPagar()}"