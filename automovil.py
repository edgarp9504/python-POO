class Automovil:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else: 
            self._motor.inyecta_gasolina(3)

        self._estado = 'movimiento'

class Motor:

    def __init__(self, cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Parabrisas:

    def __init__(self, accion):
        self.accion = accion
        self.encender = 'on'
        self.apagado = 'of'

    def prender_limpiaparabrisas(self, encender,apagado):
        if self.encender == 'on':
            self.encender
        else:
            self.apagado