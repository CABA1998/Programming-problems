#    _________    ____  ___ 
#   / ____/   |  / __ )/   |
#  / /   / /| | / __  / /| |
# / /___/ ___ |/ /_/ / ___ |
# \____/_/  |_/_____/_/  |_|

# Python

import numpy as np

# Funcion para saber si un numero es Primo

def primo(num):
    resultado = not np.any([num%i == 0 for i in range(2, num)])
    if resultado==True:
        return True
    else:
        return False

# Ingreso del numero 'N'
while True:
    numero = int(input())
    if  numero > 0 and len(str(numero)) <= 7:
        break
    else:
        print("Intente de nuevo")

""" El siguiente algoritmo  se trata de buscar en los numeros palindromos,
esto con el fin de ahorrar iteraciones """

for i in range(1, 10**7):
    # Miramos los numeros de logitud impar
    prueba = str(i)
    el_numero = int(prueba + prueba[-2::-1])
    if el_numero >= numero and primo(el_numero):
        print(el_numero)
        break
    # Miramos los numeros de longitud par
    prueba = str(i)
    el_numero = int(prueba + prueba[-1::-1])
    if el_numero >= numero and primo(el_numero):
        print(el_numero)
        break
