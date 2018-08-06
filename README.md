# Tenissimulator
Estos programas simulan partidos de tenis (sin ventajas en los games, es decir, que si van "40-40" el siguiente punto define el game) entre dos jugadores donde están predeterminados dos aspectos:

- La probabilidad que tiene el jugador 1 de ganar cada punto frente al jugador 2 (performancePuntoNormal).
- La probabilidad que tiene el jugador 1 de ganar un "40-40" frente al jugador 2 (performancePuntoDefinitivo).

El tenisSimulator_v.1 itera sobre performancePuntoNormal, mientras que performancePuntoDefinitivo se mantiene fijo.
El tenisSiumlator_v.2 itera sobre performancePuntoDefinitivo, dejando fijo performancePuntoNormal.

Estos programas devuelven un gráfico de los partidos ganados por el jugador 1 vs performancePuntoNormal o performancePuntoDefinitivo, según el programa ejecutado.

Los valores predeterminados en tenisSimulator_v.1 son:

- performancePuntoDefinitivo = 70 (es decir que el jugador 1 tiene un 70% de chances de ganar los "40-40" frente al jugador 2).
- performancePuntoNormalMinima = 0
- performancePuntoNormalMaxima = 100 
- intervalo = 1 (el programa va a simular partidos tomando como performancePuntoNormal desde 0 a 100 de uno en uno).
- cantidadPartidos = 2000 (cantidad de partidos jugados en cada iteración).


Los valores predeterminados en tenisSimulator_v.1 son:

- performancePuntoNormal = 70 (es decir que el jugador 1 tiene un 70% de chances de ganar los "40-40" frente al jugador 2).
- performancePuntoDefinitivoMinima = 0
- performancePuntoDefinitivoMaxima = 100 
- intervalo = 1 (el programa va a simular partidos tomando como performancePuntoDefinitivo desde 0 a 100 de uno en uno).
- cantidadPartidos = 2000 (cantidad de partidos jugados en cada iteración).

Estos valores pueden modificarse a gusto y no alteran el funcionamiento del programa.
