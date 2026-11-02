# ==============================================================================
# EJERCICIOS DE PYTHON: DICCIONARIOS (DICTS) - 10 EJERCICIOS (DÍA 8)
# ==============================================================================

# 1. Creación básica y agregar elementos:
#    - Crea un diccionario vacío llamado 'perro'.
#    - Añade las claves: 'nombre', 'color', 'raza', 'patas' y 'edad' con sus respectivos valores.
#    - Imprime el diccionario resultante.

print("Ejercicio 1:")
# Tu código aquí:
perro = {}
perro['nombre'] = 'oso'
perro['color'] = 'negro con blanco'
perro['raza'] = 'Pitbull'
perro['patas'] = 4
perro['edad'] = "3 años"
print(perro)
print(type(perro))
# 2. Diccionario con múltiples tipos de datos:
#    - Crea un diccionario llamado 'estudiante' con los siguientes datos:
#      'nombre', 'apellido', 'genero', 'edad', 'estado_civil',
#      'habilidades' (debe ser una lista con al menos 2 habilidades),
#      'pais', 'ciudad' y 'direccion'.
#    - Imprime el diccionario.

print("\nEjercicio 2:")
# Tu código aquí:
estudiante = {
    'nombre' : 'Yahir',
    'apellido' : 'Medina',
    'genero' : 'Hombre',
    'edad' : 24,
    'estado_civil' : 'soltero',
    'habilidades' : ['Phyton', 'SQL', 'HTML'],
    'pais' : 'Mexico',
    'ciudad' : 'CDMX',
    'direccion' : 'Cuahutemoc'
}
print(type(estudiante))
print(estudiante)

# 3. Longitud y acceso a valores:
#    - Obtén e imprime la longitud del diccionario 'estudiante' usando len().
#    - Accede al valor de la clave 'habilidades' e imprime su tipo de dato usando type().

print("\nEjercicio 3:")
# Tu código aquí:
len_estudiante = len(estudiante)
print(len_estudiante)
habilidades = estudiante.get('habilidades')
print(type(habilidades))

# 4. Modificar valores existentes:
#    - Modifica la lista de 'habilidades' del diccionario 'estudiante' agregando una o dos nuevas habilidades
#      (por ejemplo: 'Git' y 'SQL') usando append() o extend().
#    - Imprime la lista de habilidades actualizada.

print("\nEjercicio 4:")
# Tu código aquí:
estudiante['habilidades'].extend(['Git', 'Java'])
print(estudiante['habilidades'])

# 5. Acceso seguro con get() vs corchetes []:
#    - Intenta acceder a una clave inexistente (por ejemplo, 'telefono') usando corchetes dentro de un bloque try-except para capturar KeyError.
#    - Luego, accede a esa misma clave usando el método get() pasando un valor por defecto ('No registrado').
#    - Explica en un comentario la diferencia entre ambos métodos.

print("\nEjercicio 5:")
# Tu código aquí:
try:
    print(estudiante['telefono'])
except: 
    print("El diccionario 'estudiante' no tiene clave para 'telefono'")
telefono = estudiante.get('telefono', 'No registrado')
print('telefono:', telefono)

# 6. Obtener claves y valores como listas:
#    - Obtén todas las claves del diccionario 'estudiante' como una lista usando keys() y list().
#    - Obtén todos los valores del diccionario como una lista usando values() y list().
#    - Imprime ambas listas.

print("\nEjercicio 6:")
# Tu código aquí:
lista_keys = list(estudiante.keys())
lista_values = list(estudiante.values())
print(lista_keys)
print(lista_values)

# 7. Pares clave-valor con items() y recorrido con bucle for:
#    - Convierte el diccionario 'estudiante' a una lista de tuplas usando items().
#    - Recorre el diccionario usando un bucle for (desempaquetando clave y valor)
#      e imprime cada pareja con el formato: "Campo: <clave> -> Valor: <valor>".

print("\nEjercicio 7:")
# Tu código aquí:
lista_items = estudiante.items()
print(lista_items)

for clave, valor in estudiante.items():
    print(f'Campo: {clave} -> Valor: {valor}')

# 8. Eliminar elementos (pop, popitem y del):
#    - Elimina la clave 'estado_civil' usando pop() y guarda el valor eliminado en una variable.
#    - Elimina el último elemento agregado al diccionario usando popitem().
#    - Elimina la clave 'pais' usando la palabra clave 'del'.
#    - Imprime el valor eliminado con pop() y el diccionario resultante tras las tres eliminaciones.

print("\nEjercicio 8:")
# Tu código aquí:
estado_civil = estudiante.pop('estado_civil')
print(estado_civil)
ultimo_elm = estudiante.popitem()
print(ultimo_elm)
del estudiante['pais']
print(estudiante)

# 9. Actualización y fusión de diccionarios (update):
#    - Crea un diccionario nuevo con información de contacto:
#      info_contacto = {'email': 'tu_correo@example.com', 'telefono': '+52 333-1234567'}
#    - Actualiza el diccionario 'estudiante' con 'info_contacto' usando el método update().
#    - Imprime el diccionario 'estudiante' actualizado.

print("\nEjercicio 9:")
# Tu código aquí:
info_contacto = {
    'email' : 'test@hotmail.com',
    'telefono' : '+525514556509'
}

estudiante.update(info_contacto)
print(estudiante)

# 10. Conteo de frecuencias (Caso práctico):
#     - Dada la siguiente oración:
#       frase = "manzana pera manzana platano pera manzana naranja fresa pera"
#     - Divide la frase en una lista de palabras con split().
#     - Usa un diccionario para contar cuántas veces aparece cada fruta.
#     - Imprime el diccionario de frecuencias resultante.

print("\nEjercicio 10:")
frase = "manzana pera manzana platano pera manzana naranja fresa pera"
# Tu código aquí:
conteo = {}
for palabra in frase.split() :
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)
