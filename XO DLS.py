#depth limited search
import random
import tkinter as tk

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic-Tac-Toe Game")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player = "X"
        self.computer = "O"
        self.is_player_turn = True
        self.turn_label = tk.Label(self.window, text="X turn")
        self.turn_label.grid(row=3, column=0, columnspan=3)
        self.create_buttons()
        self.clear_buttons()
        self.is_player_turn = random.choice([True, False])
        if not self.is_player_turn:
            self.make_ai_move()

    def create_buttons(self):
        for row in range(3):
            for column in range(3):
                button = tk.Button(self.window, text="", width=10, height=5,
                                   command=lambda r=row, c=column: self.make_move(r, c))
                button.grid(row=row, column=column)
                self.buttons[row][column] = button

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
            depth_limit = 3  # Set the depth limit for the DLS algorithm
            result = self.dls_computer_move(depth_limit)
            if result is not None:
                row, column = result
                self.buttons[row][column]["text"] = self.computer
                self.buttons[row][column]["state"] = "disabled"
                self.check_game_status()
                self.is_player_turn = True

    def dls_computer_move(self, depth_limit):
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]["text"] == "":
                    self.buttons[row][column]["text"] = self.computer
                    self.buttons[row][column]["state"] = "disabled"
                    if self.check_winner() == self.computer:
                        self.buttons[row][column]["text"] = ""
                        self.buttons[row][column]["state"] = "normal"
                        return row, column
                    if depth_limit > 0:
                        result = self.dls_computer_move(depth_limit - 1)
                        if result is not None:
                            self.buttons[row][column]["text"] = ""
                            self.buttons[row][column]["state"] = "normal"
                            return result
                    self.buttons[row][column]["text"] = ""
                    self.buttons[row][column]["state"] = "normal"
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
            if (self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"]
                    != ""):
                return self.buttons[row][0]["text"]
        for column in range(3):
            if (self.buttons[0][column]["text"] == self.buttons[1][column]["text"] == self.buttons[2][column]["text"]
                    != ""):
                return self.buttons[0][column]["text"]
        if (self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"]
                != ""):
            return self.buttons[0][0]["text"]
        if (self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"]
                != ""):
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
