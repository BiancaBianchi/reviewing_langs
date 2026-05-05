#------------ Variables ------------

# Tipos primitivos
nome: str = "Bianca"
idade: int = 30
altura: float = 1.65
ativo: bool = True
nada: None = None

# Python infere o tipo — o hint é opcional, mas bom hábito
x = 42          # int
y = 3.14        # float
z = "texto"     # str

#------------ Strings ------------

nome = "Bianca"
linguagem = "Python"

# ❌ Concatenação antiga (evite)
msg = "Olá, " + nome + "! Bem-vinda ao " + linguagem

# ❌ .format() — ainda funciona mas é verboso
msg = "Olá, {}! Bem-vinda ao {}".format(nome, linguagem)

# ✅ f-string — use sempre (Python 3.6+)
msg = f"Olá, {nome}! Bem-vinda ao {linguagem}"

# f-strings aceitam expressões inteiras
preco = 19.9
print(f"Preço: R${preco:.2f}")    # R$19.90
print(f"Dobro: {preco * 2}")      # Dobro: 39.8
print(f"Maiúsculo: {nome.upper()}")

# Python 3.12 — f-string ainda mais poderosa (pode aninhar aspas)
itens = ["a", "b", "c"]
print(f"Itens: {', '.join(itens)}")  # Itens: a, b, c

# Multilinha — útil para prompts de LLM!
system_prompt = """
Você é um assistente especializado em acessibilidade.
Responda de forma clara e objetiva.
"""

# Raw string — ignora escape sequences (útil para regex e paths)
caminho = r"C:\Users\Bianca\Documents"
padrao = r"\d{3}-\d{4}"  # regex sem precisar escapar \ duas vezes

texto = "  Olá, Bianca!  "

texto.strip()          # "Olá, Bianca!"      — remove espaços
texto.lower()          # "  olá, bianca!  "
texto.upper()          # "  OLÁ, BIANCA!  "
texto.replace("Bianca", "Dev")  # substitui
texto.split(", ")      # ["  Olá", "Bianca!  "]
texto.startswith("Olá")         # False (tem espaço no início)
texto.strip().startswith("Olá") # True

# Verificar conteúdo
"python" in "aprendendo python"   # True
"" .join(["a", "b", "c"])        # "abc"
"-".join(["2025", "01", "15"])   # "2025-01-15"

#------------ Numbers ------------

# int — sem limite de tamanho (diferente de outras linguagens)
grande = 1_000_000   # underscores para legibilidade (Python 3.6+)
binario = 0b1010     # 10
hex_val = 0xFF       # 255

# float — ponto flutuante (cuidado com precisão)
0.1 + 0.2            # 0.30000000000000004  ← problema clássico
round(0.1 + 0.2, 2)  # 0.3

# Para dinheiro: use Decimal
from decimal import Decimal
preco = Decimal("19.90")
taxa = Decimal("0.10")
total = preco + preco * taxa  # Decimal('21.890') — sem erro de float

# Operadores
10 / 3    # 3.3333...  ← divisão sempre retorna float
10 // 3   # 3          ← divisão inteira
10 % 3    # 1          ← módulo
2 ** 10   # 1024       ← potência (equivalente ao pow(2, 10))
abs(-5)   # 5

#------------ Compare ------------

# Valores "falsy" — avaliam como False em contexto booleano
False, None, 0, 0.0, "", [], {}, set()

# Valores "truthy" — tudo o mais
True, 1, "texto", [1, 2], {"a": 1}

# Exemplos práticos
lista = []
if not lista:           # ← pythônico — equivale a "if lista == []"
    print("vazia")

nome = None
if nome is None:        # ← use "is None", não "== None"
    print("sem nome")

# Operadores lógicos — são palavras, não símbolos!
True and False  # False    (em Ruby: &&)
True or False   # True     (em Ruby: ||)
not True        # False    (em Ruby: !)

# Comparadores encadeados — exclusivo do Python
1 < x < 10          # equivale a: x > 1 and x < 10
0 <= pontos <= 100  # validação de range em uma linha