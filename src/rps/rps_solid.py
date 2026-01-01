import random
from enum import IntEnum
from collections import Counter



class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3  
    Spock = 4 


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2

Victories = {
    GameAction.Rock: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Paper: [GameAction.Rock, GameAction.Spock],
    GameAction.Scissors: [GameAction.Paper, GameAction.Lizard],
    GameAction.Lizard: [GameAction.Spock, GameAction.Paper],
    GameAction.Spock: [GameAction.Scissors, GameAction.Rock]
}

class IntelligentAgent:
    def __init__(self):
        self.history = []

    def record_move(self, move):
        self.history.append(move)

    def get_move(self):
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
        
        return GameAction(random.randint(0, len(GameAction) - 1))

my_agent = IntelligentAgent()

def assess_game(user_action, computer_action):
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
    computer_action = my_agent.get_move()
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
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