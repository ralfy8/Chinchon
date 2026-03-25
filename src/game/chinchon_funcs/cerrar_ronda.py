from game.chinchon_funcs.mostrar_resumen_ronda import mostrar_resumen_ronda
from game.chinchon_funcs.calcular_y_mostrar_puntuaciones import calcular_y_mostrar_puntuaciones
from game.chinchon_funcs.procesar_eliminaciones_y_ganador import procesar_eliminaciones_y_ganador
from game.chinchon_funcs.aplicar_penalizacion_comodines_no_usados import aplicar_penalizacion_comodines_no_usados


def cerrar_ronda(game, jugador_cierra):
    game.limpiar()
    # Al cerrar, el jugador elige una carta para tirar
    game._procesar_descarte(jugador_cierra)
    mostrar_resumen_ronda(game, jugador_cierra)
    calcular_y_mostrar_puntuaciones(game)
    resultado = procesar_eliminaciones_y_ganador(game, game.limpiar, game.escribir, game.colores)

    if resultado == "fin" and len(game.jugadores) == 1:
        ganador = game.jugadores[0]
        aplicar_penalizacion_comodines_no_usados(game, ganador)

    return resultado
