import tkinter as tk
import random



class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.buttons = []
        self.player = "X"
        self.computer = "O"
        self.turn_label = None
        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=4, columnspan=3)
        self.is_player_turn = True

        # Create game board buttons
        for row in range(3):
            button_row = []
            for column in range(3):
                button = tk.Button(root, text="", width=10, height=5)
                button.grid(row=row, column=column)
                button.config(command=lambda r=row, c=column: self.make_move(r, c))
                button_row.append(button)
            self.buttons.append(button_row)

        # Create turn label
        self.turn_label = tk.Label(root, text="X turn", font=("Arial", 16))
        self.turn_label.grid(row=3, columnspan=3)

    def restart_game(self):
        # Reset game state
        self.player = "X"
        self.is_player_turn = True
        self.turn_label.config(text="X turn")
        self.enable_buttons()
        self.clear_buttons()
        
        # Randomly choose whether the player or computer goes first
        self.is_player_turn = random.choice([True, False])
        if not self.is_player_turn:
            self.make_ai_move()

    def enable_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]["state"] = "normal"

    def clear_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]["text"] = ""

    def make_move(self, row, column):
        if self.is_player_turn and self.buttons[row][column]["text"] == "":
            self.buttons[row][column]["text"] = self.player
            self.buttons[row][column]["state"] = "disabled"
            self.check_game_status()
            self.is_player_turn = False
            if not self.check_game_over():
                self.make_ai_move()

    def make_ai_move(self):
     if not self.is_player_turn:
        while True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if self.buttons[row][column]["text"] == "":
                self.buttons[row][column]["text"] = self.computer
                self.buttons[row][column]["state"] = "disabled"
                self.check_game_status()
                self.is_player_turn = True
                break
     else:
        result = self.dfs_computer_move()
        if result is not None:
            row, column = result
            self.buttons[row][column]["text"] = self.computer
            self.buttons[row][column]["state"] = "disabled"
            self.check_game_status()
            self.is_player_turn = True

    def dfs_computer_move(self):
     for row in range(3):
        for column in range(3):
            if self.buttons[row][column]["text"] == "":
                self.buttons[row][column]["text"] = self.player
                if self.check_winner() == self.player:
                    self.buttons[row][column]["text"] = ""
                    return row, column
                result = self.dfs_computer_move()
                if result is not None:
                    return result
                self.buttons[row][column]["text"] = ""
     return None

    def check_game_status(self):
        winner = self.check_winner()
        if winner:
            self.turn_label.config(text=winner + " wins!")
            self.disable_buttons()
        elif self.check_tie():
            self.turn_label.config(text="It's a tie!")
            self.disable_buttons()

    def check_winner(self):
        for row in range(3):
            if (
                self.buttons[row][0]["text"]
                == self.buttons[row][1]["text"]
                == self.buttons[row][2]["text"]
                != ""
            ):
                return self.buttons[row][0]["text"]
        for column in range(3):
            if (
                self.buttons[0][column]["text"]
                == self.buttons[1][column]["text"]
                == self.buttons[2][column]["text"]
                != ""
            ):
                return self.buttons[0][column]["text"]
        if (
            self.buttons[0][0]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][2]["text"]
            != ""
        ):
            return self.buttons[0][0]["text"]
        if (
            self.buttons[0][2]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][0]["text"]
            != ""
        ):
            return self.buttons[0][2]["text"]
        return ""

    def check_tie(self):
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]["text"] == "":
                    return False
        return True

    def disable_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]["state"] = "disabled"

    def check_game_over(self):
        winner = self.check_winner()
        if winner:
            self.turn_label.config(text=winner + " wins!")
            self.disable_buttons()
            return True
        elif self.check_tie():
            self.turn_label.config(text="It's a tie!")
            self.disable_buttons()
            return True
        return False


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Tic-Tac-Toe Game")

    game = TicTacToe(window)

    window.mainloop()


