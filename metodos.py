import string

def main():

    while True:
        f = input("Seleccione una opcion: \n"
              "1: Cifrado de Cesar\n"
              "2: Cifrado de Vigenere\n\n")
        try:
            f = int(f)
            if f < 1 or f > 2:
                print("Inserte una opcion valida.\n")
            else:
                break
        except ValueError:
            print("Inserte una opcion valida.\n")

    cifrados = {
        1: cesar,
        2: vigenere
    }
        
    cifrado_elegido = cifrados[f]
    cifrado_elegido()


def alfabeto_ingles(x):

    return x in string.ascii_letters


def cesar():

    while True:
        f = input("Seleccione una opcion: \n"
              "1: Encriptacion\n"
              "2: Desencriptacion\n\n")
        try:
            f = int(f)
            if f < 1 or f > 2:
                print("Inserte una opcion valida.\n")
            else:
                break
        except ValueError:
            print("Inserte una opcion valida.\n")

    while True:
        try:
            texto = str(input("Ingresa el texto (debe contener al menos un caracter alfabetico): "))
            if(isinstance(texto, str) and any(alfabeto_ingles(i) for i in texto)):
                break
        except:
            print("El input recibido debe ser un string.")

    while True:
        try:
            n = int(input("Ingresa el numero de orden a afectar cada letra: "))
            if(isinstance(n, int)):
                break
        except:
            print("El input recibido debe ser un numero entero.")

    opciones = {
        1: cesar_encriptacion,
        2: cesar_desencriptacion,
    }

    opcion_elegida = opciones[f]
    opcion_elegida(texto, n)


def vigenere():

    while True:
        f = input("Seleccione una opcion: \n"
              "1: Encriptacion\n"
              "2: Desencriptacion\n\n")
        try:
            f = int(f)
            if f < 1 or f > 2:
                print("Inserte una opcion valida.\n")
            else:
                break
        except ValueError:
            print("Inserte una opcion valida.\n")

    while True:
        try:
            texto = str(input("Ingresa el texto (debe contener al menos un caracter alfabetico): "))
            if(isinstance(texto, str) and any(alfabeto_ingles(i) for i in texto)):
                break
        except:
            print("El input recibido debe ser un string.")

    while True:
        try:
            clave = str(input("Ingresa la clave (solamente pueden ser caracteres alfabeticos sin espacios): "))
            if(isinstance(clave, str) and all(alfabeto_ingles(i) for i in clave) and any(alfabeto_ingles(i) for i in clave)):
                break
        except:
            print("El input recibido debe ser un string.")

    opciones = {
        1: vigenere_encriptacion,
        2: vigenere_desencriptacion,
    }

    opcion_elegida = opciones[f]
    opcion_elegida(texto, clave)

def cesar_encriptacion(a, b):
    texto_encriptado = []
    b = b % 26
    for i in range(len(a)):
        caracter = a[i]
        if alfabeto_ingles(caracter):
            if caracter.isupper():
                caracter_encriptado = chr((ord(caracter) + b - ord('A')) % 26 + ord('A'))
            else:
                caracter_encriptado = chr((ord(caracter) + b - ord('a')) % 26 + ord('a'))
        else:
            caracter_encriptado = caracter
        texto_encriptado.append(caracter_encriptado)
    texto_encriptado = "".join(texto_encriptado)
    print(f"Mensaje: {a}\nMensaje encriptado: {texto_encriptado}")
    repeticion()

def cesar_desencriptacion(a, b):
    texto_desencriptado = []
    b = b % 26
    for i in range(len(a)):
        caracter = a[i]
        if alfabeto_ingles(caracter):
            if caracter.isupper():
                caracter_desencriptado = chr((ord(caracter) - b - ord('A')) % 26 + ord('A'))
            else:
                caracter_desencriptado = chr((ord(caracter) - b - ord('a')) % 26 + ord('a'))
        else:
            caracter_desencriptado = caracter
        texto_desencriptado.append(caracter_desencriptado)
    texto_desencriptado = "".join(texto_desencriptado)
    print(f"Mensaje encriptado: {a}\nMensaje: {texto_desencriptado}")
    repeticion()

def vigenere_encriptacion(a, b):
    texto_encriptado = []
    b = list(b)
    if len(a) == len(b):
        return b
    else:
        for i in range(len(a) - len(b)):
            b.append(b[i % len(b)])
    b = "".join(b)
    b = b.upper()

    for i in range(len(a)):
        caracter = a[i]
        if alfabeto_ingles(caracter):
            if caracter.isupper():
                caracter_encriptado = chr((ord(caracter) + ord(b[i]) - (2*ord('A'))) % 26 + ord('A'))
            else:
                caracter_encriptado = chr((ord(caracter) + ord(b[i]) + 32 - (2*ord('a'))) % 26 + ord('a'))
        else:
            caracter_encriptado = caracter
        texto_encriptado.append(caracter_encriptado)
    texto_encriptado = "".join(texto_encriptado)
    print(f"Mensaje: {a}\nMensaje encriptado: {texto_encriptado}")
    repeticion()

def vigenere_desencriptacion(a, b):
    texto_desencriptado = []
    b = list(b)
    if len(a) == len(b):
        return b
    else:
        for i in range(len(a) - len(b)):
            b.append(b[i % len(b)])
    b = "".join(b)
    b = b.upper()
    for i in range(len(a)):
        caracter = a[i]
        if alfabeto_ingles(caracter):
            if caracter.isupper():
                caracter_desencriptado = chr((ord(caracter) - ord(b[i]) + 26) % 26 + ord('A'))
            else:
                caracter_desencriptado = chr((ord(caracter) - ord(b[i]) - 6) % 26 + ord('a'))
        else:
            caracter_desencriptado = caracter
        texto_desencriptado.append(caracter_desencriptado)
    texto_desencriptado = "".join(texto_desencriptado)
    print(f"Mensaje encriptado: {a}\nMensaje: {texto_desencriptado}")
    repeticion()


def repeticion():
    while True:
        respuesta = input("¿Desea hacer otra operacion? (y/n): ")
        if respuesta.lower() in ["yes", "y", "s", "si"]:
            print("\n")
            break
        elif respuesta.lower() in ["no", "n"]:
            return
        else:
            print("Ingrese una opcion valida.")
    main()


main()
