import random

class player:
	name = "Ricarlos"
	performance = [42, 100]
	gamePoints = 0
	games = 0
	sets = 0
	matches = 0

	def performanceEspecial(self, jugador2):
		if (self.gamePoints == 3) & (jugador2.gamePoints == 3):
			return self.performance[1]
		else:
			return self.performance[0]

playerOne = player()
playerOne.name = "Ricarlos"
playerTwo = player()
playerTwo.name = "Estelaura"

class game:
	gameName = 1

	def jugarGame(self, jugador1, jugador2):
		while (jugador1.gamePoints < 4) & (jugador2.gamePoints < 4):
			numeroGanador = random.randint(1,100)
			if (numeroGanador <= jugador1.performanceEspecial(jugador2)):
				jugador1.gamePoints = jugador1.gamePoints + 1
				#print(jugador1.name, str(jugador1.gamePoints), jugador2.name, str(jugador2.gamePoints))
			else:
				jugador2.gamePoints = jugador2.gamePoints + 1
				#print(jugador1.name, str(jugador1.gamePoints), jugador2.name, str(jugador2.gamePoints))
		if (jugador1.gamePoints > jugador2.gamePoints):
			jugador1.games = jugador1.games + 1
			jugador1.gamePoints = 0
			jugador2.gamePoints = 0
		else:
			jugador2.games = jugador2.games + 1
			jugador1.gamePoints = 0
			jugador2.gamePoints = 0

class set(game):
	setName = 1

	def jugarSet(self, jugador1, jugador2):
		while (jugador1.games < 6) & (jugador2.games < 6):
			self.jugarGame(jugador1, jugador2)
		if (jugador1.games > jugador2.games):
			jugador1.sets = jugador1.sets + 1
			#print(jugador1.name, str(jugador1.games), jugador2.name, str(jugador2.games))
			jugador1.games = 0
			jugador2.games = 0
		else:
			jugador2.sets = jugador2.sets + 1
			#print(jugador1.name, str(jugador1.games), jugador2.name, str(jugador2.games))
			jugador1.games = 0
			jugador2.games = 0

class match(set):
	matchName = 1
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
#gameOne = game()
#gameOne.jugarGame(playerOne,playerTwo)
#print([playerOne.games, playerTwo.games])

#setOne = set()
#setOne.jugarSet(playerOne,playerTwo)
#print([playerOne.sets, playerTwo.sets])

matchOne = match()

i = 0


while (i < 10000):
	matchOne.jugarMatch(playerOne, playerTwo)
	i = i + 1

print ([playerOne.matches, playerTwo.matches])

#j = 50
#partidos = []
#while (j < 101):
#	i = 1
#	playerOne.performance = j
#	while (i < 10001):
#		matchOne.jugarMatch(playerOne,playerTwo)
#		i = i + 1
#	partidos.append([[j], [playerOne.matches, playerTwo.matches]])
#	playerOne.matches = 0
#	playerTwo.matches = 0
#	j = j + 1

#print(partidos)