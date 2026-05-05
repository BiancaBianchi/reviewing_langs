# Gerenciamento de ambiente virtual
python -m venv .venv          # cria ambiente virtual
source .venv/bin/activate     # ativa (Linux/Mac)
.venv\Scripts\activate        # ativa (Windows)
deactivate                    # desativa

# uv — substituto moderno e muito mais rápido do pip + venv
pip install uv
uv init meu-projeto          # cria projeto
uv add fastapi               # instala dependência
uv add --dev pytest ruff mypy  # dependência de dev
uv run pytest                # roda pytest no ambiente correto
uv sync                      # sincroniza dependências do pyproject.toml

# pyproject.toml — config moderna do projeto
[project]
name = "app-tea"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.100",
    "sqlalchemy>=2.0",
    "anthropic>=0.20",
    "pydantic-settings>=2.0",
]

[project.optional-dependencies]
dev = ["pytest", "pytest-asyncio", "ruff", "mypy"]

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "UP"]   # regras: erros, estilo, imports, naming, upgrade

[tool.mypy]
strict = true
python_version = "3.11"

[tool.pytest.ini_options]
asyncio_mode = "auto"

# Linting e formatação
ruff check .          # checa erros de estilo e bugs
ruff format .         # formata o código (substitui black)
ruff check --fix .    # auto-corrige o que der

# Type checking
mypy src/             # checa tipos
mypy --strict src/    # modo estrito

# Rodar testes
pytest                         # todos os testes
pytest tests/test_services.py  # arquivo específico
pytest -k "test_score"         # só testes com "score" no nome
pytest -v                      # verbose
pytest --cov=src               # com cobertura (pip install pytest-cov)