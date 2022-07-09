class Motor():
    def __init__(self,tipo):
        self.tipo = tipo
    def getEmissao(self):
        return print(self.emissao)


class Combustao(Motor):
    def __init__(self,vida_util,emissao,potencia):
        self.vida = vida_util
        self.emissao = emissao
        self.potencia = potencia


class Hibrido(Motor):
    def __init__(self,vida_util,emissao,potencia):
        self.vida = vida_util
        self.emissao = emissao
        self.potencia = potencia


class Elétrico(Motor):
    def __init__(self,vida_util,potencia):
        self.vida = vida_util
        self.emissao = 0
        self.potencia = potencia

class Veiculo(Motor):
    def __init__(self,cor,marca,imposto):
        self.cor = cor
        self.marca = marca
        self.imposto = imposto
        self.motor = Motor.tipo

    def cobrarImposto(self):
        self.imposto = Motor.emissao * 0.3


class Carro(Veiculo):
    def __init__(self,capacidade,modelo):
        self.capacidade = capacidade
        self.modelo = modelo


class Caminhão(Veiculo):
    def __init__(self,capacidade,modelo):
        self.capacidade = capacidade
        self.modelo = modelo
