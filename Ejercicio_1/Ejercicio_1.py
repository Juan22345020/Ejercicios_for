print("------------------------------------------------")
print("-----------------Pares e impares----------------")
print("------------------------------------------------")

n = int(input("Ingrese la cantidad de números que desea ingresar: "))
pares = 0
impares = 0

for i in range(n):
    n1 = int(input("Ingrese un número entero: "))
    if n1 % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Los numeros que son pares fueron: " + str(pares) + " y los numeros que fueron impares son: " + str(impares) )
