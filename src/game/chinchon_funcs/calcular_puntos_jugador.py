def calcular_puntos_jugador(jugador):
    from validation.validador import detectar_escaleras
    normales = [c for c in jugador.mano if c.tipo != "comodin"]
    comodines = [c for c in jugador.mano if c.tipo == "comodin"]
    num_comodines = len(comodines)

    # Verificar Chinchón
    escaleras = detectar_escaleras(jugador.mano)
    for escalera in escaleras:
        # Para Chinchón, verificar si con comodines se llega a 7 consecutivas
        grupo = escalera  # lista de cartas normales
        if len(grupo) + num_comodines >= 7:
            # Calcular huecos
            valores = sorted(c.valor for c in grupo)
            huecos = sum(valores[i+1] - valores[i] - 1 for i in range(len(valores)-1))
            if huecos <= num_comodines:
                return -10

    return sum(c.valor for c in normales)
