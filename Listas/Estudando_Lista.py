frutas = ["laranja","maça","uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "f8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

frutas = ["laranja","maça","uva", "pera"]
print(frutas[0])
print(frutas[2])
print(frutas[-1])

matriz = [
    [1,"a",2],
    ["b",3,4],
    [6,7,"c"]
]
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[2][1])

lista = ["p","y","t","h","o","n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[::])
print(lista[::-1])

numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

numeros = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

numeros = [1,30,21,2,9,65,34]
quadrado = []

for numero in numeros:
        quadrado.append(numero ** 2)
print(quadrado)