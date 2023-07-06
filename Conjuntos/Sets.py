print("Conjunto ou set é uma coleção que não possui elementos repetidos ou duplicados.")

numeros = [1,1,2,3,4,4,4,3]

print(set(numeros))

objeto = ("ABACAXI")

print(set(objeto))

objetos = ("mesa","mesa","cadeira","sofa")

print(set(objetos))

numeros = {1,1,1,2,3,4,5,6,1,2,3,4,5}

print(numeros)

print("Há como converter esses conjuntos em lista:")

numeros = {1,1,1,2,3,4,5,6,1,2,3,4,5}

print(numeros)

numero = list(numeros)

print(numero[0])

for num in numeros:
    print(num)

print("Tambem conseguimos usar alguns métodos com o set, o primeiro deles é o [].union, que uni dois conjuntos.")

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.union(conjunto_b))

print("O segundo método é o [].intersection, ele pega os valores pertencentes aos conjuntos indicados conjuntos.")

print(conjunto_a.intersection(conjunto_b))

print("O terceiro é o [].diferrence, são todos aqueles valores que não estão presentes em um e no outro está.")

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

print("O quarto é o [].symmetric_diference, pega os elementos que não estão presente em um conjunto mais estão no outro, só que aparece ambos os elementos.")

print(conjunto_a.symmetric_difference(conjunto_b))

print("O quinto é o [].issubset, ele informa se um conjunto é um sub-conjunto de outro, ou seja os elementos de um conjunto estão em outro conjunto.")

conjunto_a = {1,2,3}
conjunto_b = {5,7,2,3,1,4}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

print("O sexto é o [].issuperset, faz o contrario do issubsset.")

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

print("O sétimo é o [].isdisjoint, onde ele informa se nenhum dos conjuntos possuem valores iguais.")

conjunto_a = {1,2,3}
conjunto_b = {5,7,4}
conjunto_c = {8,9,10,11,1}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))
print(conjunto_b.isdisjoint(conjunto_c))

print("O oitavo é o [].add, que passa um elemento que é verificado se ele existe ou não no conjunto, se eu passar um existente ele não adiciona.")

conjunto_a.add(30)
conjunto_a.add(2)

print(conjunto_a)

print("O nono é o [].copy, funciona da mesma forma que na lista.")

print("O décimo é o [].discard, onde ele remove valores existentes no conjunto, se não existir ele não faz nada.")

conjunto_a.discard(30)
conjunto_a.discard(45)

print(conjunto_a)

print("O décimo primeiro é o [].pop, ele no set vai tirando os itens de forma empilhada, a unica diferença é que ele tira o primeiro valor até o ultimo.")

print(conjunto_a.pop())
print(conjunto_a.pop())
print(conjunto_a.pop())

print("O décimo primeiro é o [].remove, ele remove um elemento só que ele da erro caso você tente remover um valor inexistente no conjunto.")

conjunto_a = {1,2,3}

conjunto_a.remove(1)

print(conjunto_a)

print("O décimo segundo é o [].len, ele conta a quantidade de elementos dentro do conjunto.")

print(len(conjunto_a))

print("Podemos tambem verificar se um valor está dentro de um conjunto")

print(1 in conjunto_a)
print(2 in conjunto_a)
print(3 in conjunto_a)
print(4 in conjunto_a)
