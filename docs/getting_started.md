# Getting Started with ARIA RPG Engine

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/aria-rpg-engine.git
cd aria-rpg-engine
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## Running Your First Game

Create a simple game script:

```python
from aria.core.game_loop import GameLoop
from aria.core.world import World

# Initialize the game world
world = World()

# Create the game loop
game = GameLoop(world)

# Run the game
game.start()
```

## Basic Concepts

### Entities

Everything in the game world is an Entity:
- Players
- NPCs
- Monsters
- Items

### The World

The World manages:
- All entities
- Game state
- Environmental conditions

### The Game Loop

The Game Loop:
- Processes user input
- Updates game state
- Manages AI decisions
- Handles persistence

## Next Steps

- Read the [Architecture Documentation](architecture.md)
- Explore the [Data Integration Guide](data_integration_guide.md)
- Check out example games in the `examples/` directory
