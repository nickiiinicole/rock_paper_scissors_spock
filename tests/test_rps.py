import pytest
from src.rps.rps_solid import assess_game, GameAction, GameResult, IntelligentAgent

# --- TESTS DE LÓGICA DEL JUEGO ---
@pytest.mark.draw
def test_draw():
    """Comprueba que si ambos sacan lo mismo, es empate"""
    actions = [GameAction.Rock, GameAction.Paper, GameAction.Scissors, GameAction.Lizard, GameAction.Spock]
    for action in actions:
        assert GameResult.Tie == assess_game(user_action=action, computer_action=action)

@pytest.mark.rock
def test_rock_mechanics():
    """Rock: Gana a Scissors y Lizard. Pierde contra Paper y Spock."""
    assert GameResult.Victory == assess_game(GameAction.Rock, GameAction.Scissors)
    assert GameResult.Victory == assess_game(GameAction.Rock, GameAction.Lizard)
    assert GameResult.Defeat == assess_game(GameAction.Rock, GameAction.Paper)
    assert GameResult.Defeat == assess_game(GameAction.Rock, GameAction.Spock)

@pytest.mark.paper
def test_paper_mechanics():
    """Paper: Gana a Rock y Spock. Pierde contra Scissors y Lizard."""
    assert GameResult.Victory == assess_game(GameAction.Paper, GameAction.Rock)
    assert GameResult.Victory == assess_game(GameAction.Paper, GameAction.Spock)
    assert GameResult.Defeat == assess_game(GameAction.Paper, GameAction.Scissors)
    assert GameResult.Defeat == assess_game(GameAction.Paper, GameAction.Lizard)

@pytest.mark.scissors
def test_scissors_mechanics():
    """Scissors: Gana a Paper y Lizard. Pierde contra Rock y Spock."""
    assert GameResult.Victory == assess_game(GameAction.Scissors, GameAction.Paper)
    assert GameResult.Victory == assess_game(GameAction.Scissors, GameAction.Lizard)
    assert GameResult.Defeat == assess_game(GameAction.Scissors, GameAction.Rock)
    assert GameResult.Defeat == assess_game(GameAction.Scissors, GameAction.Spock)

@pytest.mark.lizard
def test_lizard_mechanics():
    """Lizard: Gana a Spock y Paper. Pierde contra Rock y Scissors."""
    assert GameResult.Victory == assess_game(GameAction.Lizard, GameAction.Spock)
    assert GameResult.Victory == assess_game(GameAction.Lizard, GameAction.Paper)
    assert GameResult.Defeat == assess_game(GameAction.Lizard, GameAction.Rock)
    assert GameResult.Defeat == assess_game(GameAction.Lizard, GameAction.Scissors)

@pytest.mark.spock
def test_spock_mechanics():
    """Spock: Gana a Scissors y Rock. Pierde contra Paper y Lizard."""
    assert GameResult.Victory == assess_game(GameAction.Spock, GameAction.Scissors)
    assert GameResult.Victory == assess_game(GameAction.Spock, GameAction.Rock)
    assert GameResult.Defeat == assess_game(GameAction.Spock, GameAction.Paper)
    assert GameResult.Defeat == assess_game(GameAction.Spock, GameAction.Lizard)

# --- TEST DEL AGENTE INTELIGENTE ---

def test_intelligent_agent_learning():
    """
    Verifica que el agente aprende del historial.
    Si el usuario saca siempre 'Rock', el agente debería aprenderlo
    y sacar algo que venza a 'Rock' (Paper o Spock).
    """
    # Creo el agentee 
    agent = IntelligentAgent()
    
    # Entrenar al agente (Simulamos que el usuario saca Piedra 5 veces por ej)
    for _ in range(5):
        agent.record_move(GameAction.Rock)
        
    #Pedir predicción
    prediction = agent.get_move()
    
    # Verificar: El agente DEBE sacar Papel o Spock para ganar a la Piedra
    winning_moves_against_rock = [GameAction.Paper, GameAction.Spock]
    assert prediction in winning_moves_against_rock, \
        f"El agente debería haber sacado Paper o Spock, pero sacó {prediction.name}"