#Condicionales
x = 5
if x > 10:
    print("Mayor a 10")
else:
    print("Menor a 10")

if x > 10:
    print("Mayor a 10")
elif x > 7: #else if
    print("Mayor a 7")
else:
    print("Menor a 10 y a 7")

if x < 10:
    print("Menor a 10")


#Bucles / Ciclos
for x in range(5): #Repetir del 0 al 4. Ya NO ENTRA en 5
    print(x)

print("--------")

for y in range(1,5): #Comenzando con el 1 y siempre y cuando sea menor a 5
    print(y)

print("--------")

for z in range(0, 10, 2): #(Comienzo, Menor a 10, Cantidad a avanzar)
    print(z)

print("--------")
string = "Buenos días"
print(string[0])
for letra in string:
    print(letra) 

print("--------")

array = ["A", "B", "C", "D"]
for m in array:
    print(m)

diccionario = {"nombre": "Cynthia", "edad": 30, "apellido": "Doe"}
for atributo in diccionario: #atributo = nombre, atributo = edad, atributo = apellido
    print(diccionario[atributo])


y = 0
while y < 3:
    print(y)
    y += 1

#break -> es una interrupción COMPLETA de mi bucle, es decir que cuando te encuentras con un break el bucle SE DETIENE y deja de ejecutarse
#continue -> es una interrupción solo de la ronda en la que se encuentra. Ignora la ronda actual y continúa con el ciclo

#EJERCICIO
#Dado un for que recorra del 1 al 15, Imprime todos los números EXCEPTO aquellos múltiples de 5
# % ---- x % 2 == 0

for x in range(1, 16):
    if x % 5 == 0:
        continue
    else:
        print(x)

[print(x) for x in range(1,16) if x %5 != 0]

#Dado un texto, imprime cada uno de lo caracteres y DETENTE y ya no imprimas cuando encuentres un .
texto = "Había un vez un pajarito. Muy chiquito"
nuevo_texto = ""
for letra in texto:
    if (letra == "."):
        break
    else :
        nuevo_texto += letra

print(nuevo_texto)