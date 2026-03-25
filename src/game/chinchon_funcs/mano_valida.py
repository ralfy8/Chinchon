from validation.validador import detectar_grupos, detectar_escaleras, _filtrar_normales


def mano_valida(cartas):
    """Determina si una mano es válida para cerrar."""
    normales = _filtrar_normales(cartas)

    grupos = detectar_grupos(cartas)
    escaleras = detectar_escaleras(cartas)
    total_normales_usadas = sum(len(g) for g in grupos) + sum(len(e) for e in escaleras)

    return total_normales_usadas == len(normales)
