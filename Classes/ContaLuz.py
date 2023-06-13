class ContaLuz:
    def __init__(self,numero,numeroLeitura,valorPagar,dataLeitura,dataPagto,kwGasto):
        self.__numero = numero
        self.__numeroLeitura = numeroLeitura
        self.__valorPagar = valorPagar
        self.__dataLeitura = dataLeitura
        self.__dataPagto = dataPagto
        self.__kwGasto = kwGasto

    def getValorPagar(self):
        return self.__valorPagar

    def getNumero(self):
        return self.__numero

    def getNumeroLeitura(self):
        return self.__numeroLeitura

    def getDataLeitura(self):
        return self.__dataLeitura

    def getDataPagto(self):
        return self.__dataPagto
    
    def getKwGasto(self):
        return self.__kwGasto