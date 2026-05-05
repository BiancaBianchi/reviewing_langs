#------------ If/Else/Elif ------------

score = 8.5

# Básico
if score >= 9:
    nivel = "expert"
elif score >= 7:
    nivel = "senior"
elif score >= 5:
    nivel = "pleno"
else:
    nivel = "junior"

# Ternário — equivale ao a ? b : c de outras linguagens
nivel = "aprovado" if score >= 6 else "reprovado"

# Match/case — Python 3.10+ (equivale ao switch/case)
match nivel:
    case "expert":
        print("Nível máximo!")
    case "senior" | "pleno":   # múltiplos valores
        print("Nível intermediário")
    case _:                    # default
        print("Nível inicial")

# Match com estruturas (muito poderoso para APIs)
def processar_evento(evento: dict):
    match evento:
        case {"tipo": "login", "usuario": usuario}:
            print(f"Login: {usuario}")
        case {"tipo": "erro", "codigo": codigo} if codigo >= 500:
            print(f"Erro crítico: {codigo}")
        case _:
            print("Evento desconhecido")


#------------ For and While ------------

# for — itera sobre qualquer iterável
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8 (start, stop, step)
    print(i)

# Controle de loop
for n in range(10):
    if n == 3:
        continue    # pula para próxima iteração
    if n == 7:
        break       # sai do loop
    print(n)
else:
    # else do for executa se o loop completou sem break
    print("loop completo")

# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1   # Python não tem ++

# Evite while True sem break claro — use condição no while

#------------ Generators ------------

# generators calculam um item por vez. Essencial para pipelines de dados.

# List comprehension — cria tudo na memória
quadrados_lista = [n ** 2 for n in range(1_000_000)]  # 8MB na memória

# Generator expression — calcula sob demanda ✅
quadrados_gen = (n ** 2 for n in range(1_000_000))    # ~100 bytes

# Consumindo um generator
next(quadrados_gen)    # 0
next(quadrados_gen)    # 1
for q in quadrados_gen:  # itera normalmente
    print(q)

# Função geradora com yield
def contar_ate(limite: int):
    n = 0
    while n < limite:
        yield n          # pausa aqui, retorna n, retoma na próxima chamada
        n += 1

for i in contar_ate(5):  # 0, 1, 2, 3, 4
    print(i)

# Caso de uso real — leitura de arquivo grande linha a linha
def ler_linhas(caminho: str):
    with open(caminho) as f:
        for linha in f:
            yield linha.strip()   # uma linha por vez, sem carregar tudo

# Encadeamento de generators (pipeline de dados)
linhas = ler_linhas("dados.csv")
nao_vazias = (l for l in linhas if l)
campos = (l.split(",") for l in nao_vazias)