class jugador:
	nombre = ''
	velocidadCarrera = 0
	porcentajeDeAciertos = 0
	velocidadImpacto = 0
	posicionImpacto = [0,0]
	velocidadPrimerSaque = 0
	porcentajePrimerSaque = 0
	velocidadSegundoSaque = 0
	porcentajeSegundoSaque = 0

cantidadDeJugadores = input('¿Cuántos jugadores vas a cargar? ')

listaDeJugadores
i = 0

while (i < cantidadDeJugadores):
	listaDeJugadores[i] = jugador()
	listaDeJugadores[i].nombre = input('Nombre del jugador i')
	listaDeJugadores[i].velocidadCarrera = input
