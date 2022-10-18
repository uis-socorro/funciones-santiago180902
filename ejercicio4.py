# Ejercicio 4

def promediar(lista):
    suma = 0
    promedio = 0
    cont = 0
    for i in lista:
        suma = suma + i
        cont = cont + 1
    promedio = suma / cont
    return promedio


#lista
lista1 = [2,3,4,5,6]
promedio = promediar(lista1)
print(promedio)