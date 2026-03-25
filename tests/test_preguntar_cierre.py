# tests/test_preguntar_cierre.py
# Test para verificar que preguntar_cierre solo acepte ENTER o S/s

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pytest
from model.jugador import Jugador
from model.carta import Carta
from game.chinchon_funcs.preguntar_cierre import preguntar_cierre


def test_preguntar_cierre_acepta_enter(monkeypatch):
    """Test que verifica que ENTER (vacío) se acepta y retorna False (no cerrar)."""

    def mock_escribir(texto, color=None):
        pass

    class MockGame:
        def escribir(self, texto, color=None):
            pass
        colores = {"amarillo": "", "rojo": ""}

    game = MockGame()
    jugador = Jugador("Test")
    # Agregar carta baja para poder cerrar
    jugador.recibir_cartas([Carta("oros", 1)])

    # Simular entrada ENTER (vacío)
    monkeypatch.setattr("builtins.input", lambda prompt="": "")

    resultado = preguntar_cierre(game, jugador)
    assert resultado is False


def test_preguntar_cierre_acepta_s_minuscula(monkeypatch):
    """Test que verifica que 's' se acepta y retorna True (cerrar)."""

    def mock_escribir(texto, color=None):
        pass

    class MockGame:
        def escribir(self, texto, color=None):
            pass
        colores = {"amarillo": "", "rojo": ""}

    game = MockGame()
    jugador = Jugador("Test")
    # Agregar carta baja
    jugador.recibir_cartas([Carta("oros", 1)])

    # Simular entrada 's'
    monkeypatch.setattr("builtins.input", lambda prompt="": "s")

    resultado = preguntar_cierre(game, jugador)
    assert resultado is True


def test_preguntar_cierre_acepta_s_mayuscula(monkeypatch):
    """Test que verifica que 'S' se acepta y retorna True (cerrar)."""

    def mock_escribir(texto, color=None):
        pass

    class MockGame:
        def escribir(self, texto, color=None):
            pass
        colores = {"amarillo": "", "rojo": ""}

    game = MockGame()
    jugador = Jugador("Test")
    # Agregar carta baja
    jugador.recibir_cartas([Carta("oros", 1)])

    # Simular entrada 'S'
    monkeypatch.setattr("builtins.input", lambda prompt="": "S")

    resultado = preguntar_cierre(game, jugador)
    assert resultado is True


def test_preguntar_cierre_rechaza_otras_entradas(monkeypatch):
    """Test que verifica que entradas inválidas se rechazan y se pide de nuevo."""

    def mock_escribir(texto, color=None):
        pass

    class MockGame:
        def escribir(self, texto, color=None):
            pass
        colores = {"amarillo": "", "rojo": ""}

    game = MockGame()
    jugador = Jugador("Test")
    # Agregar carta baja
    jugador.recibir_cartas([Carta("oros", 1)])

    # Simular entradas: primero inválida, luego válida
    inputs = iter(["x", "invalid", "s"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    resultado = preguntar_cierre(game, jugador)
    assert resultado is True  # Finalmente acepta 's'


def test_preguntar_cierre_sin_carta_baja(monkeypatch):
    """Test que verifica que no se puede cerrar sin carta de valor <=3."""

    def mock_escribir(texto, color=None):
        pass

    class MockGame:
        def escribir(self, texto, color=None):
            pass
        colores = {"amarillo": "", "rojo": ""}

    game = MockGame()
    jugador = Jugador("Test")
    # Agregar cartas sin baja (valor >3)
    jugador.recibir_cartas([Carta("oros", 4), Carta("copas", 5)])

    resultado = preguntar_cierre(game, jugador)
    assert resultado is False