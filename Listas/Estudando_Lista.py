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

print("Métodos que podemos utilizar com as listas.")

print("O primeiro método é o [].append, ele é responsavel por adicionar objetos a lista.")

lista = []

lista.append(1)
lista.append("python")
lista.append([40,30,20])

print(lista)

print("O segundo é o [].clear, tem a função de limpar a lista.")

lista = [1, "Python",[40,20,30]]

print(lista)

lista.clear()

print(lista)

print("O terceiro é o [].copy, tem a função de copiar uma instancia, só que ele não retorna exatamente a lista que pode ter sido alterada.")

lista = [1, "Python",[40,20,30]]

l2 = lista.copy()

print(l2)

print(id(l2),id(lista))

print("A quarta é o [].count, esse tem a função de contar quantas vezes um valor aparece na lista.")

lista = [1,1,2,3,4,4,4]

print(lista.count(1))
print(lista.count(2))
print(lista.count(4))

print("A quinta é o [].extend, tem como função extender ou juntar listas.")

linguagens1 = ["C","C#","Java"]
linguagens2 = ["Python","JavaScript"]
linguagens = []

print(linguagens1)
print(linguagens2)

linguagens.extend(linguagens1)
linguagens.extend(linguagens2)

print(linguagens)

print("A sexta é o [].index, essa tem a função de localizar o indice de algo dentro de uma lista.")

linguagens = ["Python","Java","C#","Java","C","Dart"]

print(linguagens.index("Java"))
print(linguagens.index("C"))

print("A sétima é o [].pop, tem como função de pegar as informações da lista de acordo com a ultima informação adicionada. Como se fosse uma pilha de dados.")

linguagens = ["Python","Java","C#","Java","C","Dart"]

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

print("A oitava é o [].remove, tem como função de remover elementos da lista.")

linguagens = ["Python","Java","C#","Java","C","Dart"]

print(linguagens.count("Java"))
linguagens.remove("Java")
print(linguagens.count("Java"))

print("A nona é o [].reverse, tem como função de inverter a ordem da lista.")

linguagens = ["Python","Java","C#","Java","C","Dart"]

print(linguagens)
linguagens.reverse()
print(linguagens)

print("A décima é a [].sort, tem como função de ordenar a lista.")

linguagens = ["Python","Java","C#","Java","C","Dart"]
linguagens.sort()
print(linguagens)

linguagens = ["Python","Java","C#","Java","C","Dart"]
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ["Python","Java","C#","Java","C","Dart"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens = ["Python","Java","C#","Java","C","Dart"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

print("O décimo primeiro é o [].len, ele mostra o tamanho da lista ou quantidade de elementos dentro da lista.")

linguagens = ["Python","Java","C#","Java","C","Dart"]

print(len(linguagens))

print("O décimo segundo é o [].sorted, que serve para ordenar elementos dentro da lista assim como o sort.")

linguagens = ["Python","Java","C#","Java","C","Dart"]

print(sorted(linguagens, key=lambda x: len(x), reverse=True))