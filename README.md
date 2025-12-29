# Práctica: Agentes Inteligentes - Piedra, Papel, Tijeras (RPS)

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/status-development-orange?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

Se propone programar un agente inteligente como solución al entorno de tareas del juego **Piedra, Papel, Tijeras**, siguiendo las directrices de modelado propuestas en el capítulo 2 _Intelligent Agents_ del libro _IA: A modern approach, Russell & Norvig_.

## 📑 Índice

1. [Especificación del entorno de tareas](#1-especificación-del-entorno-de-tareas)
2. [Identificación del tipo de agente y estructura](#2-identificación-del-tipo-de-agente-y-estructura)
3. [Implementación en Python](#3-implementación-en-python)
4. [Extensión a RPS + Lagarto Spock (PENDIENTE)](#4-extensión-a-rps--lagarto-spock)


---

## 1. Especificación del entorno de tareas

Siguiendo el epígrafe _"2.3.2 Properties of task environments"_ de Russell & Norvig, se especifican las características del entorno del RPS.

### Tabla de características

| Entorno de tareas | Observable | Agentes | Determinista | Episódico | Estático | Discreto | Conocido |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **RPS** | PARTIALLY | MULTI & COMPETITIVE | STOCHASTIC | SEQUENTIAL | STATIC | DISCRETE | KNOW |


### Justificación

> **Nota:** A continuación se justifica cada una de las propiedades seleccionadas en la tabla:

* **Observable Parcialmente :**  no vemos la mano del oponente hasta que saca
* **Multi Agente:** hay dos jugadores compitiendo
* **Estocástico:** , ya que el ganar de una probabilidad de resultado 
* **Secuencial:** El agente consulta el historial (memoria) de las jugadas anteriores para decidir, por lo que los episodios están conectados.
* **Estático:** no cambia el entorno
* **Discreto:** es una iteracción fija, solo sacas piedra, papel, tijera 
* **Conocido:** conoce las reglas del juego


---

## 2. Identificación del tipo de agente y estructura

Se ha seleccionado un **Agente Reactivo Basado en Modelos**.

### Modelo del Agente

![Diagrama del Agente - RPS](./img/image_agent.png)

### Componentes y Justificación

El agente necesita mantener un registro del pasado para predecir el futuro. Sus componentes son:

1.  **Sensores:** Reciben la jugada del oponente del turno anterior (input del usuario).
2.  **Estado Interno (Memoria):** Una estructura de datos (lista o diccionario) que almacena el historial de todas las jugadas del oponente hasta el momento. Sin esto, el agente sería ciego a los patrones de comportamiento.
3.  **Reglas de condición-acción (Estrategia):** Basado en el historial, el oponente saca 'Piedra' el 60% de las veces".
    * *Regla de Decisión:* "Si lo más probable es 'Piedra', mi acción es 'Papel'".
4.  **Actuadores:** La función que devuelve la jugada elegida (`return "Paper"`) y la muestra en la consola.



## 3. Implementación en Python

La implementación se ha realizado en Python siguiendo los principios **SOLID**, haciendo especial énfasis en:
* **SRP (Single Responsibility Principle):** Modularización del código para que cada función tenga una única responsabilidad.
* **OCP (Open/Closed Principle):** Diseño preparado para añadir nuevas armas (como Lagarto y Spock) sin modificar el código fuente original. 

### Estrategia del Agente

La lógica principal reside en `get_computer_action()`. Para maximizar el rendimiento, se ha implementado una estrategia de **Análisis de Frecuencia Histórica**:

> El agente utiliza un diccionario para contar cuántas veces ha sacado el usuario Piedra, Papel o Tijeras. Calcula cuál es la jugada más frecuente del rival (Moda) y selecciona automáticamente la acción que vence a esa tendencia. Si no hay datos suficientes, actúa aleatoriamente.

### Ejemplo de Código

El núcleo de la decisión implementa esta lógica de conteo y contraataque:

```python
def get_computer_action(user_history):
    """
    Determina la acción basándose en el historial del oponente.
    Estrategia: Counter-Move sobre la jugada más frecuente (Moda).
    """
    import random
    
    game_rules = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }
    
    # 1. Si no hay datos, jugar aleatorio
    if not user_history:
        return random.choice(list(game_rules.keys()))
    
    # 2. Calcular la jugada más frecuente del usuario (Modelo)
    most_frequent_move = max(set(user_history), key=user_history.count)
    
    # 3. Elegir la acción que gana a esa jugada (Regla de decisión)
    prediction = game_rules[most_frequent_move]
    
    return prediction

