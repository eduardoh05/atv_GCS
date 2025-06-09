"""
Este módulo contém funções matemáticas e de manipulação de strings.
"""
from typing import Union

# Define um tipo para aceitar tanto inteiros quanto floats
Numero = Union[int, float]


def soma(a: Numero, b: Numero) -> Numero:
    """
    Soma dois números (inteiros ou floats).

    Args:
        a (Numero): O primeiro número.
        b (Numero): O segundo número.

    Returns:
        Numero: O resultado da soma de a e b.
    """
    return a + b


def multiplicacao(a: Numero, b: Numero) -> Numero:
    """
    Multiplica dois números (inteiros ou floats).

    Args:
        a (Numero): O primeiro número.
        b (Numero): O segundo número.

    Returns:
        Numero: O resultado da multiplicação de a e b.
    """
    return a * b


def concatena(a: str, b: str) -> str:
    """
    Concatena duas strings.

    Args:
        a (str): A primeira string.
        b (str): A segunda string.

    Returns:
        str: A string resultante da concatenação de a e b.
    """
    return a + b
