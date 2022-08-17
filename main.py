class Sequencia:
    def __init__(self, potencia, fim):
        self._potencia = potencia
        self._fim = fim
        self._indice = 1

    def setSequencia(self, potencia):
        if (isinstance(potencia, int)):
            self._potencia = potencia
    
    def getFim(self):
        return self._fim

    def proximo(self):
        proximo = self._potencia ** self._indice 
        self._indice += 1
        return proximo

class Grafico:
    def __init__(self, caracterImpressao):
        self._caracter = caracterImpressao

    def conecta(self, sequencia ):
        self._sequencia = sequencia

    def plot(self):
        for i in range(self._sequencia.getFim()+1):
            print(self._caracter * self._sequencia.proximo())

sequenciaExp2 = Sequencia(2, 8)
grafico = Grafico('#')
grafico.conecta(sequenciaExp2)

grafico.plot()
