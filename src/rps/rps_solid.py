"""
Módulo del juego Piedra, Papel, Tijera, Lagarto, Spock.

Básicamente es la versión del juego popularizada por The Big Bang Theory.
La idea principal aquí es tener un Agente que no juegue totalmente al azar, sino que
intente aprender de tus patrones básicos, a través del historial
"""
import random
from enum import IntEnum
from collections import Counter



class GameAction(IntEnum):
    """
    Mapeo simple de acciones a números enteros.
    
    Usamos IntEnum para que las comparaciones sean más rápidas en vez de usar 
    strings por todas partes.
    """
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3  
    Spock = 4 


class GameResult(IntEnum):
    """Estados posibles al terminar una ronda."""
    Victory = 0
    Defeat = 1
    Tie = 2

Victories = {
    # Clave: La acción ganadora.
    # Valor: Lista de acciones a las que vence.
    GameAction.Rock: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Paper: [GameAction.Rock, GameAction.Spock],
    GameAction.Scissors: [GameAction.Paper, GameAction.Lizard],
    GameAction.Lizard: [GameAction.Spock, GameAction.Paper],
    GameAction.Spock: [GameAction.Scissors, GameAction.Rock]
}

class IntelligentAgent:
    """
    Un Agente intenta predecir que juagada vas usar para anticiparse a ella.

    Almacena simplemente el historial y toma la jugada frecuente
    """
    def __init__(self):
        self.history = []

    def record_move(self, move):
        """
        Almacena el movimiento del usuario
        
        Es fundamental llamar a esto después de cada input del usuario, 
        si no, el agente nunca aprenderá y jugará siempre random.

        Args:
            move (GameAction): La jugada que acaba de hacer el usuario
        """
        self.history.append(move)

    def get_move(self):
        """
        La siguiente jugada se basa en la frecuencia estadística.

        La estrategia es: 'Si el usuario saca Piedra, yo saco lo que gane a Piedra'.

        Returns:
            GameAction: La jugada elegida para intentar ganar.

        Note:
            Si el historial está vacío (ej: primera ronda), devuelve un random para no romper
            la lógica de 'Counter'.
            
            Si el usuario tiene varias jugadas favoritas empatadas (ej: 2 Piedras y 2 Papeles),
            `most_common` elegirá uno arbitrariamente
        """
        # Si hay datos, busca ganar a lo que más sacas
        if not self.history:
            selection = random.randint(0, len(GameAction) - 1)
            return GameAction(selection)
        
        #most_common(1) devuelve una lista [(Acción, Cantidad)]. 
        #[0][0] para extraer solo la Acción.
        most_common = Counter(self.history).most_common(1)[0][0]
        
        for action, losers in Victories.items():
            if most_common in losers:
                return action
        
        # Si por alguna razón no encontramos ->tiramos random.
        return GameAction(random.randint(0, len(GameAction) - 1))

my_agent = IntelligentAgent()

def assess_game(user_action, computer_action):
    """
    Compara las dos jugadas y decide quién gana la ronda.

    En lugar de comparar manualmente, consultamos el diccionario `Victories`. 

    Esto hace que el código sea escalable. Solo tocaríamos el diccionario

    Args:
        user_action (GameAction): Lo que ha elegido el usuario.
        computer_action (GameAction): Lo que ha elegido el agente.

    Returns:
        GameResult: El resultado final
    """
    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # AQUÍ CAMBIAMOS LOS IFs POR EL DICCIONARIO para cumplir OCP y SRP
    else:
        # Buscamos a quién gana el usuario
        beaten_by_user = Victories.get(user_action, [])                              
        if computer_action in beaten_by_user:
            print(f"{user_action.name} beats {computer_action.name}. You won!")
            game_result = GameResult.Victory
        else:
            print(f"{computer_action.name} beats {user_action.name}. You lost!")
            game_result = GameResult.Defeat
    return game_result


def get_computer_action(): 
    """
    Llama a la función del agente que determina su jugada y la muestra

    Returns:
        GameAction: La elección final del agente
    """
    computer_action = my_agent.get_move()
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    """
    Determina la decisión del usuario
    Returns:
        GameAction: Jugada del usuario
    Raises:
        ValueError: Para reiniciar el bucle si 
        el usuario escribe letras o números fuera de rango.
    """
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    
    valid_input = False
    user_action = None

    while not valid_input:
        try:
            user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
            # Validamos rango
            if 0 <= user_selection < len(GameAction):
                user_action = GameAction(user_selection)
                valid_input = True
            else:
                raise ValueError
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")

    # Guardo la jugada para que el agente "aprenda"
    my_agent.record_move(user_action)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():
    game_is_running = True                                        
    while game_is_running:
        # El try ya no hace falta porque get_user_action lo gestiona
        user_action = get_user_action()
        computer_action = get_computer_action()
        
        assess_game(user_action, computer_action)

        if not play_another_round():
            game_is_running = False


if __name__ == "__main__":
    main()