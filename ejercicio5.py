# Ejercicio 5

def promediar_pares(lista):
    suma = 0
    promedio = 0
    cont = 0
    for i in lista:
        if i%2 == 0:
            suma = suma + i
            cont = cont + 1
    promedio = suma / cont
    return promedio


#lista
lista1 = [2,3,4,5,6]
promedio = promediar_pares(lista1)
print(promedio)