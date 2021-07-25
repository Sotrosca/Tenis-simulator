# Tenissimulator
Implementación de un simulador estadístico de partidos de tenis.

Los partidos se simulan instanciando la clase Match con la cantidad deseada de sets a ganar para terminar el partido y con la función que simulará la probabilidad de ganar cada punto del primer jugador, luego ejecutar el método play_full_match().

Los scripts "totally_even_players.py" y "worst_on_decisisve_games_simulation.py" simulan varios partidos con distintas funciones de probabilidad y crean un dataframe que puede ser utilizado para analizar la distribución de resultados posibles del partido.

"totally_even_players.py" simula varios partidos donde ambos jugadores tienen la misma probabilidad de ganar cada punto que se juega.

"worst_on_decisisve_games_simulation.py" simula varios partidos donde el jugador 0 es levemente superior salvo a partir de que el set se pone (4, 4), donde el jugador 1 es el que empieza a "jugar mejor".

Esto se puede usar para simular partidos de jugadores que ceden ante la presión en momentos de definición o al contrario, que se vuelven fuertes en los momentos importantes.

La clase Score es independiente del resto del desarrollo y simula un marcador de tenis. Puede utilizarse fuera de este trabajo.

Por último el script get_matches_info.py consume un servicio de la API "Tennis Live Data" hosteada en "https://rapidapi.com/".

Este servicio devuelve los resultados de los partidos del torneo pasado por parámetro, que se puede utilizar para comparar los resultados obtenidos por el simulador.

Los parámetros necesarios para conectarse a la API deberán ser seteados en el archivo "x-rapidapi-key.json".

Todavía cosas por realizar, ante cualquier sugerencia o aporte que quieras realizar no dudes en contactarme a mi mail "facuserna93@gmail.com".