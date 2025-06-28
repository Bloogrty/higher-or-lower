# Higher or Lower: Tech Sultan Edition

Welcome to **Higher or Lower: Tech Sultan Edition**, a command-line game where you guess which gadget burns more cash! From Apple Watches to Xiaomi phones, it’s your job to pick the pricier product and flex your tech-finance instincts.

This project is built entirely in Python and includes a local SQLite database to store and display high scores.

## Features

- Fun, tech-themed price comparison game
- Clear, punchy output with a "Sultan" vibe
- Persistent high score leaderboard using SQLite (no server needed)
- Modular code: separate logic for database and game engine
- Automatically shows the Top 5 scorers at the end of each session

## Technologies Used

- Python 3.9+
- SQLite3 (via Python's built-in sqlite3 module)
- No external dependencies

## Project Structure

    higher__or__lower/
    ├── art.py            # ASCII logo and VS art
    ├── game_data.py      # List of product data (name, brand, price, etc.)
    ├── database.py       # Database functions (init, insert, get scores)
    ├── main.py           # Main game logic
    └── README.md         # You're reading it now!

## Database Functions (in `database.py`)

- `init_db()`: Initializes the `scores` table if it doesn't exist
- `insert_score(name, score)`: Inserts a player’s score
- `get_scores()`: Returns a sorted list of all scores (highest first)

These functions use a local `game.db` file — no setup needed, it auto-creates.

## Game Flow

Here's how the game works:

1. `main.py` starts and prints the game logo from `art.py`
2. The game randomly selects two products from `game_data.py`
3. Player guesses which product is more expensive
4. Score increases for correct answers; game ends on first wrong guess
5. At the end:
   - Player enters their name
   - Score is saved in `game.db`
   - Top 10 high scores are displayed using `get_scores()`

## How to Run

Make sure you're in the project directory and run:

    python main.py

Optional: Clear the database manually if needed by deleting `game.db`.

## Future Ideas

- Add product images (if moving to GUI)
- Let players retry without restarting the script
- Use `argparse` for running in different modes (e.g., test mode, reset DB)

Have fun, and may your tech guesses always be on point.
