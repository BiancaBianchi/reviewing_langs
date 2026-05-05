#------------ Lists ------------

# Criação
frutas = ["maçã", "banana", "uva"]
misturada = [1, "texto", True, None]  # pode misturar tipos
vazia = []

# Acesso — indexação e fatiamento (slicing)
frutas[0]     # "maçã"     — primeiro
frutas[-1]    # "uva"      — último
frutas[1:3]   # ["banana", "uva"]  — do índice 1 até 2 (3 não incluso)
frutas[:2]    # ["maçã", "banana"] — do início até 1
frutas[::2]   # ["maçã", "uva"]   — de 2 em 2

# Modificação
frutas.append("laranja")          # adiciona no fim
frutas.insert(1, "kiwi")          # insere na posição 1
frutas.extend(["pêra", "manga"])  # concatena outra lista
frutas.remove("banana")           # remove por valor (erro se não existe)
ultimo = frutas.pop()             # remove e retorna o último
frutas.pop(0)                     # remove e retorna o de índice 0

# Informações
len(frutas)            # tamanho
"maçã" in frutas       # True/False
frutas.index("uva")    # posição do elemento
frutas.count("maçã")   # quantas vezes aparece

# Ordenação
numeros = [3, 1, 4, 1, 5]
numeros.sort()              # ordena in-place (modifica a lista)
ordenada = sorted(numeros)  # retorna nova lista ordenada
numeros.reverse()           # inverte in-place

#------------ Map/Select ------------

# Equivale a um map/select do Ruby, mas em uma linha

# Sem comprehension (verboso)
quadrados = []
for n in range(10):
    quadrados.append(n ** 2)

# Com comprehension ✅
quadrados = [n ** 2 for n in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Com filtro
pares = [n for n in range(10) if n % 2 == 0]
# [0, 2, 4, 6, 8]

# Transformação e filtro juntos
scores_altos = [s.upper() for s in nomes if len(s) > 4]

# Com enumerate — quando você precisa do índice
frutas = ["maçã", "banana", "uva"]
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
# 0: maçã / 1: banana / 2: uva

# Zip — iterar duas listas juntas
nomes = ["Alice", "Bob"]
idades = [30, 25]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

#------------ Dictionaries ------------

# Criação
usuario = {
    "nome": "Bianca",
    "email": "bi@email.com",
    "ativo": True,
    "score": 9.5
}

# Criação alternativa (útil para keys dinâmicas)
vazio = {}
de_lista = dict(nome="Bianca", email="bi@email.com")

# Acesso
usuario["nome"]                    # "Bianca" — erro se não existir
usuario.get("nome")                # "Bianca" — None se não existir
usuario.get("telefone", "N/A")     # "N/A"   — valor padrão ✅ use sempre
usuario.get("telefone") or "N/A"   # alternativa com or

# Modificação
usuario["telefone"] = "11999999999"  # adiciona ou atualiza
usuario.update({"score": 10, "nivel": "senior"})  # atualiza múltiplos
del usuario["telefone"]              # remove
removido = usuario.pop("score", None)  # remove e retorna (None se não existe)

# Verificação
"nome" in usuario       # True — checa keys
"Bianca" in usuario     # False — não checa values!

# Iteração
for chave in usuario:                    # itera sobre keys
    print(chave)
for chave, valor in usuario.items():    # itera sobre key-value
    print(f"{chave}: {valor}")
for valor in usuario.values():          # só valores
    print(valor)

# Informações
len(usuario)          # número de pares
list(usuario.keys())  # ["nome", "email", "ativo"]

# Inverter key/value
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# Filtrar dict
ativos = {k: v for k, v in usuarios.items() if v["ativo"]}

# Criar dict a partir de duas listas
campos = ["nome", "email", "score"]
valores = ["Bianca", "bi@email.com", 9.5]
usuario = dict(zip(campos, valores))

#------------ Merge de Dicts ------------

base = {"host": "localhost", "port": 5432}
extra = {"database": "mydb", "port": 5433}  # port conflita

merged = base | extra          # ✅ novo operador — extra sobrescreve base
# {"host": "localhost", "port": 5433, "database": "mydb"}

base |= extra                  # merge in-place (modifica base)

#------------ Tuples ------------

ponto = (10, 20)          # tupla
coordenada = (1.5, -3.2)

# Acesso igual à lista
ponto[0]   # 10
ponto[-1]  # 20

# Imutabilidade
ponto[0] = 99  # ❌ TypeError — não pode modificar

# Unpacking — muito usado em Python
x, y = ponto               # x=10, y=20
a, b, *resto = (1, 2, 3, 4, 5)  # a=1, b=2, resto=[3,4,5]

# Funções que retornam múltiplos valores usam tupla
def dividir(a, b):
    return a // b, a % b   # retorna tupla implicitamente

quociente, resto = dividir(10, 3)  # unpacking direto

# Named tuple — tupla com campos nomeados (melhor legibilidade)
from collections import namedtuple
Ponto = namedtuple("Ponto", ["x", "y"])
p = Ponto(10, 20)
p.x    # 10 — acesso por nome
p.y    # 20

#------------ Sets ------------

# Criação
cores = {"vermelho", "azul", "verde"}
vazio = set()          # ATENÇÃO: {} cria dict vazio, não set!

# Adicionar/remover
cores.add("amarelo")
cores.discard("azul")    # remove se existir, não dá erro se não existir
cores.remove("azul")     # remove, dá KeyError se não existir

# Verificação — O(1), muito mais rápido que lista!
"vermelho" in cores   # True

# Operações de conjunto
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a & b       # {3, 4}         — interseção
a | b       # {1,2,3,4,5,6}  — união
a - b       # {1, 2}         — diferença (em a mas não em b)
a ^ b       # {1,2,5,6}      — diferença simétrica

# Caso de uso clássico: remover duplicatas
lista_com_dup = [1, 2, 2, 3, 3, 3, 4]
sem_dup = list(set(lista_com_dup))  # [1, 2, 3, 4]