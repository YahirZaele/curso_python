# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€  y luego imprime la longitud de la cadena usando len().

print("Ejercio 1: ")
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: â€œHolaâ€  y â€œPythonâ€ , y muestra el resultado en una sola lÃ­nea.

print("Ejercio 2: ")
texto1 = "Hola"
texto2 = "Python"
print(texto1 + " " + texto2)

# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.

print("Ejercio 3: ")
texto1 = "Hola como estas? \n Estoy aprediendo Python"
print(texto1)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

print("Ejercio 4: ")
nombre = "Yahir"
apellido = "Medina"
edad = 24
print(f"Hola son {nombre} {apellido} y tengo {edad}")

# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€  en variables separadas y luego imprÃ­melos uno por uno.

print("Ejercio 5: ")
python = "python"
p1,p2,p3,p4,p5,p6=python
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)

# 6. Extrae un â€œsliceâ€  de la palabra â€œProgramaciÃ³nâ€  para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.

print("Ejercio 6: ")
Programacion = "Programacion"
print(Programacion[3:8])

# 7. Invierte la cadena â€œPythonâ€  usando slicing y muestra el resultado.

print("Ejercio 7: ")

cadena = "Python"
print(cadena[:: -1])

# 8. Convierte la cadena â€œaprendiendo pythonâ€  en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.

print("Ejercio 8: ")
cadena = "aprendiendo python"
print(cadena.upper())

# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€  en la cadena â€œProgramaciÃ³n en Pythonâ€ .

print("Ejercio 9: ")
cadena = "Programando en Python"
print(cadena.count("n"))

# 10. Verifica si la cadena â€œ12345â€  es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.

print("Ejercio 10: ")
cadena = "12345"
print(cadena.isnumeric())
