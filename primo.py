# Verificar si un número es primo

def es_primo(n):
    primo = True
    for i in range(2,n):
        if n % i == 0:
            primo = False
    return primo


n = int(input("Digite la cantidad de primos a mostrar: "))

i = 1
s = "Primos: "
np = 0
while np < n:
    if es_primo(i):
        s = s + str(i) + ","
        np = np + 1
    i = i + 1
print(s)
