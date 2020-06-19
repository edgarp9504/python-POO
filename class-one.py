class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self, otra_persona):
        return print(f'Hola {otra_persona.nombre}, me llamo {self.nombre} y mi edad es {self.edad}')

javier = Persona('Javier', 20)
erika = Persona('Erika', 18)

javier.saludar(erika)