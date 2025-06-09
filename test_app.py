"""
Arquivo de teste para as funções do módulo `app`.

Este arquivo contém testes unitários para as funções `soma`, `multiplicacao`,
e `concatena`, cobrindo casos de uso básicos e casos de borda.
"""
from app import soma, multiplicacao, concatena


def test_soma_positivos():
    """Testa a soma de dois números positivos."""
    assert soma(2, 3) == 5


def test_soma_negativos():
    """Testa a soma de dois números negativos."""
    assert soma(-5, -10) == -15

def test_multiplicacao_positivos():
    """Testa a multiplicação de dois números positivos."""
    assert multiplicacao(4, 5) == 20

def test_multiplicacao_negativos():
    """Testa a multiplicação de dois números negativos."""
    assert multiplicacao(-3, -6) == 18

def test_concatena_strings_simples():
    """Testa a concatenação de duas strings."""
    assert concatena("ola", "mundo") == "olamundo"


def test_concatena_com_string_vazia():
    """Testa a concatenação de uma string com uma string vazia."""
    assert concatena("teste", "") == "teste"
