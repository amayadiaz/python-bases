# Cuando pensamos en objetos, todos los sustantivos son objetos. 
# Las cualidades son adjetivos. 
# Un objeto es un sustantivo que posee atributos, cuya cualidades lo describen. 
# Ejemplo: El computador es de color verde. 
# Un objeto puede realizar acciones. 
# En programación: Objeto = Objeto, Cualidades = Atributos o Propiedades, Acciones = Métodos.
# Polimorfismo: objetos relacionados entre sí, tienen nombres de atributos iguales como por ejemplo: color y tamaño, y sin embargo pueden tener valores diferentes.
# Herencia: objetos que son sub-tipos o ampliación de otros. 

# Programación Orientada a Objetos (POO)

# Clases: son los modelos sobre los cuáles se construirán nuestros objetos.
# El nombre de las clases se define en singular, utilizando CamelCase. 

# Propiedades: características intrínsecas del objeto. Son representadas a modo de variables.
# Las propiedades se definen de la misma forma que las variables (aplican las mismas reglas de estilo).

# Métodos: técnicamente son funciones, y son las acciones propias que puede realizar un objeto.
# Notar que el primer parámetro de un método, siempre debe ser self.

class Equipo:
    nombre = ""
    años = ""

class Entrenador:
    nombre = ""
    altura = ""
    equipo = Equipo()

    def hablar(self):
        print ("Hola a todos!")

# Objeto: Las clases por sí mismas, no son más que modelos que nos servirán para crear objetos en concreto. Podemos decir que una clase, es el razonamiento abstracto de un objeto, mientras que el objeto, es su materialización. A la acción de crear objetos, se la denomina instanciar una clase y dicha instancia, consiste en asignar la clase, como valor a una variable.

entrenador = Entrenador()
entrenador.nombre = "Ernesto Valverde"
entrenador.altura = "1.69 m"
print (entrenador.nombre)
entrenador.equipo.nombre = "Barcelona"
print (entrenador.equipo.nombre)

# Herencia: algunos objetos comparten las mismas propiedades y métodos que otro objeto, y además agregan nuevas propiedades y métodos. A esto se lo denomina herencia: una clase que hereda de otra. 

class Jugador(Entrenador):
    goles = ""

    def patear(self):
        pass

jugador = Jugador()
jugador.nombre = "Lionel Messi"
jugador.altura = "1.69 m"
jugador.equipo.nombre = "Barcelona"
jugador.goles = 530
print(jugador.goles)
jugador.hablar()



    





