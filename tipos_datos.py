#Boolean
boolean = True #True o False

#Numerales
num = 10
fl = 10.34
nuevo_float = float(90) #Transformo un numero entero en número decimal
nuevo_entero = int(1092.60) #Transformando un número decial a entero
print(nuevo_float)
print(nuevo_entero)

import random
num_aleatoria = random.randint(2,5) #Numero aleatorio entre 2 y 5
print(num_aleatoria)

#Cadenas/Texto/String
string = "ABCDEFG"
print("Este es el alfabeto", string) #La coma en automático me agrega un espacio
print("Este es el alfabeto "+string) #El + concatena tal cual se encuentra
print("Este es un numero", 10)
#print("Este es un numero"+ 10) #ERROR estamos intentando sumar dos tipos diferentes
print("Este es un numero "+ str(num))

#Métodos para strings
saludo = "hola mundo! bienvenidos a Python"
print(saludo.title()) #Primera letra de cada palabra sea mayúscula
print(saludo.upper()) #Todas las letras las hace mayúsculas
print(saludo.lower()) #Todas las letras sean minúsculas
print(saludo.count('do')) #Regresa cuántos 'do' hay en la cadena
print(saludo.find('python')) #Regresa dónde comienza 'Python'. SI ACASO no está me regresa -1. CASE SENSITIVE

#Lista/Arreglo
lista_vacia = []
lista_llena = ["Hugo", "Paco", "Luis"] #0 => Hugo, 1 => Paco, 2 = Luis
print(lista_llena[0])
lista_llena[0] = "Donald"
print(lista_llena)
lista_llena.append("Mickey") #Agrega un último dato a la lista
print(lista_llena)
lista_llena.pop() #Eliminamos el último elemento de la lista
print(lista_llena)
lista_llena.pop(0) #Eliminamos el elemento en posición 0
print(lista_llena)
lista_mix = ["Texto1", "Texto2", 1, ["elemento1.1", "elemento1.2"]] #Las listas tienen la capacidad de agregar distintos tipos de datos
lista_nombres = ["Juana", "Pedro", "Pablo"]
nuevo_lista = lista_mix+lista_nombres
print(nuevo_lista)
print(lista_mix[3][0])

#Diccionarios -> similar a Objeto en JS
diccionario_vacio = {}
diccionario = {"nombre": "Juana", "apellido": "De Arco", "edad": 30, "soltero": False}
diccionario['estatura'] = 1.67
diccionario['hobbies'] = ["Leer", "Ver tele", "Escribir"]
print(diccionario)
diccionario['nombre'] = "Elena"
print(diccionario)
diccionario.pop("estatura")
print(diccionario)
diccionario['nombre_completo'] = diccionario['nombre']+" "+diccionario['apellido']
print(diccionario)