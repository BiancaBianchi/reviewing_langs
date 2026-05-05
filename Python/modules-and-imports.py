# Importar módulo inteiro
import os
import json
import pathlib

os.getcwd()           # diretório atual
os.path.join("a", "b")  # "a/b" (cross-platform)

# Importar específico
from datetime import datetime, timedelta
from pathlib import Path

agora = datetime.now()
amanha = agora + timedelta(days=1)

caminho = Path("/home/bianca/projetos")
caminho.exists()         # True/False
caminho / "app" / "main.py"   # Path join com /  ✅

# Alias
import numpy as np                  # convenção da comunidade
import pandas as pd
from typing import Optional as Opt

# Evitar import *
from modulo import *   # ❌ polui o namespace, difícil de debugar

# Organização de um projeto Python
#
# meu_projeto/
# ├── src/
# │   └── meu_pacote/
# │       ├── __init__.py       ← torna a pasta um pacote
# │       ├── models.py
# │       ├── services.py
# │       └── utils.py
# ├── tests/
# │   ├── __init__.py
# │   └── test_services.py
# ├── pyproject.toml            ← config moderna (substitui setup.py)
# └── README.md

# __init__.py — controla o que é exportado
# Em meu_pacote/__init__.py:
from .models import Usuario, Evento
from .services import processar

# Agora de fora você pode:
from meu_pacote import Usuario, processar

# Importações relativas (dentro do pacote)
from .models import Usuario         # mesmo pacote
from ..utils import formatar        # pacote pai