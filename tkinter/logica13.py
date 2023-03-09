import random
import string

class password:
    def generar_contrasena(longitud=8):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
        return contrasena

    # Pedir al usuario la longitud de la contraseña
    longitud = input("Ingresa la longitud de la contraseña: ")

    # Verificar que la longitud es un entero positivo
    if longitud.isdigit() and int(longitud) > 0:
        contrasena = generar_contrasena(int(longitud))
    else:
        contrasena = generar_contrasena()
    print("La contraseña generada es:", contrasena)
