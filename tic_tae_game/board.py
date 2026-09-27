from typing import List

# in board class we have features like , to check if board is full , check who win , check status(aboart, who win ,stalemate etc) , display the board , make a move.
# all these features we will implement.



class board:
    def __init__(self):
        self.board = [['_' for _ in range(3)] for _ in range(3)]

    # check if board is full
    def check_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=='_':
                    return False

        
        return True

    def check_win(self, symbol: str) -> bool:
        # return true if 3 consistent block(row , col or diag) has same suymbol
        grid = self.board

        for i in range(3):
            ans = True
            for j in range(3):
                if grid[i][j]!=symbol:
                    ans=False
                    break
            if ans:
                return True


        for i in range(3):
            ans = True
            for j in range(3):
                if grid[j][i]!=symbol:
                    ans=False
                    break
            if ans:
                return True


        ans = True
        for i in range(3):
                if grid[i][i]!=symbol:
                    ans=False
                    break
        if ans:
            return True

        ans = True
        for i in range(3):
                if grid[i][2-i]!=symbol:
                    ans=False
                    break
        if ans:
            return True

        return False

    def check_status(self) -> int:
        if self.check_win('X'):
            return 1
        if self.check_win('O'):
            return 2
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=="_":
                    return 0

        # 0 means match aborted


        return 3 
        #3 means stalemate




    # diplay the board
    def display_board(self):
        box=[]
        for i in range(3):
            for j in range(3):
                box.append(self.board[i][j])


        return box

    # make a move
    def make_a_move(self, row, col, symbol):
        if self.board[row][col] != '_':
            return False
        self.board[row][col] = symbol
        return True