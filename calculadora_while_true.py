"""Este programa usa el "while True" Para crear una calculadora donde el usuario decida si 
seguir haciendo cálculos o salirse del programa """


def bienvenida():
    """ Esta función imprime la bienvenida. """
    print("🔢 Bienvenido a la Calculadora Cuántica 🧠")
    print("Estas son las operaciones disponibles:")
    print("- Suma")
    print("- Resta")
    print("- Multiplicación")
    print("- División")
    print("- Potenciación")
    print("✨ Puedes comenzar cuando quieras...\n")

def operaciones():
    """ Le pedimos al usuario que ingrese la operacion
    que desea hacer, pero si ingresa una operacion
    no válida entonces le seguirá pidiendo una operación
    hasta que ingrese una válida. """

    operaciones_validas = ["Suma", "Resta", "Multiplicacion", "Division", "Potenciacion"]
    print(f"Operaciones válidas: {operaciones_validas}")

    while True:
        operacion = input("Ingrese la operación:").capitalize()

        if operacion not in operaciones_validas:
            print("Error: Ingresaste una operación no válida. ")
            continue
        return operacion

def ingresar_numeros():
    """ Le pedimos al usuario los números, si ingresa un
    dato no válido le seguiremos pidiendo los números hasta
    que ingrese números válidos. """

    while True:
        try:
            n1 = float(input("Digite el primer número: "))
            n2 = float(input("Digite el segundo número: "))
            return n1,n2
        except ValueError:
            print("Error: Tipo de dato no válido.")
            continue

def operar_numeros(a,b, op):
    """Esta función resuelve las operaciones. """
    if op == "Suma":
        return a + b
    elif op == "Resta":
        return a - b
    elif op == "Multiplicacion":
        return a * b
    elif op == "Division":
        return a / b
    elif op == "Potenciacion":
        return a ** b

def imprimir_datos(dato1,dato2, operacion, resultado):
    """Esta funcion imprimira la operacion final. """
    if operacion == "Suma":
        print(f"{dato1} + {dato2} = {resultado}")
    elif operacion == "Resta":
        print(f"{dato1} - {dato2} = {resultado}")
    elif operacion == "Multiplicacion":
        print(f"{dato1} * {dato2} = {resultado}")
    elif operacion == "Division":
        print(f"{dato1} / {dato2} = {resultado}")
    elif operacion == "Potenciacion":
        print(f"{dato1} ^ {dato2} = {resultado}")

def programa_principal():
    """Esto ejecutará el programa principal."""
    while True:
        try:
            numero1, numero2 = ingresar_numeros()
            operacion = operaciones()
            resultado = operar_numeros(numero1, numero2, operacion)
            imprimir_datos(numero1, numero2, operacion, resultado)

            # Este while debe estar dentro del try
            while True:
                seguir = input("¿Deseas realizar otro cálculo? (si/no): ").lower()
                if seguir == "si":
                    break  # Vuelve al inicio del primer while
                elif seguir == "no":
                    print("👋 Gracias por usar la calculadora.")
                    return
                else:
                    print("❌ Respuesta no válida. Escribe 'sí' o 'no'.")

        except ZeroDivisionError:
            print("⚠️ No se puede dividir entre cero. Intenta otra vez.\n")
            continue

if __name__ == "__main__":
    programa_principal()
