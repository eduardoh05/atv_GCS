import pytest
from app import soma, multiplicacao, concatena

def test_soma_positivos():
    assert soma(2, 3) == 5

def test_multiplicacao_positivos():
    assert multiplicacao(2, 3) == 6

def test_concatena_strings():
    assert concatena("", "bar") == "foobar"
