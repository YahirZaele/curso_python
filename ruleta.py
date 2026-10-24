import random
import string
import time
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def girar_ruleta():
    # Abecedario en español (incluyendo la Ñ)
    letras = list(string.ascii_uppercase)
    letras.insert(14, 'Ñ')

    input("\nPresiona [Enter] para girar la ruleta...")

    # Animación de giro
    giros = random.randint(25, 40)
    velocidad = 0.05

    for i in range(giros):
        limpiar_pantalla()
        letra_actual = random.choice(letras)
        
        print("=" * 30)
        print("       RULETA DE LETRAS       ")
        print("=" * 30)
        print(f"\n            [ {letra_actual} ]\n")
        print("=" * 30)
        
        # Incremento progresivo para simular desaceleración
        velocidad += 0.015
        time.sleep(velocidad)

    # Letra ganadora final
    limpiar_pantalla()
    print("=" * 30)
    print("       RESULTADO FINAL        ")
    print("=" * 30)
    print(f"\n      >>> Letra: [ {letra_actual} ] <<<\n")
    print("=" * 30)

if __name__ == "__main__":
    while True:
        girar_ruleta()
        repetir = input("\n¿Girar otra vez? (s/n): ").strip().lower()
        if repetir != 's':
            print("\n¡Gracias por jugar!\n")
            break
