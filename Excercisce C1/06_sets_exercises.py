# ==============================================================================
# EJERCICIOS DE PYTHON: CONJUNTOS (SETS) - 10 EJERCICIOS (DÍA 7)
# ==============================================================================

# Datos iniciales del Día 7:
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Longitud y adición simple:
#    - Encuentra e imprime la longitud del conjunto it_companies usando len().
#    - Agrega 'Twitter' a it_companies usando el método add() e imprime el conjunto.
print("Ejercicio 1:")
print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)

# 2. Inserción múltiple:
#    - Agrega varias empresas a la vez (por ejemplo: 'Tesla', 'Intel', 'Spotify')
#      al conjunto it_companies usando update().
#    - Imprime el conjunto resultante.

print("\nEjercicio 2:")
it_companies.update(['Tesla', 'Nvidia', 'Intel'])
print(it_companies)

# 3. Eliminar elementos (remove vs discard):
#    - Elimina una empresa de it_companies usando remove().
#    - En un comentario explica qué diferencia hay entre remove() y discard()
#      si intentas borrar un elemento que no existe.

print("\nEjercicio 3:")
it_companies.remove('Apple')
print(it_companies)
# la difrencias de remove() es que al querer eliminar un elemento que no existe este mandara un error si no lo encuetra el cual es nombrado como KeyError
# la diferencia de discard() no manda error si no existe, de cierta manera lo convierte en algo un poco mas seguro, y no rompera el codigo

# 4. Unión de conjuntos:
#    - Une los conjuntos A y B usando union() o el operador | y guarda el resultado en una variable.
#    - Imprime el conjunto resultante.

print("\nEjercicio 4:")
sumaDeConjuntos = A.union(B)
print(sumaDeConjuntos)

# 5. Intersección de conjuntos:
#    - Encuentra los elementos que están presentes tanto en A como en B
#      usando intersection() o el operador &.
#    - Imprime el resultado.

print("\nEjercicio 5:")
interseccionesAB = A&B
print(interseccionesAB)

# 6. Diferencia de conjuntos:
#    - Encuentra los elementos que están en A pero NO en B usando difference() o el operador -.
#    - Encuentra los que están en B pero NO en A.
#    - Imprime ambos resultados.

print("\nEjercicio 6:")
differenceAB = A-B
print(differenceAB)
differenceBA = B-A
print(differenceBA)

# 7. Subconjuntos y superconjuntos:
#    - Comprueba si A es un subconjunto de B usando issubset() (True/False).
#    - Comprueba si B es un superconjunto de A usando issuperset() (True/False).
#    - Imprime ambos resultados.

print("\nEjercicio 7:")
subconjuntoAb = A.issubset(B)
print(f"A es un subcojunto de B : {subconjuntoAb}")
subconjuntoBa = B.issuperset(A)
print(f"B es un subconjuto de A: {subconjuntoBa}")

# 8. Conjuntos disjuntos y diferencia simétrica:
#    - Verifica si A y B son conjuntos disjuntos usando isdisjoint().
#    - Encuentra la diferencia simétrica entre A y B usando symmetric_difference() o el operador ^.
#    - Imprime ambos resultados.

print("\nEjercicio 8:")
disjuntosAb = A.isdisjoint(B)
print(disjuntosAb)
dif_simetricaAB = A.symmetric_difference(B)
print(dif_simetricaAB)

# 9. Conversión y eliminación de duplicados:
#    - Convierte la lista 'age' a un conjunto usando set() y guárdala en una variable.
#    - Imprime la longitud de la lista original y la longitud del conjunto usando len().
#    - Explica brevemente en un comentario por qué cambian de tamaño.

print("\nEjercicio 9:")
ages = set(age)
print(len(age))
print(len(ages))
# las listas aceptan variables repetidas sin problema, pero los set no, no se puede repetir ninguna variable

# 10. Contar palabras únicas en un texto:
#     - Dada la siguiente oración:
#       "I am a teacher and I love to inspire and teach people."
#     - Usa split() para separar las palabras en una lista.
#     - Convierte la lista en un set para eliminar las palabras repetidas.
#     - Imprime la cantidad de palabras únicas con len() y el conjunto resultante.

print("\nEjercicio 10:")
frase = "I am a teacher and I love to inspire and teach people."
en_palabras = list(frase.split())
print(en_palabras)
en_set = set(en_palabras)
print(len(en_set))
