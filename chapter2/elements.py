# Variable: utilizar nombres descriptivos y en minúsculas. Para nombres compuestos, separar las palabras por guiones bajos. Antes y después del signo =, debe haber uno (y solo un) espacio en blanco.
mi_variable = 1

# Constantes: utilizar nombres descriptivos y en mayúsculas separando palabras por guiones bajos.
MI_CONSTANTE = 12

# Imprimir
print (mi_variable)

# Cadena Multilínea
cadena_multilinea = """Esta es una cadena de 
varias líneas."""
print (cadena_multilinea)

# Operadores
mi_suma = 1 + 3 
print (mi_suma)

# Comentarios
# Este es un comentarios de una línea 
"""Este es un comentario de varias líneas"""
# Comentarios en la misma línea del código deben separarse con dos espacios en blanco. Luego del símbolo # debe ir un solo espacio en blanco.
# Correcto
a = 24  # Edad de Julián

# Tupla: una tupla es una variable que permite almacenar varios datos inmutables (NO PUEDEN SER MODIFICADOS UNA VEZ CREADOS) de tipos diferentes.
mi_tupla = ('Hola', 3, 'Mundo', 24)
# Se puede acceder a cada uno de los datos mediante su índice correspondiente, siendo 0 (cero), el índice del primer elemento. 
print (mi_tupla[0])

# Listas: una lista es similar a una tupla con la diferencia fundamental de que PERMITE MODIFICAR los datos una vez creados
mi_lista = ['Julian', 'Laura', 24, 31, 'Hely']
# A las listas se accede igual que a las tuplas, por su número de índice.
print (mi_lista[0])
# Las listas NO son inmutables, permiten modificar los datos una vez creados.
mi_lista[0] = 'Mario'
print (mi_lista[0])
# Las listas, a diferencia de las tuplas, permiten agregar nuevos valores.
mi_lista.append('Julian')
print (mi_lista)

# Diccionarios: los diccionarios permiten utilizar una clave para declarar y acceder a un valor.
mi_diccionario = {'jugador_1': 'Messi', 'jugador_2': 'Iniesta', 'jugador_3': 'Neymar'}
print (mi_diccionario['jugador_1'])
# Un diccionario permite eliminar cualquier entrada.
del(mi_diccionario['jugador_3'])
print (mi_diccionario)
# Al igual que las listas, el diccionario permite modificar los valores.
mi_diccionario['jugador_2'] = 'Coutinho'
print (mi_diccionario)
