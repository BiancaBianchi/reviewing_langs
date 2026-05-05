#------------ Errors and Exceptions ------------

# Hierarquia básica
# BaseException
#   Exception
#     ValueError      — valor inválido
#     TypeError       — tipo errado
#     KeyError        — chave inexistente em dict
#     IndexError      — índice fora de range
#     AttributeError  — atributo inexistente
#     FileNotFoundError
#     RuntimeError

# try/except/else/finally
def ler_config(caminho: str) -> dict:
    try:
        with open(caminho) as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        return {}
    except json.JSONDecodeError as e:
        print(f"JSON inválido: {e}")
        return {}
    else:
        # executa SOMENTE se não houve exceção
        print("Config carregada com sucesso")
    finally:
        # executa SEMPRE, com ou sem exceção
        print("Tentativa de leitura concluída")

# Capturar múltiplas exceções
try:
    resultado = dados[chave]
except (KeyError, IndexError) as e:
    print(f"Erro de acesso: {e}")

# Relançar exceção
try:
    chamar_api()
except TimeoutError as e:
    log.error(f"Timeout: {e}")
    raise   # relança a mesma exceção

# Exceções customizadas
class ErroDeNegocio(Exception):
    """Erros esperados do domínio da aplicação."""
    pass

class ScoreInvalido(ErroDeNegocio):
    def __init__(self, valor: float) -> None:
        self.valor = valor
        super().__init__(f"Score deve estar entre 0 e 10, recebeu {valor}")

def validar_score(score: float) -> None:
    if not 0 <= score <= 10:
        raise ScoreInvalido(score)

try:
    validar_score(15.0)
except ScoreInvalido as e:
    print(f"Erro: {e}")         # "Erro: Score deve estar entre 0 e 10, recebeu 15.0"
    print(f"Valor: {e.valor}")  # 15.0

# Context manager para tratamento de recursos (com __enter__ e __exit__)

# O "with" garante que recursos sejam liberados mesmo com exceções

# Arquivo — o jeito correto
with open("arquivo.txt", "r") as f:
    conteudo = f.read()
# f.close() é chamado automaticamente

# Criando seu próprio context manager
from contextlib import contextmanager

@contextmanager
def cronometrar(nome: str):
    import time
    inicio = time.time()
    try:
        yield              # executa o bloco "with"
    finally:
        fim = time.time()
        print(f"{nome}: {fim - inicio:.3f}s")

with cronometrar("processar dados"):
    processar_dados(10_000)
# processar dados: 0.002s

# Com classe (mais verboso, mas mais controle)
class ConexaoDB:
    def __enter__(self):
        self.conn = conectar()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return False  # não suprime exceções

with ConexaoDB() as conn:
    conn.executar("SELECT ...")