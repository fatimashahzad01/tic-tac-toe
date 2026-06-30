import socket
import threading

def isWinner(board, symbol):
    """Checks if a player has won the game."""
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == symbol:
            return True
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

def create_grid():
    """Creates an empty Tic-Tac-Toe board."""
    return [[" " for _ in range(3)] for _ in range(3)]

def broadcast(message, players):
    """Send a message to both players."""
    for player in players:
        try:
            player.send(message.encode())
        except:
            pass  

def handle_client(conn, player, board, lock, players, turn_tracker):
    symbol = 'X' if player == 0 else 'O'
    conn.send(symbol.encode())

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            row, col = map(int, data.split(','))

            with lock:
                if turn_tracker[0] != player:
                    conn.send("Not your turn".encode())
                    continue

                if board[row][col] == " ":
                    board[row][col] = symbol

                    # Send updated board to all players BEFORE checking for a win
                    board_state = ";".join([",".join(row) for row in board])
                    broadcast(f"BOARD:{board_state}", players)  

                    # Now check for win/draw AFTER sending the update
                    if isWinner(board, symbol):
                        broadcast(f"Player {symbol} wins!", players)
                        return
                    elif all(cell != " " for row in board for cell in row):
                        broadcast("Draw!", players)
                        return

                    turn_tracker[0] = 1 - player  # Switch turn

                else:
                    conn.send("Invalid move".encode())
        except:
            break
    conn.close()
    
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(2)
    print("Waiting for players...")

    board = create_grid()
    lock = threading.Lock()
    players = []
    turn_tracker = [0]  

    while len(players) < 2:
        conn, addr = server.accept()
        players.append(conn)
        print(f"Player {len(players)} connected from {addr}")
        threading.Thread(target=handle_client, args=(conn, len(players) - 1, board, lock, players, turn_tracker)).start()

    broadcast("Game starts", players)

if __name__ == "__main__":
    main()
