# The-Forge

The-Forge is a top-down action game built with Pygame. It features a stack-based state management system, a custom camera with Y-sorting for depth, and smooth player mechanics including movement, dashing, and attacks.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

Follow these steps to set up the project locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/The-Forge.git
    cd The-Forge
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Play

Run the game using the following command:
```bash
python main.py
```

### Controls

- **WASD:** Move the player.
- **SPACE / L-SHIFT:** Dash in the current movement direction (consumes stamina).
- **LEFT CLICK:** Perform an attack in the direction the player is facing.
- **ENTER:** Start the game from the main menu.
- **ESC:** Return to the main menu from the game.
- **CLOSE WINDOW:** Exit the application.

## Project Structure

- `main.py`: Entry point of the game.
- `entities/`: Contains game entities like the Player, Obstacles, and Camera management.
- `states/`: Contains the State Manager and various game states (Menu, Gameplay).
- `requirements.txt`: List of required Python packages.
