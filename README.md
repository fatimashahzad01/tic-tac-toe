# Multiplayer Tic-Tac-Toe

## Description

This project is a multiplayer Tic-Tac-Toe game developed in Python using socket programming, multithreading, and Tkinter. The application allows two players to connect over a local network, play against each other in real time, and automatically synchronize game moves through a central server.

The server manages player connections, validates moves, controls player turns, updates the game board, and determines the winner. The client provides a graphical user interface where players can interact with the game board and view the current game state.

## Features

- Two-player multiplayer gameplay
- Real-time board synchronization
- Turn-based gameplay
- Winner and draw detection
- Graphical user interface using Tkinter
- Score tracking
- Restart functionality
- Threaded server supporting multiple client connections

## Technologies Used

- Python 3
- Socket Programming
- Multithreading
- Tkinter GUI

## Project Structure

```
.
├── server.py
├── client.py
└── README.md
```

## Requirements

- Python 3.10 or later
- Tkinter (included with most Python installations)

## How to Run

### Step 1: Start the Server

Open a terminal in the project directory and run:

```bash
python server.py
```

The server will start and wait for two players.

Example output:

```
Waiting for players...
```

---

### Step 2: Start the First Client

Open another terminal and run:

```bash
python client.py
```

---

### Step 3: Start the Second Client

Open a third terminal and run:

```bash
python client.py
```

Once both clients are connected, the game will begin automatically.

## Gameplay

- Player 1 is assigned the symbol **X**.
- Player 2 is assigned the symbol **O**.
- Players take turns placing their symbols on the board.
- The server validates each move before updating the game state.
- The game ends when:
  - A player completes a row, column, or diagonal.
  - The board is full, resulting in a draw.

## Network Configuration

The server listens on:

```
Host: localhost
Port: 5555
```

To play across different computers on the same network:

1. Replace `localhost` in the client with the server computer's IP address.
2. Ensure both computers are connected to the same network.
3. Allow Python through the firewall if prompted.

## Game Rules

- Only one player can move at a time.
- Invalid moves are rejected.
- Players cannot overwrite existing moves.
- The server maintains the official game state.

## Future Improvements

- Online multiplayer support
- Chat between players
- Player usernames
- Game lobby system
- Match history
- Spectator mode
- Better UI and animations
- Sound effects
- AI opponent
- Cross-platform packaging

## Authors

Developed as a Computer Science project using Python, Socket Programming, Multithreading, and Tkinter.
