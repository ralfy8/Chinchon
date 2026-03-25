from game.chinchon_funcs.mano_valida import mano_valida


def avisar_mano_valida(game, jugador):
    game.escribir("\nTus cartas:", game.colores["amarillo"])
    for i, carta in enumerate(jugador.mano):
        game.escribir(f"{i+1}. {game._formatear_carta(carta)}")
    
    if mano_valida(jugador.mano):
        game.escribir("Tu mano es válida.", game.colores["verde"])
    else:
        game.escribir("Tu mano NO es válida.", game.colores["rojo"])
