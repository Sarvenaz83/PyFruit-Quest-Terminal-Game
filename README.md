# 🍇 PyFruit Quest - Terminal Adventure Game

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3670A0?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://github.com/your-username/PyFruit-Quest-Terminal-Game/actions/workflows/python.yml/badge.svg)](https://github.com/your-username/PyFruit-Quest-Terminal-Game/actions)
[![Codecov](https://codecov.io/gh/your-username/PyFruit-Quest-Terminal-Game/branch/main/graph/badge.svg)](https://codecov.io/gh/your-username/PyFruit-Quest-Terminal-Game)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> A Python-based terminal game developed as part of the **Testautomatsering Python** course at Stockholm University

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZThiYzY1YjMxYjM5Y2RjOGFmYzJhYTg1M2QxMjUwYjAxY2NlOTUzNiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/3o7btT1T9qpQZWhNl6/giphy.gif" width="600" alt="Game Demo">
</p>

## ✨ Features

### 🎮 Core Gameplay
- **WASD Movement** with collision detection
- **Dynamic Inventory System** (`i` to view)
- **Smart Wall Generation** using loops
- **Score Management** with "The Floor is Lava" (-1/step)

### 🧩 Advanced Mechanics
- **Traps & Spades** 
  - 🕳️ Traps: -10 points per hit
  - ⚒️ Spades: Break walls (one-time use)
- **Key & Chest System**
  - 🔑 Collect keys to open chests (+100 points)
- **Auto-Fruit Generation** (Every 25 moves)

### 🤖 AI Challenges (v3)
- **Smart Enemies** with pathfinding
- **Bomb Mechanics** (`B` to plant)
- **Trap Disarming** (`T` command)
- **Grace Period** (5 safe moves after item pickup)

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/ُSarvenaz83/PyFruit-Quest-Terminal-Game.git
cd PyFruit-Quest-Terminal-Game

# Install dependencies
pip install -r requirements.txt
