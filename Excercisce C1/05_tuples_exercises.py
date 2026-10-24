# ==============================================================================
# EJERCICIOS DE PYTHON: TUPLAS (TUPLES)
# ==============================================================================

# 1. Crea una tupla llamada "colores" con 5 colores diferentes.
#    - Imprime el primer elemento usando un índice positivo.
#    - Imprime el último elemento usando un índice negativo.
#    - Crea una tupla de un solo elemento (recuerda la coma al final) e imprime su tipo usando type().

print("Ejercicio 1:")
colores = ('verde', 'azul','rojo','naranja', 'amarillo')
print(colores[0])
print(colores[-1])
print(type(colores))
color = ('verde',)
print(type(color))

# 2. Dada la tupla: numeros = (10, 20, 30, 40)
#    - Intenta cambiar el valor del índice 1 a 25 dentro de un bloque try-except (o coméntalo).
#    - Explica en un comentario por qué se genera un TypeError y qué significa que las tuplas sean inmutables.

print("\nEjercicio 2:")
numeros = (10, 20, 30, 40)
try: 
    numeros[1] = 25
except TypeError:
    print(TypeError)
# las tuplas solo se pueden modificar si las convertimos a listas, las Tuplas son ideales para mantener seguros los valores.

# 3. Dadas las siguientes tuplas:
#    tupla_a = (1, 2, 3)
#    tupla_b = (4, 5, 6)
#    - Únelas en una nueva tupla llamada "tupla_c" usando el operador '+'.
#    - Crea otra tupla llamada "tupla_d" que repita "tupla_a" 3 veces usando el operador '*'.
#    - Imprime ambas tuplas resultantes.

print("\nEjercicio 3:")
tupla_a = (1, 2, 3)
tupla_b = (4, 5, 6)
tupla_c = tupla_a + tupla_b
print(tupla_c)
tupla_d = tupla_a * 3
print(tupla_d)

# 4. Dada la tupla: notas = (8, 9, 10, 7, 8, 10, 6, 8)
#    - Cuenta cuántas veces aparece la nota 8 usando count() e imprime el resultado.
#    - Encuentra e imprime el índice de la primera aparición de la nota 10 usando index().

print("\nEjercicio 4:")
notas = (8, 9, 10, 7, 8, 10, 6, 8)
print(notas.count(8))
print(notas.index(10))

# 5. Dada la tupla: dias = ("lunes", "martes", "miércoles")
#    - Conviértela a lista usando list() para poder modificarla.
#    - Agrega "jueves" y "viernes" a la lista.
#    - Vuelve a convertir la lista en una tupla usando tuple().
#    - Imprime la tupla final resultante.

print("\nEjercicio 5:")
dias = ("lunes", "martes", "miercoles")
print(dias)
list_dias = list(dias)
list_dias.append("jueves")
list_dias.append("viernes")
dias = tuple(list_dias)
print(dias)


# 6. Dada la tupla: alfabeto = ("a", "b", "c", "d", "e", "f", "g", "h")
#    - Extrae usando slicing los elementos desde el índice 2 hasta el 5 inclusive ("c", "d", "e", "f").
#    - Extrae los primeros 3 elementos.
#    - Extrae los últimos 2 elementos usando índices negativos.
#    - Imprime cada una de las subtuplas resultantes.

print("\nEjercicio 6:")
alfabeto = ("a", "b", "c", "d", "e", "f", "g", "h")
print(alfabeto[2:6])
print(alfabeto[0:3])
print(alfabeto[-2:])

# 7. Crea una tupla con 4 nombres de países:
#    - Usa el operador 'in' para verificar si un país (por ejemplo "Japón") está en la tupla (True/False).
#    - Verifica si otro país que sí esté en tu tupla existe usando 'in'.
#    - Imprime la cantidad total de elementos usando len().

print("\nEjercicio 7:")
paises = ('Mexico', 'Canada', 'Estados Unidos', 'Japon')
print('Japon' in paises)    
print('Argentina' in paises)
print(len(paises))

# 8. Dada la tupla: coordenadas = (19.4326, -99.1332, 2240)  # latitud, longitud, altitud
#    - Desempaqueta sus valores en 3 variables individuales: latitud, longitud y altitud.
#    - Imprime cada variable en un f-string con un mensaje claro.

print("\nEjercicio 8:")
coordenadas = (19.4326, -99.1332, 2240)
latitud, longitud, altitud = coordenadas
print(f"La latitud es {latitud}")
print(f"La longitud es {longitud}")
print(f"La altitud es {altitud}")

# 9. Dada la siguiente tupla anidada:
#    matriz = (
#        (1, 2, 3),
#        (4, 5, 6),
#        (7, 8, 9)
#    )
#    - Imprime la segunda fila completa.
#    - Accede e imprime el número 6 (fila 2, columna 3).
#    - Accede e imprime el número 7 (fila 3, columna 1).

print("\nEjercicio 9:")
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)
print(matriz[1])
print(matriz[1][2])
print(matriz[2][0])

# 10. Dada la tupla de precios: precios = (120, 45, 300, 89, 15, 650)
#     - Encuentra e imprime el precio más alto usando max().
#     - Encuentra e imprime el precio más bajo usando min().
#     - Calcula e imprime la suma total de los precios usando sum().
#     - Usa sorted() para ordenar los precios de menor a mayor e imprime el resultado (nota qué tipo de dato retorna).

print("\nEjercicio 10:")
precios = (120, 45, 300, 89, 15, 650)
print(max(precios))
print(min(precios))
print(sum(precios))
resutado_ordenado = sorted(precios)
print(resutado_ordenado)
print(type(resutado_ordenado))    
