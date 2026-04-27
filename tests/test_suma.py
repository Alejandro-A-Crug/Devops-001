"""
Este módulo contiene el testing unitario para la funcion suma
"""

from miapp import suma  # cambia por el nombre real del archivo


def test_suma_positivos():
    """
    Este módulo contiene el testing unitario para suma de positivos
    """
    assert suma(2, 3) == 5

def test_suma_negativos():
    """
    Este módulo contiene el testing unitario para suma de negativos
    """
    assert suma(-1, -1) == -2

def test_suma_mixto():
    """
    Este módulo contiene el testing unitario para suma de mixtos
    """
    assert suma(-1, 1) == 0
