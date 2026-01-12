# Práctica: Agentes Inteligentes - Piedra, Papel, Tijeras (RPS)

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/status-development-orange?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

Se propone programar un agente inteligente como solución al entorno de tareas del juego **Piedra, Papel, Tijeras**, siguiendo las directrices de modelado propuestas en el capítulo 2 _Intelligent Agents_ del libro _IA: A modern approach, Russell & Norvig_.

## 📑 Índice

1. [Especificación del entorno de tareas](#1-especificación-del-entorno-de-tareas)
2. [Identificación del tipo de agente y estructura](#2-identificación-del-tipo-de-agente-y-estructura)
3. [Implementación en Python](#3-implementación-en-python)
4. [Extensión a RPS + Lagarto Spock](#4-extensión-a-rps--lagarto-spock)


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

La implementación se ha realizado siguiendo los principios **SOLID**: 
* **SRP (Single Responsibility Principle):** Se ha modularizado el código separando responsabilidades:
    * `Victories` (Diccionario): Define las reglas de datos y relaciones de victoria.
    * `IntelligentAgent`: Clase encargada únicamente de gestionar la memoria y decidir el siguiente movimiento.
    * `assess_game`: Función encargada únicamente de gestionar la visualización del resultado (UI), delegando la lógica de decisión.
* **OCP (Open/Closed Principle):** El diseño está "cerrado a modificación" pero "abierto a extensión". Al sustituir las cadenas de `if/elif` por un diccionario de reglas (`Victories`), fue posible añadir nuevas armas sin modificar la lógica interna de las funciones de evaluación.

### Estrategia del Agente (IntelligentAgent)

La lógica de decisión se invoca desde `get_computer_action()`, pero reside en la clase `IntelligentAgent`. Se ha implementado un **Agente Reactivo Basado en Modelos** con una estrategia de **Análisis de Frecuencia Histórica:D**:

> El agente mantiene una memoria interna (`self.history`) de todas las jugadas del usuario. En cada turno, utiliza la herramienta `Counter` para calcular la **moda** (la jugada que más repite el rival) y consulta el diccionario de reglas para seleccionar automáticamente la acción específica que la derrota

### Ejemplo de Código

`IntelligentAgent` implementa la lógica de predicción y contraataque:

```python
class IntelligentAgent:
    def __init__(self):
        self.history = []

    def get_move(self):
        # 1. Si no hay datos (primera ronda), jugar aleatorio
        if not self.history:
             selection = random.randint(0, len(GameAction) - 1)
             return GameAction(selection)
        
        # 2. INTELIGENCIA: Calcular la jugada más frecuente del usuario (Moda)
        # most_common(1) devuelve [(Acción, Cantidad)], usamos [0][0] para sacar la acción.
        most_common = Counter(self.history).most_common(1)[0][0]
        
        # 3. CONTRAATAQUE: Buscar en las reglas qué gana a esa jugada frecuente
        for action, losers in Victories.items():
            if most_common in losers:
                return action
        
        # Fallback de seguridad
        return GameAction(random.randint(0, len(GameAction) - 1))
