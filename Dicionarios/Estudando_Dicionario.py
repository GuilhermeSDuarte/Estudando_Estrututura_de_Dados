print("Dicionarios")

pessoa = {"nome": "Guilherme", "idade":28}

print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)

print(pessoa)

pessoa["telefone"] = "3333-1234"

print(pessoa)

print("Exemplo")

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados)

dados["nome"] = "Miguel"
dados["idade"] = 17
dados["telefone"] = "1234-1234"

print(dados)

print("Dicionario aninhado:")

contatos = {
    "guilherme@mail.com": {"nome": "Guilherme", "telefone": "1234-1234"},
    "miguel@mail.com": {"nome": "Miguel", "telefone": "1222-1334"},
    "pedro@mail.com": {"nome": "Pedro", "telefone": "1211-4444"}
}

print(contatos)

numero = contatos["miguel@mail.com"]["telefone"]

print(numero)

contato = contatos["guilherme@mail.com"]

print(contato)

for chave in contatos:
    print(chave, contatos[chave])
print("===============================================")
for chave, valor in contatos.items():
    print(chave, valor)

print("Métodos do Dicionario")

print("O primeiro método é o {}.clear, ele limpa o dicionario.")

contatos = {
    "guilherme@mail.com": {"nome": "Guilherme", "telefone": "1234-1234"},
    "miguel@mail.com": {"nome": "Miguel", "telefone": "1222-1334"},
    "pedro@mail.com": {"nome": "Pedro", "telefone": "1211-4444"}
}

contatos.clear()

print(contatos)

print("O segundo método é o {}.copy, ele copia o dicionario.")

contatos = {
    "guilherme@mail.com": {"nome": "Guilherme", "telefone": "1234-1234"},
    "miguel@mail.com": {"nome": "Miguel", "telefone": "1222-1334"},
    "pedro@mail.com": {"nome": "Pedro", "telefone": "1211-4444"}
}

copia = contatos.copy()
copia["guilherme@mail.com"] = {"nome": "Gui"}

print(contatos["guilherme@mail.com"])
print(copia["guilherme@mail.com"])

print("O terceiro método é o {}.fromkeys, serve para criar chaves dentro da biblioteca.")

contatos = {
    "guilherme@mail.com": {"nome": "Guilherme", "telefone": "1234-1234"},
    "miguel@mail.com": {"nome": "Miguel", "telefone": "1222-1334"},
    "pedro@mail.com": {"nome": "Pedro", "telefone": "1211-4444"}
}

contatos = dict.fromkeys(["idade", "sexo"], "info")

print(contatos)

print("O quarto método é o {}.get, uma forma para consultar valores dentro do dicionario, independentes dele existir ou não.")

contatos = {
    "guilherme@mail.com": {"nome": "Guilherme", "telefone": "1234-1234"},
    "miguel@mail.com": {"nome": "Miguel", "telefone": "1222-1334"},
    "pedro@mail.com": {"nome": "Pedro", "telefone": "1211-4444"}
}

resultado = contatos.get("chave")

print(resultado)

resultado = contatos.get("chave", {})

print(resultado)

resultado = contatos.get("guilherme@mail.com")

print(resultado)

print("O quinto método é o {}.items, ele retorna uma lista de tuplas, ou seja todas as chaves e valores.")

print(contatos.items())

print("O sexto método é o {}.keys, ele serve para mostrar as chaves dentro do dicionario.")

print(contatos.keys())
print(contatos["guilherme@mail.com"].keys())

print("O sétimo método é o {}.pop, ele exibe e remove o valor de forma empilhada.")

resultado = contatos.pop("guilherme@mail.com")

print(resultado)

print("O oitavo método é o {}.popitem, faz a mesma coisa que o pop, mas não há a necessidade de informar a chave.")

contatos = {
    "guilherme@mail.com": {"nome": "Guilherme", "telefone": "1234-1234"},
    "miguel@mail.com": {"nome": "Miguel", "telefone": "1222-1334"},
    "pedro@mail.com": {"nome": "Pedro", "telefone": "1211-4444"}
}

resultado = contatos.popitem()

print(resultado)

resultado = contatos.popitem()

print(resultado)

print("O nono método é o {}.setdeafault, ele verifica se um atributo existe ou não em um dicionario, se não houver ele adiciona.")

contatos = {
    "guilherme@mail.com": {"nome": "Guilherme", "telefone": "1234-1234"},
    "miguel@mail.com": {"nome": "Miguel", "telefone": "1222-1334"},
    "pedro@mail.com": {"nome": "Pedro", "telefone": "1211-4444"}
}

contatos.setdefault("nome", "Gabriel")

print(contatos)

print("O décimo método é o {}.update, ele serve para atualizar o dicionario com outros dicioanrios.")

contatos.update({"guilherme@mail.com": {"nome": "gui"}})

print(contatos)

contatos.update({"giovana@mail.com": {"nome": "Giovana", "telefone": "1546-8416"}})

print(contatos)

print("O décimo primeiro método é o {}.values, ele nos retorna todos os valores dentro do dicionario.")

print(contatos.values())

print("O décimo segundo método é o in, serve para verificar se uma chave é existente dentro do dicionario.")

resultado = "guilherme@mail.com" in contatos

print(resultado)

resultado = "gabriela@mail.com" in contatos

print(resultado)

resultado = "nome" in contatos["guilherme@mail.com"]

print(resultado)


print("O décimo terceiro método é o del, ele remove valores ou chaves do dicionario.")

contatos = {
    "guilherme@mail.com": {"nome": "Guilherme", "telefone": "1234-1234"},
    "miguel@mail.com": {"nome": "Miguel", "telefone": "1222-1334"},
    "pedro@mail.com": {"nome": "Pedro", "telefone": "1211-4444"}
}

del contatos["guilherme@mail.com"]

print(contatos)
