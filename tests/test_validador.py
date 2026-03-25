import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from model.carta import Carta
from validation.validador import detectar_escaleras, detectar_grupos, es_chinchon


def test_detectar_escaleras():
    cartas = [
        Carta("oros", 2), Carta("oros", 3), Carta("oros", 4), Carta("oros", 5),
        Carta("copas", 7), Carta("espadas", 10), Carta("bastos", 12)
    ]

    escaleras = detectar_escaleras(cartas)

    assert len(escaleras) == 1
    assert len(escaleras[0]) == 4
    assert [c.valor for c in escaleras[0]] == [2, 3, 4, 5]


def test_detectar_grupos():
    cartas = [
        Carta("oros", 7), Carta("copas", 7), Carta("espadas", 7),
        Carta("bastos", 1), Carta("oros", 2), Carta("copas", 3), Carta("espadas", 4)
    ]

    grupos = detectar_grupos(cartas)

    assert len(grupos) == 1
    assert len(grupos[0]) == 3
    assert all(c.valor == 7 for c in grupos[0])


def test_es_chinchon_valido():
    cartas = [
        Carta("oros", 1), Carta("oros", 2), Carta("oros", 3), Carta("oros", 4),
        Carta("oros", 5), Carta("oros", 6), Carta("oros", 7)
    ]

    assert es_chinchon(cartas) is True


def test_es_chinchon_invalido():
    cartas = [
        Carta("oros", 1), Carta("oros", 2), Carta("oros", 3), Carta("oros", 4),
        Carta("oros", 5), Carta("copas", 6), Carta("oros", 7)
    ]

    assert es_chinchon(cartas) is False


def test_chinchon_con_comodin():
    from model.jugador import Jugador
    from game.chinchon_funcs.calcular_puntos_jugador import calcular_puntos_jugador

    # Crear comodín
    class Comodin:
        def __init__(self):
            self.tipo = "comodin"
            self.nombre = "test"
            self.valor = None
            self.palo = None

    jugador = Jugador("Test")
    cartas = [
        Carta("oros", 1), Carta("oros", 2), Carta("oros", 3), Carta("oros", 4),
        Carta("oros", 5), Carta("oros", 7), Comodin()
    ]
    jugador.mano = cartas

    puntos = calcular_puntos_jugador(jugador)
    assert puntos == -10, f"Esperado -10, obtenido {puntos}"
