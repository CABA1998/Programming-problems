#    _________    ____  ___ 
#   / ____/   |  / __ )/   |
#  / /   / /| | / __  / /| |
# / /___/ ___ |/ /_/ / ___ |
# \____/_/  |_/_____/_/  |_|
                          
# Python

# Ingreso de la informacion

import numpy as np

numeros = [int(i) for i in raw_input().split(' ')]
palabra1 = raw_input()
palabra2 = raw_input()
palabra3 = raw_input()

# Funcion para comparar dos strings

def comparar_strings(string1,string2):
    for j in range(0,len(string2)-len(string1)+1):
        if string1 == string2[j:len(string1)+j]:
            return True

""" Funcion que encuentra el string comun mas largo entre tres strings
    string1 => string2 => string3 """

def string_comun(string1, string2, string3):
    for i in range(0, len(string1)):
        for k in range(0,i+1):
            if comparar_strings(string1[k:len(string1)+(k-i)], string2) and comparar_strings(string1[k:len(string1)+(k-i)], string3):
                return string1[k:len(string1)+(k-i)]
    
#Organizo la informacion en listas segun la longitud de las palabras
lista_palabras = [palabra1, palabra2, palabra3]
lista_numeros = np.array(numeros)
lista_ordenada=[]

for i in range(1,len(lista_palabras)+1):
    posicion = lista_numeros.argsort()[-i]
    lista_ordenada.append(lista_palabras[posicion])


print(string_comun(lista_ordenada[2], lista_ordenada[1], lista_ordenada[0]))
