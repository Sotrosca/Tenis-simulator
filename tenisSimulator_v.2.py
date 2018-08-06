import random
import matplotlib.pyplot as plt
import numpy as np

class player:
	name = "Ricarlos"
	performance = [50, 50] # El primer elemento determina la probabilidad de ganar un punto contra su rival, mientras que el segundo elemento determina la probabilidad de ganar un "40-40" contra su rival.
	gamePoints = 0
	games = 0
	sets = 0
	matches = 0

	def performanceEspecial(self, jugador2):
		if (self.gamePoints == 3) & (jugador2.gamePoints == 3):
			return self.performance [1]
		else:
			return self.performance [0]


playerOne = player()
playerOne.name = "Ricarlos"
playerTwo = player()
playerTwo.name = "Estelaura"

class game:

	def jugarGame(self, jugador1, jugador2):
		while (jugador1.gamePoints < 4) & (jugador2.gamePoints < 4):
			numeroGanador = random.randint(1,100)
			if (numeroGanador <= jugador1.performanceEspecial(jugador2)):
				jugador1.gamePoints = jugador1.gamePoints + 1
			else:
				jugador2.gamePoints = jugador2.gamePoints + 1		
		if (jugador1.gamePoints > jugador2.gamePoints):
			jugador1.games = jugador1.games + 1
			jugador1.gamePoints = 0
			jugador2.gamePoints = 0
		else:
			jugador2.games = jugador2.games + 1
			jugador1.gamePoints = 0
			jugador2.gamePoints = 0

class set(game):

	def jugarSet(self, jugador1, jugador2):
		while (jugador1.games < 6) & (jugador2.games < 6):
			self.jugarGame(jugador1, jugador2)
		if (jugador1.games > jugador2.games):
			jugador1.sets = jugador1.sets + 1
			jugador1.games = 0
			jugador2.games = 0
		else:
			jugador2.sets = jugador2.sets + 1
			jugador1.games = 0
			jugador2.games = 0

class match(set):
	matchType = 2 # Cantidad de sets que debe ganar un jugador para ganar el partido.

	def jugarMatch(self, jugador1,jugador2):
		while (jugador1.sets < self.matchType) & (jugador2.sets < self.matchType):
			self.jugarSet(jugador1, jugador2)
		if (jugador1.sets > jugador2.sets):
			jugador1.matches = jugador1.matches + 1
			jugador1.sets = 0
			jugador2.sets = 0
		else:
			jugador2.matches = jugador2.matches + 1
			jugador1.sets = 0
			jugador2.sets = 0

matchOne = match()
performancePuntoDefinitivo = 50 # Es la probabilidad de ganar un "40-40" para el jugador1.
performancePuntoNormalMinima = 0 # Valor inicial de la iteración del programa.
performancePuntoNormalMaxima = 100 # Valor final de la iteración del programa.
intervalo = 1 
cantidadPartidos = 2000 # Cantidad de partidos jugados en cada iteración.
partidos = []
j = performancePuntoNormalMinima

while (j < (performancePuntoNormalMaxima + 1)):
	i = 1
	playerOne.performance = [j, performancePuntoDefinitivo]
	while (i < cantidadPartidos):
		matchOne.jugarMatch(playerOne,playerTwo)
		i = i + 1
	partidos.append(playerOne.matches)
	playerOne.matches = 0
	playerTwo.matches = 0
	j = j + intervalo

dominio = np.arange(performancePuntoNormalMinima, performancePuntoNormalMaxima + 1,intervalo)
plt.show(plt.plot(dominio, np.array(partidos)))
