import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac_Toe")
        self.root.iconbitmap('crown_icon.ico')
        self.root.geometry("400x500")

        self.board_size = 3 
        self.board = [None] * (self.board_size * self.board_size)
        self.current_player = "X"

        self.score_X = 0
        self.score_O = 0

        self.title_label = tk.Label(root, text = "Tic-Tac-Toe", font=("Arial",20))
        self.title_label.pack(pady = 10)

        self.score_label = tk.Label(root, text= f"Player X: {self.score_X} | Player O: {self.score_O}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack()

        self.create_grid()

        self.reset_button = tk.Button(root, text="Reset Game", font=("Arial",14), command=self.reset_game)
        self.reset_button.pack(pady=20)

    def create_grid(self):
        self.buttons = []
        for i in range(self.board_size * self.board_size):
            button = tk.Button(self.grid_frame, text="", width=10, height=4, font=("Arial", 16), command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//self.board_size, column=i%self.board_size)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.buttons[index]["text"] == "" and not self.check_winner():
            self.buttons[index]["text"] = self.current_player
            self.board[index] = self.current_player

            #checking winner
            if self.check_winner():
                messagebox.showinfo("Game Over", f"player {self.current_player} wins!!")
                self.update_score(self.current_player)
                self.disable_buttons()
            elif None not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_score(self, player):
        if player == "X":
            self.score_X += 1
        else:
            self.score_O += 1
        self.score_label.config(text= f"Player X: {self.score_X} | Player O: {self.score_O}")
    
    def check_winner(self):
        winning_combination = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6] 
        ]
        for combo in winning_combination:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] is not None:
                return True
        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state = "disabled")

    def reset_game(self):
        self.board = [None] * (self.board_size * self.board_size)
        self.current_player = "X"

        for button in self.buttons:
            button.config(text="", state = "normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()