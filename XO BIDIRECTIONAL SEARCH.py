import random
import tkinter as tk

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.buttons = []
        self.player = "X"
        self.computer = "O"
        self.turn_label = None
        self.restart_button = None
        self.is_player_turn = True
        self.priority_queue = []

        self.create_game_board()
        self.create_turn_label()
        self.create_restart_button()

        self.is_player_turn = random.choice([True, False])
        if not self.is_player_turn:
            self.make_ai_move()

    def create_game_board(self):
        # Create the game board buttons
        for row in range(3):
            button_row = []
            for column in range(3):
                button = tk.Button(self.window, text="", width=10, height=5,
                                   command=lambda r=row, c=column: self.make_move(r, c))
                button.grid(row=row, column=column)
                button_row.append(button)
            self.buttons.append(button_row)

    def create_turn_label(self):
        # Create the turn label
        self.turn_label = tk.Label(self.window, text="X turn", font=("Arial", 16))
        self.turn_label.grid(row=3, columnspan=3)

    def create_restart_button(self):
        # Create the restart button
        self.restart_button = tk.Button(self.window, text="Restart", width=10, height=2, command=self.restart_game)
        self.restart_button.grid(row=4, columnspan=3)

    def make_move(self, row, column):
        if self.is_player_turn and self.buttons[row][column]["text"] == "":
            self.buttons[row][column]["text"] = self.player
            self.buttons[row][column]["state"] = "disabled"
            self.check_game_status()
            self.is_player_turn = False
            if not self.check_game_over() and not self.is_player_turn:
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


    def bidirectional_computer_move(self):
     empty_spaces = []
     for i in range(3):
        for j in range(3):
            if self.buttons[i][j]["text"] == "":
                empty_spaces.append((i, j))

     if len(empty_spaces) > 0:
        random_move = random.choice(empty_spaces)
        self.buttons[random_move[0]][random_move[1]]["text"] = self.computer

    def update_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]["text"] = self.buttons[row][column]["text"]

    def check_game_status(self):
        winner = self.check_winner(self.buttons)
        if winner:
            self.turn_label.config(text=winner + " wins!")
            self.disable_buttons()
        elif self.check_tie(self.buttons):
            self.turn_label.config(text="It's a tie!")
            self.disable_buttons()

    def check_winner(self, state):
        for row in range(3):
            if state[row][0]["text"] == state[row][1]["text"] == state[row][2]["text"] != "":
                return state[row][0]["text"]
        for column in range(3):
            if state[0][column]["text"] == state[1][column]["text"] == state[2][column]["text"] != "":
                return state[0][column]["text"]
        if state[0][0]["text"] == state[1][1]["text"] == state[2][2]["text"] != "":
            return state[0][0]["text"]
        if state[0][2]["text"] == state[1][1]["text"] == state[2][0]["text"] != "":
            return state[0][2]["text"]
        return ""

    def check_tie(self, state):
        for row in range(3):
            for column in range(3):
                if state[row][column]["text"] == "":
                    return False
        return True

    def disable_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]["state"] = "disabled"

    def check_game_over(self):
        winner = self.check_winner(self.buttons)
        if winner:
            self.turn_label.config(text=winner + " wins!")
            self.disable_buttons()
            return True
        elif self.check_tie(self.buttons):
            self.turn_label.config(text="It's a tie!")
            self.disable_buttons()
            return True
        return False

    def restart_game(self):
        self.is_player_turn = True
        self.turn_label.config(text="X turn")
        self.enable_buttons()
        self.clear_buttons()

    def enable_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]["state"] = "normal"

    def clear_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]["text"] = ""

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Tic-Tac-Toe Game")

    game = TicTacToe(window)

    window.mainloop()
