def detectar_grupos(cartas):
    """
    Detecta grupos válidos en una lista de cartas.
    Un grupo es:
        - 3 o más cartas
        - mismo valor
        - palos distintos
    Los comodines pueden usarse para completar grupos.
    """
    from validation.validador_funcs.filtrar_normales import filtrar_normales

    cartas_normales = filtrar_normales(cartas)
    comodines = [c for c in cartas if c.tipo == "comodin"]
    num_comodines = len(comodines)

    valores = {}
    for carta in cartas_normales:
        valores.setdefault(carta.valor, []).append(carta)

    grupos = []

    for valor, grupo in valores.items():
        size = len(grupo)
        if size >= 3:
            grupos.append(grupo)
        elif size == 2 and num_comodines >= 1:
            grupos.append(grupo)  # usa 1 comodín
        elif size == 1 and num_comodines >= 2:
            grupos.append(grupo)  # usa 2 comodines
        # No agregar si size=0, comodines solos no cuentan

    return grupos