# 1. Realiza las siguientes operaciones aritmÃ©ticas:
# â€¢	Suma: 15 + 25
# â€¢	Resta: 50 - 22
# â€¢	MultiplicaciÃ³n: 8 * 7
# â€¢	DivisiÃ³n: 100 / 20
suma = 15 + 25
resta = 50 - 22
multiplicacion = 8 * 7
division = 100/20
print(f"Ejercicio 1\n{suma}\n{resta}\n{multiplicacion}\n{division}")

# 2. Calcula el resto de la divisiÃ³n de 37 entre 5 y almacÃ©nalo en una variable remainder. Luego imprÃ­melo.

a = 37 
b = 5
remainder = a % b
print("Ejercicio 2\n" + str(remainder))

# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase â€œ es mi nÃºmero favoritoâ€ . Imprime el resultado.

a = 7
numero = str(a)
frase = " es mi numero favorito"
print("Ejercicio 3\n" + numero + frase)

# 4. Repite la palabra â€œPythonâ€  10 veces usando el operador de multiplicaciÃ³n para cadenas y luego imprÃ­mela.

palabra = 'Python '
m_cadenas = palabra * 10
print("Ejercicio 4\n" + m_cadenas)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.

a = 12
b = 8
resultado = a > b
print("Ejercicio 5\n" + str(resultado))

# 6. Compara dos cadenas de texto (â€œappleâ€  y â€œbananaâ€ ) usando los operadores > y < y explica cuÃ¡l tiene mayor orden alfabÃ©tico.

cadena1 = "apple"
cadena2 = "banana"
comparacion1 = cadena1 > cadena2
comparacion2 = cadena1 < cadena2
print("Ejercicio 6\n" + str(comparacion1) + "\n" + str(comparacion2))
print("En python los caractesres se comparan segun su valor de ASCII/Unicode. Como 'b'(ASCII 98) tiene un valor mayor que 'a'(ASCII 97), 'banana' es mayor que 'apple'")

# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 10 es mayor que 5 y menor que 20. Imprime el resultado.

numero1 = 10
numero2 = 5
numero3 = 20
comparacion =  (numero1 > numero2) and (numero1 <numero3)
print("Ejercicio 7\n" + str(comparacion))

# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.

numero1 = 7
numero2 = 3
numero3 = 5
comparacion = (numero1 < numero2) or (numero1 > numero3)
print("Ejercicio 8\n" + str(comparacion))

# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?

comparacion = 15 > 20
resultado = comparacion
print("Ejercicio 9\n" + "15 > 20 es: " + str(resultado))
comparacion_opuesta = not comparacion
print("El opuesto de 15 > 20 es: " + str(comparacion_opuesta))

# 10. Combina operadores aritmÃ©ticos y lÃ³gicos: Verifica si el nÃºmero resultante de la expresiÃ³n (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.

expresion = (5 * 3) + 2
expresionFinal = (expresion > 10) and (expresion < 20)
print("Ejercicio 10\n" + "(5 * 3) + 2 es mayor que 10 y menor que 20: " + str(expresionFinal))

print(10 % 3 + 4 ** 2)