from typing import Optional, Union, Any, Callable
from collections.abc import Sequence, Mapping

# Básicos — Python 3.9+, sem precisar importar de typing
def processar(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# Optional — pode ser None (Python 3.10+: use | None)
def buscar(id: int) -> dict | None:      # moderno
    ...
def buscar_v2(id: int) -> Optional[dict]:  # equivalente, mais antigo
    ...

# Union — pode ser um ou outro tipo
def formatar(valor: int | float | str) -> str:
    return str(valor)

# Callable — tipo para funções
def aplicar(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# TypeVar — para generics
from typing import TypeVar
T = TypeVar("T")

def primeiro(items: list[T]) -> T | None:
    return items[0] if items else None

primeiro([1, 2, 3])       # retorna int
primeiro(["a", "b"])      # retorna str

# TypedDict — dict com estrutura definida
from typing import TypedDict

class UsuarioDict(TypedDict):
    nome: str
    email: str
    score: float
    ativo: bool

def criar_usuario(dados: UsuarioDict) -> UsuarioDict:
    return dados

# Literal — valor específico
from typing import Literal

Ambiente = Literal["development", "staging", "production"]

def configurar(env: Ambiente) -> None:
    ...

configurar("production")   # ✅
configurar("prod")         # ❌ mypy vai reclamar

# Protocol — duck typing com tipo (Python 3.8+)
from typing import Protocol

class Serializable(Protocol):
    def to_dict(self) -> dict: ...
    def to_json(self) -> str: ...

def salvar(objeto: Serializable) -> None:  # aceita qualquer classe que implemente
    dados = objeto.to_dict()
    