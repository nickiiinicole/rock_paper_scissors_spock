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
5. [Bibliografía](#bibliografía)

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
* **Episódico:** solo importa maximizar la recompensa inmediata, no afecta a futuro
* **Estático:** no cambia el entorno
* **Discreto:** es una iteracción fija, solo sacas piedra, papel, tijera 
* **Conocido:** conoce las reglas del juego


---

## 2. Identificación del tipo de agente y estructura

Para resolver este problema, se ha seleccionado un **[INDICAR TIPO DE AGENTE: Ej. Agente Reactivo Basado en Modelos]**.

### Modelo del Agente

A continuación se muestra el diagrama del modelo elegido, adaptado específicamente al contexto del juego RPS:

![Modelo Agente](./doc/modelo_AI.png)
*(Recuerda sustituir esta imagen por tu propio diagrama donde se vean los componentes específicos de tu agente).*

### Componentes y Justificación

El agente se estructura con los siguientes componentes mostrados en la figura:

1.  **Sensores:** [Descripción de qué percibe el agente...]
2.  **Estado Interno:** [Descripción de qué memoria guarda el agente...]
3.  **Reglas de condición-acción:** [Descripción de la lógica de decisión...]
4.  **Actuadores:** [Descripción de cómo ejecuta la acción el agente...]

---

## 3. Implementación en Python

La implementación se ha realizado en Python siguiendo los principios **SOLID**, haciendo especial énfasis en:
* **SRP (Single Responsibility Principle):** Modularización del código para que cada función tenga una única responsabilidad.
* **OCP (Open/Closed Principle):** Diseño preparado para añadir nuevas armas (como Lagarto y Spock) sin modificar el código fuente original.

### Estrategia del Agente

La lógica principal de decisión reside en la función `get_computer_action()`. La estrategia implementada para maximizar el **rendimiento** consiste en:

> [Describe aquí tu estrategia creativa. Ej: "El agente utiliza una cadena de Markov para predecir el siguiente movimiento del usuario basándose en su historial reciente..."]

### Diagrama de flujo del programa

![Table Driven Agent Program](./doc/table_driven_agent_program.png)

### Ejemplo de Código

El núcleo de la decisión se encuentra en el siguiente bloque:

```python
def get_computer_action(user_action):
    # Ejemplo de lógica simplificada
    if user_action == "Rock":
        return "Paper"
    # ... lógica real ...
    return action