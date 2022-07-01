#Función es un bloque de código al cual nombramos y que podemos ejecutar cada vez que lo llamemos
def hola():
    print("Hello World")


def holaReturn():
    suma = 1 + 2
    texto = "Hello World Return"
    return texto

hola()
hello = holaReturn() #hello = "Hello World Return"
print(hello)
print(holaReturn())

def suma(a, b): #a = 1; b = 2
    numeros_sumados = a + b #numeros_sumados = 1 + 2 -> 3
    print(numeros_sumados)

def sumaReturn(a, b): #a = 3; b = 4
    print(a)
    print(b)
    numeros_sumados = a + b #numeros_sumados = 3 + 4 -> 7
    return numeros_sumados

suma(1, 2)
sum = sumaReturn(3, 4) # sum = 7

print("El valor de tu suma es "+str(sum))

sum += 1
print("El valor de tu suma es con un numero mas es "+str(sum))

def hello_world(nombre="John", apellido="Doe"): #nombre = "Elena" apellido = "De Troya"
    print(f"Hola {nombre} {apellido}") #Hola Elena De Troya

hello_world("Elena", "De Troya")
hello_world("Elena")
hello_world()
hello_world(apellido="De Troya")

#Función que reciba una lista de números y que regrese la sumatoria de los números recibidos
#lista = [1, 2, 3, 4, 5]
#suma = 0
#num = 1
#suma = 0 + 1 -> 1
#num = 2
#suma = 1 + 2 -> 3
#num = 3
#suma = 3 + 3 -> 6
#num = 4
#suma = 6 + 4 -> 10
#num = 5
#suma = 10 + 5 -> 15
#RETURN suma = 15
def sumatoria(lista):
    suma = 0
    for num in lista:
        suma += num

    return suma

#suma = sumatoria([1, 2, 3, 4, 5]) #suma = 15
print(sumatoria([1, 2, 3, 4, 5]))

#Funcion que reciba una lista de números y que me regrese el número MAYOR.
#OJO no podemos usar las funciones por default de Python (max)
#lista = [10,2,7,6]
#num_mayor = 10
#n = 10
#n = 2
#n = 7
#n = 6
def numero_mayor(lista):
    num_mayor = lista[0]
    for n in lista:
        if n > num_mayor:
            num_mayor = n
    return num_mayor

mayor = numero_mayor([10,2,7,6]) #Me debe regresar 7
print(mayor)

#numero = 5
#lista = []
#5 - 0
#i = 5
#lista = [5]
#i = 4
#lista = [5, 4]
#i = 3
#lista = [5, 4, 3]
#i = 2
#lista = [5, 4, 3, 2]
#i = 1
#lista = [5, 4, 3, 2, 1]
#i = 0
#lista = [5, 4, 3, 2, 1, 0]
#RETURN [5, 4, 3, 2, 1, 0]
def countdown(numero):
    lista = []
    for i in range(numero, -1, -1): #(Comienzo, Detener, Cantidad a avanzar)
        lista.append(i)
    return lista

print(countdown(5))

def imprimir_y_devolver(lista): #lista = [1, 2]
    print(lista[0]) #IMPRIME 1
    return lista[1] #RETURN 2

print(imprimir_y_devolver([1, 2]))

#len(array) -> Regresa el tamaño de nuestra lista

#tamano = 3
#valor = 5
#lista = []
#0 - 2
#i = 0
#lista = [5]
#i = 1
#lista = [5, 5]
#i = 2
#lista = [5, 5, 5]
def length_and_value(tamano, valor):
    lista = []
    for i in range(tamano): #0 - tamano-1
        lista.append(valor)
    return lista

print(length_and_value(3, 5))