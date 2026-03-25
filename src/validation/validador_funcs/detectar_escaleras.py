def detectar_escaleras(cartas):
    """
    Detecta escaleras válidas en una lista de cartas.
    Una escalera es:
        - 3 o más cartas
        - mismo palo
        - valores consecutivos
    Los comodines pueden usarse para completar huecos en las escaleras.
    """
    from validation.validador_funcs.filtrar_normales import filtrar_normales

    cartas_normales = filtrar_normales(cartas)
    comodines = [c for c in cartas if c.tipo == "comodin"]
    num_comodines = len(comodines)

    # Agrupar por palo
    palos = {}
    for carta in cartas_normales:
        palos.setdefault(carta.palo, []).append(carta)

    escaleras = []

    for palo, grupo in palos.items():
        if len(grupo) + num_comodines < 3:
            continue
        grupo_ordenado = sorted(grupo, key=lambda c: c.valor)
        # Calcular huecos
        huecos = 0
        for i in range(1, len(grupo_ordenado)):
            huecos += grupo_ordenado[i].valor - grupo_ordenado[i-1].valor - 1
        if huecos <= num_comodines:
            # La escalera usa len(grupo) + (huecos) comodines, pero mínimo 3
            total_cartas = len(grupo) + min(huecos, num_comodines)
            if total_cartas >= 3:
                escaleras.append(grupo_ordenado)  # simplificado

    return escaleras