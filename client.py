import tkinter as tk
from tkinter import messagebox, Toplevel

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#1687a7")  # Background color changed to match the provided image
        self.root.geometry("400x500")
        self.root.configure(borderwidth=5, relief="solid")
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0}
        
        self.create_widgets()
    
    def create_widgets(self):
        """Creates the Tic-Tac-Toe board with updated colors and fonts."""
        self.turn_label = tk.Label(self.root, text=f"Player {self.current_player}'s Turn", font=("Comic Sans MS", 16, "bold"), fg="white", bg="#1687a7")
        self.turn_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text=f"X: {self.scores['X']} | O: {self.scores['O']}", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#1687a7")
        self.score_label.pack(pady=5)
        
        board_frame = tk.Frame(self.root, bg="#1687a7")
        board_frame.pack(padx=20, pady=10)
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(board_frame, text="", font=("Comic Sans MS", 48, "bold"), width=3, height=1,
                                               bg="#a9ede6", fg="#364f6b", relief="ridge", borderwidth=5,
                                               command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        # Add a restart button
        self.restart_button = tk.Button(self.root, text="Restart", font=("Comic Sans MS", 14, "bold"), 
                                        bg="#04324b", fg="white", relief="ridge", borderwidth=3, 
                                        command=self.restart_game)
        self.restart_button.pack(pady=10)
    
    def make_move(self, row, col):
        """Handles player moves and updates the board."""
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)

            if self.check_winner(self.current_player):
                self.scores[self.current_player] += 1
                self.show_winner_popup(self.current_player)
                return

            if all(self.board[i][j] != " " for i in range(3) for j in range(3)):
                self.show_winner_popup(None)
                return
            
            self.current_player = "O" if self.current_player == "X" else "X"
            self.turn_label.config(text=f"Player {self.current_player}'s Turn")
    
    def check_winner(self, symbol):
        """Checks if the current player has won."""
        for row in range(3):
            if all(self.board[row][col] == symbol for col in range(3)):
                return True
        for col in range(3):
            if all(self.board[row][col] == symbol for row in range(3)):
                return True
        if all(self.board[i][i] == symbol for i in range(3)) or all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False
    
    def show_winner_popup(self, winner):
        """Displays a custom popup window for the winner."""
        popup = Toplevel(self.root)
        popup.title("Game Over")
        popup.geometry("250x150")
        popup.configure(bg="#1687a7")
        
        message = f"Player {winner} wins!" if winner else "It's a tie!"
        msg_label = tk.Label(popup, text=message, font=("Comic Sans MS", 14, "bold"), fg="white", bg="#1687a7")
        msg_label.pack(pady=20)
        
        close_button = tk.Button(popup, text="OK", font=("Comic Sans MS", 12, "bold"), bg="#04324b", fg="white", command=lambda: [popup.destroy(), self.restart_game()])
        close_button.pack()
    
    def restart_game(self):
        """Resets the board for a new game."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state=tk.NORMAL)
        self.current_player = "X"
        self.turn_label.config(text=f"Player {self.current_player}'s Turn")
        self.score_label.config(text=f"X: {self.scores['X']} | O: {self.scores['O']}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()