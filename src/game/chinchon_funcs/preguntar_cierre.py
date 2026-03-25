def preguntar_cierre(game, jugador):
    # Verificar si tiene al menos una carta de valor <= 3
    tiene_carta_baja = any(c.valor <= 3 for c in jugador.mano if c.tipo != "comodin")
    if not tiene_carta_baja:
        game.escribir("No puedes cerrar la ronda porque no tienes una carta de valor 3 o inferior.", game.colores["rojo"])
        return False

    while True:
        game.escribir(f"{jugador.nombre}, ¿quieres cerrar la ronda?", game.colores["amarillo"])
        opcion = input("Escribe S para cerrar, o ENTER para seguir: ").strip().lower()
        if opcion == "" or opcion == "s":
            return opcion == "s"
        game.escribir("Opción inválida. Solo ENTER o S están permitidos.", game.colores["rojo"])
