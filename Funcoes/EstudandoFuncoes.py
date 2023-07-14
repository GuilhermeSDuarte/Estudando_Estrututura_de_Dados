def mensagem():
    print("Ola mundo")

def mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

mensagem()
mensagem2("Guilherme")
mensagem3()

def soma(numeros):
    return sum(numeros)
def retorna (numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(soma([10,20,30]))
print(retorna(10))

def salvar_carro(marca, modelo,ano,placa):
    print(f"Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}")

salvar_carro("Fiat","Palio",1999,"ABC-1234")
salvar_carro(marca="Fiat",modelo="Palio",ano=1999,placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "palio", "ano": 1999, "placa": "ABC-1234"})

def exibir_texto(data_extenso, *palavras, **detalhes):
    texto = "\n".join(palavras)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in detalhes.items()])
    mensagem = f"\n{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_texto(
    "Quinta Feira, 13 de Julho de 2023",
    "Funções",
    "Hoje estou estudando as funções,",
    "ou seja, como fazer manipulação com elas,",
    "aqui aprendi como fazer com que a função retorne",
    "Tuplas e Variaveis.",
    autor="Guilherme",
    ano=2023,
)

#Tudo que houver antes da / tem que ser definido por posição, após podemos adicioanr parametros por keywords.
#Tudo que houver após * tem que ser definido por keywords
def criar_carros(modelo, ano, placa, /, marca, motor, combustivel, *, tamanho):
    print(modelo, ano, placa, marca, motor, combustivel,tamanho)

criar_carros("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina", tamanho="5 metros") #Válido

#criar_carros(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina", "2 metros") #Inválido

def somar(a,b):
    return a + b
def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da soma {a} + {b} = {resultado}")

exibir_resultado(10,10,somar)

#Exemplo de variavelGlobal

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))