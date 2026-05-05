# pip install pytest pytest-asyncio

# test_services.py
import pytest
from unittest.mock import Mock, patch, AsyncMock

# Teste básico — função deve começar com test_
def test_somar():
    assert somar(2, 3) == 5

def test_somar_negativos():
    assert somar(-1, -1) == -2

# Teste de exceção
def test_score_invalido():
    with pytest.raises(ScoreInvalido) as exc_info:
        validar_score(15.0)
    assert exc_info.value.valor == 15.0

# Fixtures — setup reutilizável
@pytest.fixture
def usuario_exemplo():
    return Usuario(nome="Bianca", email="bi@email.com")

@pytest.fixture
def db_teste():
    db = criar_db_em_memoria()
    yield db          # código antes do yield = setup
    db.fechar()       # código depois = teardown

def test_usuario_score(usuario_exemplo):    # fixture injetada automaticamente
    usuario_exemplo.score = 9.5
    assert usuario_exemplo.score == 9.5

# Parametrize — roda o mesmo teste com dados diferentes
@pytest.mark.parametrize("score,esperado", [
    (10.0, True),
    (0.0,  True),
    (5.5,  True),
    (-1.0, False),
    (10.1, False),
])
def test_score_valido(score, esperado):
    if esperado:
        validar_score(score)   # não levanta exceção
    else:
        with pytest.raises(ScoreInvalido):
            validar_score(score)

# Mock — substitui dependências externas
def test_chamar_api_com_mock():
    with patch("meu_modulo.httpx.get") as mock_get:
        mock_get.return_value.json.return_value = {"id": 1, "nome": "Bianca"}
        mock_get.return_value.status_code = 200

        resultado = chamar_api(1)

        mock_get.assert_called_once_with("https://api.exemplo.com/users/1")
        assert resultado["nome"] == "Bianca"

# Teste async
@pytest.mark.asyncio
async def test_buscar_usuario_async():
    mock_response = Mock()
    mock_response.json.return_value = {"id": 1}

    with patch("meu_modulo.httpx.AsyncClient") as mock_client:
        mock_client.return_value.__aenter__.return_value.get = AsyncMock(
            return_value=mock_response
        )
        resultado = await buscar_usuario(1)
        assert resultado["id"] == 1