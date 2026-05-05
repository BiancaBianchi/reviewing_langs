from pathlib import Path
import json
import os
from dotenv import load_dotenv   # pip install python-dotenv

# Leitura de arquivos
caminho = Path("dados.txt")

conteudo = caminho.read_text(encoding="utf-8")              # arquivo inteiro
linhas = caminho.read_text(encoding="utf-8").splitlines()   # lista de linhas

# Escrita
Path("saida.txt").write_text("conteúdo aqui", encoding="utf-8")

# Para arquivos grandes — linha por linha
with open("grande.csv", "r", encoding="utf-8") as f:
    for linha in f:                    # não carrega tudo na memória
        processar(linha.strip())

# JSON
dados = {"nome": "Bianca", "score": 9.5, "tags": ["ai", "backend"]}

# Serializar
json_str = json.dumps(dados, ensure_ascii=False, indent=2)
Path("dados.json").write_text(json_str, encoding="utf-8")

# Desserializar
texto = Path("dados.json").read_text(encoding="utf-8")
dados = json.loads(texto)

# Atalho: ler/escrever direto em arquivo
with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Variáveis de ambiente — nunca coloque secrets no código!
# Arquivo .env (nunca commite esse arquivo):
# API_KEY=sk-123...
# DATABASE_URL=postgresql://...
# AMBIENTE=production

load_dotenv()   # carrega o .env

api_key = os.getenv("API_KEY")                    # None se não existir
db_url = os.getenv("DATABASE_URL", "sqlite:///")  # valor padrão
ambiente = os.environ["AMBIENTE"]                 # KeyError se não existir

# Padrão moderno: pydantic-settings (você vai usar no FastAPI)
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    database_url: str
    ambiente: str = "development"
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
print(settings.api_key)       # lê do .env ou variável de ambiente
print(settings.ambiente)      # "development" se não definido