print("¡Hola Mundo!")
# Este codigo imprime un texto que dice "¡Hola Mundo!"

print("Yahir Zaele, 23 años")

print("Yahir")
print(23)
print(1.75)

print(type("Yahir"))
print(type(23))
print(type(1.75))

"""
En python los tipos de datos 
- string = que es un texto o una cadena de textos
- int = son numeros enteros
- float = son numeros con decimales
- bool = son valores Verdaderas o Falsas 
- complex = son numeros con parte imaginaria "1+1j"
"""

print("HOLA" + "MUNDO")

A = "Yahir Zaele Medina"
B = 23

print(A, B)

#Solicitar un valor al usuario
name = input("ingresa tu nombre: ")
print(name + " BIENVENIDO AL MUNDO DE PYTHON")


a = 10 #Aqui declaro el primer valor
b = 20 #Aqui declaro el segundo valor
print(a + b) #Imprimo el resultado de la suma de a y b
print(type(a + b)) #Imprimo el tipo de dato de la suma de a y b



edad = 20
tiene_credenciales = True

mayor = edad >= 18 and tiene_credenciales
print(mayor)
