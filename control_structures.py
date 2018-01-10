# -*- coding: utf-8 -*-
# Encoding: el encoding no es más que una directiva que se coloca al inicio de un archivo Python, a fin de indicar al sistema, la codificación de caracteres utilizada en el archivo.abs

# Asignación múltiple
a, b, c = 'Hola', 15, True
print (b)

# Condicionales
semaforo = 3
if semaforo == 1:
    print ("No pase")
elif semaforo == 2:
    print ("Aliste motores")
else:
    print ("Siga")    

# Estructuras de control iterativas
# While: Este bucle, se encarga de ejecutar una misma acción "mientras que" una determinada condición se cumpla.
anio = 2000
while anio <= 2005:
    print ("Bienvenido al Año: ", str(anio))
    anio += 1

# For: el bucle for, en Python, es aquel que nos permitirá iterar sobre una variable compleja, del tipo lista o tupla.
mi_lista = ['Juan', 'Lionel', 'Luis', 'James']
for nombre in mi_lista:
    print (nombre)
# Otra forma de iterar con el bucle for, puede emular a while. 
for anio in range(2000, 2006):
    print ("Bienvenido al año: ", anio)

 