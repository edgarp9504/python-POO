class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Estoy cominando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Estoy moviendome en mi bicicleta')

def main():
    persona = Persona('Edgar')
    persona.avanza()

    ciclista = Ciclista('Pancho')
    ciclista.avanza()

if __name__ == '__main__':
    main()