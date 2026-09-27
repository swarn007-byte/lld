from board import board


class tictactoe:
    def __init__(self):
        self.board = board()
        self.current_player = 'X'

    # switch turn between X and O
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    # print the board nicely using board's display_board (flat list)
    def print_board(self):
        cells = self.board.display_board()
        for i in range(3):
            row = cells[i*3:(i+1)*3]
            print(" | ".join(row))
            if i < 2:
                print("-" * 9)

    # main game loop
    def play(self):
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")

            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Please enter numbers only.")
                continue

            if not (0 <= row < 3 and 0 <= col < 3):
                print("Row/col must be between 0 and 2.")
                continue

            moved = self.board.make_a_move(row, col, self.current_player)
            if not moved:
                print("That cell is already taken, try again.")
                continue

            status = self.board.check_status()

            if status == 1:
                self.print_board()
                print("X wins!")
                break
            elif status == 2:
                self.print_board()
                print("O wins!")
                break
            elif status == 3:
                self.print_board()
                print("It's a stalemate!")
                break

            # status == 0 -> game continues
            self.switch_player()


if __name__ == "__main__":
    game = tictactoe()
    game.play()