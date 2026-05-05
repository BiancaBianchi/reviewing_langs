#------------ Functions ------------

# Básico
def somar(a: int, b: int) -> int:
    return a + b

# Retorno múltiplo (tupla)
def dividir(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b

q, r = dividir(10, 3)   # unpacking

# Valor padrão
def saudar(nome: str, saudacao: str = "Olá") -> str:
    return f"{saudacao}, {nome}!"

saudar("Bianca")           # "Olá, Bianca!"
saudar("Bianca", "Oi")    # "Oi, Bianca!"

# ⚠️ Armadilha clássica: valor padrão mutável
def adicionar(item, lista=[]):   # ❌ a lista é compartilhada entre chamadas!
    lista.append(item)
    return lista

def adicionar(item, lista=None):  # ✅ correto
    if lista is None:
        lista = []
    lista.append(item)
    return lista

#------------ *args and **kwargs ------------

# *args — captura argumentos posicionais extras como tupla
def somar_tudo(*numeros: int) -> int:
    return sum(numeros)

somar_tudo(1, 2, 3, 4, 5)   # 15

# **kwargs — captura argumentos nomeados extras como dict
def criar_usuario(**dados: str) -> dict:
    return dados

criar_usuario(nome="Bianca", email="bi@email.com")
# {"nome": "Bianca", "email": "bi@email.com"}

# Combinando tudo
def funcao_completa(obrigatorio: str, *args, chave: str = "padrão", **kwargs):
    print(f"obrigatorio: {obrigatorio}")
    print(f"args: {args}")
    print(f"chave: {chave}")
    print(f"kwargs: {kwargs}")

funcao_completa("valor", 1, 2, 3, chave="custom", extra="dados")

# Desempacotamento — o inverso: passar lista/dict como argumentos
def somar(a, b, c):
    return a + b + c

numeros = [1, 2, 3]
somar(*numeros)     # equivale a somar(1, 2, 3)

config = {"a": 1, "b": 2, "c": 3}
somar(**config)     # equivale a somar(a=1, b=2, c=3)

#------------ lambdas ------------

# Funções são objetos — podem ser passadas e retornadas
def aplicar(func, valor):
    return func(valor)

def dobrar(x):
    return x * 2

aplicar(dobrar, 5)   # 10

# Lambda — função anônima de uma linha
dobrar = lambda x: x * 2
dobrar(5)   # 10

# Uso comum: key em sort
usuarios = [{"nome": "Zé", "score": 7}, {"nome": "Ana", "score": 9}]
usuarios.sort(key=lambda u: u["score"], reverse=True)

# map e filter (prefira comprehensions, mas bom saber)
quadrados = list(map(lambda x: x**2, [1, 2, 3, 4]))
pares = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

#------------ Decorators ------------

import time
from functools import wraps

# Decorator básico — mede tempo de execução
def medir_tempo(func):
    @wraps(func)     # preserva nome e docstring da função original
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} levou {fim - inicio:.3f}s")
        return resultado
    return wrapper

@medir_tempo
def processar_dados(n: int) -> list[int]:
    return [i ** 2 for i in range(n)]

processar_dados(10_000)
# processar_dados levou 0.002s

# Decorator com parâmetros
def repetir(vezes: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorator

@repetir(3)
def dizer_oi():
    print("Oi!")

dizer_oi()  # imprime "Oi!" 3 vezes

# Exemplo real: decorator de retry para chamadas de API
def retry(max_tentativas: int = 3, espera: float = 1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for tentativa in range(max_tentativas):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if tentativa == max_tentativas - 1:
                        raise
                    print(f"Tentativa {tentativa + 1} falhou: {e}. Tentando de novo...")
                    time.sleep(espera)
        return wrapper
    return decorator

@retry(max_tentativas=3, espera=2.0)
def chamar_api(endpoint: str) -> dict:
    # chama API que pode falhar