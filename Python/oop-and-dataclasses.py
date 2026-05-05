#------------ Basic classes ------------

class Usuario:
    # Variável de classe — compartilhada por todas as instâncias
    total_usuarios: int = 0

    def __init__(self, nome: str, email: str) -> None:
        # Variáveis de instância
        self.nome = nome
        self.email = email
        self._score: float = 0.0   # convenção: _ = "privado" (não forçado)
        Usuario.total_usuarios += 1

    # Método de instância
    def saudar(self) -> str:
        return f"Olá, sou {self.nome}"

    # Property — acesso como atributo, lógica como método
    @property
    def score(self) -> float:
        return self._score

    @score.setter
    def score(self, valor: float) -> None:
        if not 0 <= valor <= 10:
            raise ValueError(f"Score deve estar entre 0 e 10, recebeu {valor}")
        self._score = valor

    # Representação em string
    def __repr__(self) -> str:
        return f"Usuario(nome={self.nome!r}, email={self.email!r})"

    def __str__(self) -> str:
        return f"{self.nome} <{self.email}>"

    # Método de classe — alternativa ao __init__
    @classmethod
    def de_dict(cls, dados: dict) -> "Usuario":
        return cls(dados["nome"], dados["email"])

    # Método estático — não acessa self nem cls
    @staticmethod
    def validar_email(email: str) -> bool:
        return "@" in email and "." in email

# Uso
u = Usuario("Bianca", "bi@email.com")
u.score = 9.5           # usa o setter
print(u.score)          # usa o getter
print(u)                # "Bianca <bi@email.com>"  — usa __str__
print(repr(u))          # "Usuario(nome='Bianca', email='bi@email.com')"

u2 = Usuario.de_dict({"nome": "Ana", "email": "ana@email.com"})
Usuario.validar_email("invalido")  # False

#------------ Herança ------------

class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def falar(self) -> str:
        raise NotImplementedError("Subclasse deve implementar falar()")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nome={self.nome!r})"

class Cachorro(Animal):
    def falar(self) -> str:
        return "Au!"

    def buscar(self) -> str:
        return f"{self.nome} foi buscar!"

class Gato(Animal):
    def __init__(self, nome: str, indoor: bool = True) -> None:
        super().__init__(nome)       # chama __init__ do pai
        self.indoor = indoor

    def falar(self) -> str:
        return "Miau!"

# Polimorfismo
animais: list[Animal] = [Cachorro("Rex"), Gato("Mimi")]
for animal in animais:
    print(f"{animal.nome}: {animal.falar()}")   # chama o método correto de cada um

#------------ Dataclasses ------------

# Elimina boilerplate de __init__, __repr__, __eq__. Use sempre que a classe é principalmente um container de dados.

from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Evento:
    nome: str
    descricao: str
    score_impacto: float
    tags: list[str] = field(default_factory=list)   # mutável — usa field()
    criado_em: datetime = field(default_factory=datetime.now)
    ativo: bool = True

    # Você ainda pode adicionar métodos
    def resumo(self) -> str:
        return f"{self.nome} (score: {self.score_impacto})"

    # Validação pós-init
    def __post_init__(self) -> None:
        if not 0 <= self.score_impacto <= 10:
            raise ValueError(f"Score inválido: {self.score_impacto}")

# O que você ganha de graça:
e1 = Evento("Latência reduzida", "De 30s para 11s", 9.0, ["performance", "copiloto"])
e2 = Evento("Latência reduzida", "De 30s para 11s", 9.0, ["performance", "copiloto"])

print(e1)        # Evento(nome='Latência reduzida', ...) — __repr__ automático
print(e1 == e2)  # True — __eq__ automático (compara todos os campos)

# Frozen — imutável (boa prática para configs e value objects)
@dataclass(frozen=True)
class ConfigLLM:
    modelo: str = "claude-sonnet-4-20250514"
    temperatura: float = 0.7
    max_tokens: int = 1000

config = ConfigLLM()
config.temperatura = 0.9   # ❌ FrozenInstanceError