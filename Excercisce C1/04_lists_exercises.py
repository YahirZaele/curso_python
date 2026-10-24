# ==============================================================================
# EJERCICIOS DE PYTHON: LISTAS (LISTS)
# ==============================================================================

# 1. Crea una lista con 5 nombres de frutas diferentes.
#    Luego, imprime el primer elemento usando un índice positivo 
#    y el último elemento usando un índice negativo.

print("Ejercicio 1: ")
fruits = ["apple","banna","naranja","cherry","sandia"]
print(f"Primer elemento: {fruits[0]}")
print(f"Ultimo elemnto: {fruits[-1]}")

# 2. A partir de la lista de frutas anterior, cambia el segundo elemento por otra fruta diferente.
#    Imprime la lista completa para verificar la modificación.

print("Ejercicio 2: ")
print(fruits)
fruits[1]= "melon"
print(fruits)

# 3. Crea una lista vacía llamada "numeros".
#    - Agrega el número 10 al final usando append().
#    - Inserta el número 5 al principio (índice 0) usando insert().
#    - Imprime la lista resultante.

print("Ejercicio 3: ")
numeros = []
numeros.append(10)
numeros.insert(0,5)
print(numeros)

# 4. Dada la siguiente lista: colores = ["rojo", "verde", "azul", "amarillo", "verde"]
#    - Elimina la primera aparición de "verde" usando remove().
#    - Elimina el último elemento de la lista usando pop() y guárdalo en una variable.
#    - Imprime el elemento eliminado y la lista final.

print("Ejercicio 4: ")
colores = ["rojo", "verde", "azul", "amarillo", "verde"]
print(colores)
colores.remove("verde")
print(colores)
variable = colores.pop() #ya que me pides el ultimo puedo ponerlo sin valor, ya que pop() toma el ultimo de la lista
print(variable)
print(colores)

# 5. Dada la lista: valores = [1, 2, 2, 3, 4, 2, 5, 2]
#    - Imprime la longitud total de la lista usando len().
#    - Cuenta cuántas veces se repite el número 2 usando count() e imprime el resultado.

print("Ejercicio 5")
valores = [1,2,2,3,4,2,5,2]
print(len(valores))
print(valores.count(2))

# 6. Dada la lista: letras = ["a", "b", "c", "d", "e", "f", "g"]
#    - Extrae usando slicing una sublista con los elementos desde el índice 2 hasta el 5 inclusive ("c", "d", "e", "f").
#    - Imprime la sublista resultante.

print("Ejercicio 6: ")
letras = ["a","b","c","d","e","f","g"]
print(f"Lista original: {letras}")
print(f"Sublista: {letras[2:6]}")


# 7. Crea una lista con 4 nombres de ciudades:
#    - Usa el operador 'in' para verificar si una ciudad (por ejemplo "Tokio") está en la lista e imprime el resultado (True/False).
#    - Encuentra e imprime la posición (índice) de otra ciudad que sí esté en tu lista usando index().

print("Ejercicio 7: ")
ciudades = ["Mexico", "Argentina", "Colombia", "Peru"]
print(ciudades)
posicion = ciudades.index("Argentina")
print(f"Tokio esta en la lista de ciudades?: { 'Tokio' in ciudades}")
print(f"Solo esta en la lista Paises de Latinoameria por ejemplo: {ciudades[1]}")
print(f"El cual su indice en la lista es: {posicion}")
# 8. Dadas las siguientes listas:
#    lista_a = [1, 2, 3]
#    lista_b = [4, 5, 6]
#    - Concaténalas en una nueva variable lista_c usando el operador '+'.
#    - Crea otra lista que repita 3 veces los elementos de lista_a usando el operador '*'.
#    - Imprime ambas listas.

print("Ejercicio 8: ")
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c)
lista3 = lista_a * 3
print(lista3)

# 9. Dada la lista: edades = [34, 12, 65, 23, 8, 45]
#    - Ordénala de menor a mayor usando sort() e imprímela.
#    - Luego, inviértela para que quede de mayor a menor e imprímela.

print("Ejercicio 9: ")
edades = [34, 12, 65, 23, 8, 45]
print(f"Lista original: {edades}")
edades.sort()
print(f"Lista ordenada: {edades}")
edades.reverse()
print(f"Lista invertida: {edades}")


# 10. Crea una lista con 3 elementos: animales = ["perro", "gato", "loro"]
#     - Desempaqueta sus elementos en 3 variables individuales (a1, a2, a3) e imprímelas.
#     - Crea una copia independiente de la lista usando el método copy() y guárdala en copia_animales.
#     - Agrega un nuevo animal solo a la copia e imprime ambas listas para comprobar que la original no cambió.

print("Ejercicio 10:")
animales = ["perro", "gato", "loro"]
print(f"Lista original: {animales}")
a1 = animales[0]
a2 = animales[1]
a3 = animales[2]
print(f"Animal 1: {a1}, Animal 2: {a2}, Animal 3: {a3}")
animales_copia = animales.copy()
animales_copia.append("pato")
print(f"Lista original: {animales}")
print(f"Copia: {animales_copia}")