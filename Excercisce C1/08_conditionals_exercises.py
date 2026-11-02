# ==============================================================================
# EJERCICIOS DE PYTHON: CONDICIONALES (CONDITIONALS) - 10 EJERCICIOS (DÍA 9)
# Basado en: 30-Days-Of-Python (Day 9 - Conditionals)
# ==============================================================================

# ------------------------------------------------------------------------------
# NIVEL 1
# ------------------------------------------------------------------------------

# 1. Obtener la edad del usuario con input("Introduce tu edad: ").
#    - Si el usuario tiene 18 años o más, muestra: "Tienes la edad suficiente para aprender a conducir."
#    - Si es menor de 18, muestra cuántos años le faltan para cumplir 18.
#    Ejemplo:
#      Introduce tu edad: 30 -> Tienes la edad suficiente para aprender a conducir.
#      Introduce tu edad: 15 -> Te faltan 3 años para poder aprender a conducir.

print("Ejercicio 1:")
# Tu código aquí:
edad = 15

if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    calculo_edad = 18 - edad
    print(f"tu edad es de {edad} te faltan {calculo_edad} para poder conducir")

# 2. Compara los valores de 'mi_edad' y 'tu_edad' usando if ... else.
#    - ¿Quién es mayor (tú o yo)?
#    - Pide la edad con input("Introduce tu edad: ").
#    - Usa condiciones anidadas para imprimir "año" si la diferencia es de 1 año,
#      o "años" si la diferencia es mayor.
#    - Si tienen la misma edad, muestra un mensaje adecuado.
#    Ejemplo:
#      Introduce tu edad: 30 -> Eres 5 años mayor que yo.

print("\nEjercicio 2:")
# Tu código aquí:
mi_edad = 25
tu_edad = input("Introduce tu edad: ")

calculo_edad = mi_edad - int(tu_edad)

if mi_edad and tu_edad:
    print(f"Tenemos {calculo_edad} años de diferencia")

# 3. Obtén dos números del usuario mediante input.
#    - Si 'a' es mayor que 'b', muestra: "a es mayor que b".
#    - Si 'a' es menor que 'b', muestra: "a es menor que b".
#    - De lo contrario, muestra: "a es igual a b".
#    Ejemplo:
#      Introduce el primer número: 4
#      Introduce el segundo número: 3
#      4 es mayor que 3.

print("\nEjercicio 3:")
# Tu código aquí:
a = int(input("Introduce un valor: "))
b = int(input("Introduce un valor: "))

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else: 
    print("a es igual a b")

# ------------------------------------------------------------------------------
# NIVEL 2
# ------------------------------------------------------------------------------

# 4. Escribe un programa que asigne calificaciones a estudiantes según sus puntuaciones:
#    - 80 - 100: A
#    - 70 - 79:  B (o 70-89 según criterio del reto)
#    - 60 - 69:  C
#    - 50 - 59:  D
#    - 0  - 49:  F

print("\nEjercicio 4:")
# Tu código aquí:
calf = 49

if calf >= 80:
    print("Tu calificaion es A")
elif calf >= 70:
    print("Tu calificacion es B")
elif calf >= 60:
    print("Tu calificacion es C")
elif calf >= 50:
    print("Tu calificacion es D")
else:
    print("Tu calificacion es F")



# 5. Determina la estación del año según el mes introducido por el usuario:
#    - Septiembre, Octubre o Noviembre  -> La estación es Otoño (Autumn).
#    - Diciembre, Enero o Febrero      -> La estación es Invierno (Winter).
#    - Marzo, Abril o Mayo             -> La estación es Primavera (Spring).
#    - Junio, Julio o Agosto           -> La estación es Verano (Summer).

print("\nEjercicio 5:")
# Tu código aquí:
mes = input("Introduce el mes en numero para saber en que estacion del años estas: ")
autumn = {'9' : 'Sep','10' : 'Oct', '11' :'Nov'}
winter = {'12' : 'Dic', '1' : 'Ene', '2' : 'Feb'}
spring = {'3' : 'Mar', '4' : 'Abr','5' : 'May'}
summer = {'6' : 'Jun','7' : 'Jul','8' : 'Ago'}

if mes in autumn:
    print("Estamos en Otoño")
elif mes in winter:
    print("Estamos en Invierno")
elif mes in spring:
    print("Estamos en Primavera")
elif mes in summer:
    print("Estamos en Verano")


# 6. Dada la siguiente lista de frutas:
#    frutas = ['banana', 'orange', 'mango', 'lemon']
#    - Pide al usuario que ingrese una fruta.
#    - Si la fruta no existe en la lista, agrégala y muestra la lista modificada.
#    - Si la fruta ya existe, muestra: "Esa fruta ya existe en la lista".

print("\nEjercicio 6:")
frutas = ['banana', 'orange', 'mango', 'lemon']
# Tu código aquí:
fruta = input("Escoge una fruta: \n")

if fruta in frutas:
    print(f'Esa fruta ya existe en la lista:\n{frutas}')
else:
    frutas.append(fruta)
    print(f'Fruta agregada:\n{frutas}')

# ------------------------------------------------------------------------------
# NIVEL 3
# ------------------------------------------------------------------------------

# Para los siguientes ejercicios usaremos este diccionario 'persona':
persona = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 7. Comprueba si el diccionario 'persona' tiene la clave 'skills'.
#    - Si existe, imprime la habilidad que está en el medio de la lista de habilidades.

print("\nEjercicio 7:")
# Tu código aquí:
if 'skills' in persona:
    print("si existe skills en el directorio persona")


# 8. Comprueba si el diccionario 'persona' tiene la clave 'skills'.
#    - Si existe, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.

print("\nEjercicio 8:")
# Tu código aquí:
if 'skills' in persona:
    if 'Python' in persona['skills']:
        print("La persona sí tiene la habilidad de Python.")
    else:
        print("La persona no tiene la habilidad de Python.")

# 9. Determina el rol del desarrollador según sus habilidades:
#    - Si sus habilidades son solo 'JavaScript' y 'React', muestra: "Es un desarrollador frontend".
#    - Si sus habilidades incluyen 'Node', 'Python' y 'MongoDB', muestra: "Es un desarrollador backend".
#    - Si sus habilidades incluyen 'React', 'Node' y 'MongoDB', muestra: "Es un desarrollador fullstack".
#    - En cualquier otro caso, muestra: "Título desconocido".

print("\nEjercicio 9:")
# Tu código aquí:
skills = persona.get('skills', [])

if skills == ['JavaScript', 'React']:
    print("Es un desarrollador frontend")
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("Es un desarrollador backend")
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("Es un desarrollador fullstack")
else:
    print("Título desconocido")


# 10. Si la persona está casada y vive en Finlandia:
#     - Imprime la información con el siguiente formato:
#       "Asabeneh Yetayeh lives in Finland. He is married." (o en español si prefieres).

if persona['is_married'] and persona['country'] == 'Finland':
    print(f"{persona['first_name']} {persona['last_name']} lives in {persona['country']}. He is married.")