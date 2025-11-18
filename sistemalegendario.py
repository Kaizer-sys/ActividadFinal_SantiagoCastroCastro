from time import sleep
from colorama import Fore, Style, init
init(autoreset=True)

# ========================================================
# FUNCIONES MATEMÁTICAS
# ========================================================

def numero_perfecto(n):
    # Uso de generador para sumar divisores propios
    return sum(i for i in range(1, n) if n % i == 0) == n

def numero_armstrong(n):
    # Convierte a lista de dígitos, calcula exponente k, y verifica la suma de potencias
    digitos = [int(d) for d in str(n)]
    k = len(digitos)
    return sum(d ** k for d in digitos) == n


# ========================================================
# PATRONES VISUALES
# ========================================================

def patron_armstrong(n):
    for i in range(1, n+1):
        print(Fore.CYAN + (str(i) * i))
        sleep(0.1)

def patron_perfecto(n):
    for i in range(1, n+1):
        espacios = " " * (n - i)
        print(Fore.GREEN + espacios + str(i) * i)
        sleep(0.1)
        

# ========================================================
# VALIDACIÓN DE ENTRADA
# ========================================================

def pedir_entero():
    while True:
        valor = input(Fore.YELLOW + "Ingresa un número entero positivo: ")
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print(Fore.RED + "Entrada inválida. Por favor ingresa un número positivo.")


# ========================================================
# MENÚ PRINCIPAL PRO
# ========================================================

def menu():
    print(Fore.CYAN + "\n===============================")
    print(Fore.CYAN + "   SISTEMA KAIZER LEGENDARIO")
    print(Fore.CYAN + "===============================\n")
    print(Fore.WHITE + "1. Analizar número")
    print(Fore.WHITE + "2. ¿Qué es un número perfecto?")
    print(Fore.WHITE + "3. ¿Qué es un número Armstrong?")
    print(Fore.WHITE + "4. Salir\n")

def explicar_perfecto():
    print(Fore.GREEN + "\nUn número perfecto es aquel cuya suma de sus divisores propios\n"
                         "es exactamente igual al número.\n"
                         "Ejemplo: 6 → 1 + 2 + 3 = 6\n")

def explicar_armstrong():
    print(Fore.CYAN + "\nUn número Armstrong es aquel cuyos dígitos elevados a la cantidad\n"
                      "de dígitos suman el mismo número.\n"
                      "Ejemplo: 153 → 1³ + 5³ + 3³ = 153\n")


# ========================================================
# LÓGICA PRINCIPAL MODIFICADA
# ========================================================

def analizar_numero():
    n = pedir_entero()
    a = numero_armstrong(n)
    p = numero_perfecto(n)
    
    # Se usa una bandera para saber si se encontró al menos una propiedad
    encontrado = False 

    print(Fore.YELLOW + "\n=== RESULTADOS ===\n")
    sleep(0.3)

    if a:
        print(Fore.CYAN + f"{n} es un número ARMSTRONG. ")
        print(Fore.CYAN + "Mostrando patrón ascendente...\n")
        patron_armstrong(5)
        encontrado = True

    if p:
        # Se imprime un mensaje si ya se había impreso el de ARMSTRONG
        if encontrado:
            print(Fore.GREEN + f"Además, {n} es también un número PERFECTO. ")
        else:
            print(Fore.GREEN + f"{n} es un número PERFECTO. ")
        
        print(Fore.GREEN + "Mostrando patrón equilibrado...\n")
        patron_perfecto(5)
        encontrado = True

    # El bloque else final verifica si *ninguna* propiedad fue encontrada
    if not encontrado:
        print(Fore.RED + f"{n} NO es Armstrong ni Perfecto.")
        print(Fore.RED + "Mostrando patrón simple...\n")
        patron_armstrong(3)


# ========================================================
# LOOP PRINCIPAL DEL PROGRAMA
# ========================================================

while True:
    menu()
    op = input(Fore.YELLOW + "Selecciona una opción: ")

    if op == "1":
        analizar_numero()
    elif op == "2":
        explicar_perfecto()
    elif op == "3":
        explicar_armstrong()
    elif op == "4":
        print(Fore.BLUE + "\nSaliendo del sistema... Hasta pronto, Kaizer.\n")
        break
    else:
        print(Fore.RED + "Opción inválida. Intenta nuevamente.\n")
        
