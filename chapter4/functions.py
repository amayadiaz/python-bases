# Declarando Funciones
def mi_funcion():
    print ("Hola Mundo")


mi_funcion()

# Retornando valores
def mi_retorno():
    return "Hola Mundo"


frase = mi_retorno()
print (frase)

# Parámetros
# Los parámetros que una función espera, serán utilizados por ésta, dentro de su algoritmo, a modo de variables de ámbito local. Es decir, que los parámetros serán variables locales, a las cuáles solo la función podrá acceder.
def mi_nombre(nombre, apellido): 
    nombre_completo = nombre, apellido 
    print (nombre_completo)


mi_nombre("Julian", "Amaya")

# Llamar una función dentro de otra
def funcion():
    return "Hola Mundo"

# Parámetros por omisión
def saludar(nombre, mensaje='Hola'): 
    print (mensaje, nombre)
    print (funcion())


saludar('Julian Amaya')

# FUNCIONES 
# A la definición de una función la deben anteceder dos líneas en blanco.
# Al asignar parámetros por omisión, no debe dejarse espacios en blanco ni antes ni después del signo =.

# Recursividad
# Las llamadas recursivas deben solo utilizarse cuando sea estrictamente necesario y no exista una forma alternativa viable, que resuelva el problema evitando la recursividad.
# Python admite las llamadas recursivas, permitiendo a una función, llamarse a sí misma, de igual forma que lo hace cuando llama a otra función.
def jugar(intento=1): 
    respuesta = input("¿De qué color es una naranja? ") 
    if respuesta != "naranja": 
        if intento < 3: 
            print ("\nFallaste! Inténtalo de nuevo") 
            intento += 1 
            jugar(intento) # Llamada recursiva 
        else: 
            print ("\nPerdiste!") 
    else:
        print ("\nGanaste!") 
jugar()

# NOTA FINAL: una función, puede tener cualquier tipo de algoritmo y cualquier cantidad de ellos y, utilizar cualquiera de las características vistas hasta ahora. No obstante ello, una buena práctica, indica que la finalidad de una función, debe ser realizar una única acción, reutilizable y por lo tanto, tan genérica como sea posible.



