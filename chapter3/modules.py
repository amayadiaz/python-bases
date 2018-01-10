# -*- coding: utf-8 -*-
# En Python, cada uno de nuestros archivos .py se denominan módulos. Estos módulos, a la vez, pueden formar parte de paquetes. Un paquete, es una carpeta que contiene archivos .py. Pero, para que una carpeta pueda ser considerada un paquete, debe contener un archivo de inicio llamado __init__.py. Este archivo, no necesita contener ninguna instrucción. De hecho, puede estar completamente vacío.
# Los paquetes, a la vez, también pueden contener otros sub-paquetes.
# Y los módulos, no necesariamente, deben pertenecer a un paquete. 

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Importando módulos enteros
import chapter2.elements 

# Namespaces 
print (chapter2.elements.mi_suma)

# Alias
import chapter2.elements as ch2e
print (ch2e.mi_suma)

# Importar módulos sin utilizar Namespaces
from chapter2.elements import mi_suma
print (mi_suma)

# Es posible también, importar más de un elemento en la misma instrucción. Para ello, cada elemento irá separado por una coma (,) y un espacio en blanco.
# Pero ¿qué sucede si los elementos importados desde módulos diferentes tienen los mismos nombres? En estos casos, habrá que prevenir fallos, utilizando alias para los elementos.
from chapter2.elements import mi_variable as mv, mi_lista as ml
print (mv)
print (ml)

# IMPORTACIÓN

# La importación de módulos debe realizarse al comienzo del documento, en orden alfabético de paquetes y módulos.
# Primero deben importarse los módulos propios de Python. Luego, los módulos de terceros y finalmente, los módulos propios de la aplicación.
# Entre cada bloque de imports, debe dejarse una línea en blanco.

