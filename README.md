# Asteroids Game

A classic Asteroids game built using Python and Pygame. This project showcases core game mechanics like movement, collision detection, shooting, and object splitting, all while using the `pygame` library for game graphics and interaction.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Gameplay](#gameplay)
4. [Features](#features)
5. [Technologies](#technologies)
6. [Video Demo](#video-demo)

---

## Installation

To get started with the Asteroids game on your local machine, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/G1DO/Asteroids.git
````

2. **Navigate to the project directory:**

   ```bash
   cd Asteroids
   ```

3. **Set up a virtual environment:**

   For Python 3.10 or later:

   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**

   For Linux/macOS:

   ```bash
   source venv/bin/activate
   ```

   For Windows:

   ```bash
   .\venv\Scripts\activate
   ```

5. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Running the Game:**

   Run the game using the following command:

   ```bash
   python main.py
   ```

---

## Gameplay

In this game, you control a spaceship that can rotate and move in space. Your mission is to avoid and shoot at incoming asteroids. The gameplay includes the following features:

* **Movement**: Use the **W, A, S, D** keys to move and rotate your spaceship.
* **Shooting**: Press **Spacebar** to shoot bullets in the direction your spaceship is facing.
* **Asteroids**: Asteroids spawn randomly and move in various directions. They can be destroyed by shooting them.
* **Game Over**: The game ends when your spaceship collides with an asteroid.

---

## Features

* **Player Movement**: Use keyboard input to rotate and move your spaceship.
* **Shooting**: Fire bullets to destroy asteroids.
* **Asteroids**: Randomly spawn and move in different directions. Larger asteroids split into smaller ones when destroyed.
* **Collision Detection**: Detects collisions between the player’s spaceship and asteroids, triggering a "Game Over" message.

---

## Technologies

* **Python**: The main programming language used.
* **Pygame**: A Python library used for game development, providing graphics, event handling, and other game mechanics.
* **Pygbag**: For building the game into a web version (HTML, JS).

---

## Video Demo

Watch the demo of the game here:

[![Watch the video](https://img.youtube.com/vi/YFVrMwVJ5cQ/maxresdefault.jpg)](https://youtu.be/YFVrMwVJ5cQ)


