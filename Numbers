import copy
class Numbers:
    def __init__(self, board, screen):
        self.screen = screen
        self.original = copy.deepcopy(board)
        self.player = [[0]*9 for _ in range(9)]
        self.selected = None

    def select(self, row, col):
        self.selected = (row, col)

    def sketch(self, num):
        if self.selected:
            row, col = self.selected
            if self.original[row][col] == 0:
                self.player[row][col] = num
                self.update_screen()

    def clear_cell(self):
        if self.selected:
            row, col = self.selected
            if self.original[row][col] == 0:
                self.player[row][col] = 0
                self.update_screen()

    def place_number(self):
        self.update_screen()

    def reset(self):
        self.player = [[0]*9 for _ in range(9)]
        self.update_screen()

    def full_board(self):
        for r in range(9):
            for c in range(9):
                if self.original[r][c] == 0 and self.player[r][c] == 0:
                    return False
        return True

    def combine(self):
        combined = [[0]*9 for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if self.original[r][c] != 0:
                    combined[r][c] = self.original[r][c]
                else:
                    combined[r][c] = self.player[r][c]
        return combined

    def check_board(self):
        board = self.combine()
        for row in board:
            if set(row) != set(range(1, 10)):
                return False

        for col in range(9):
            col_vals = [board[row][col] for row in range(9)]
            if set(col_vals) != set(range(1, 10)):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                vals = []
                for r in range(box_row, box_row+3):
                    for c in range(box_col, box_col+3):
                        vals.append(board[r][c])
                if set(vals) != set(range(1, 10)):
                    return False

        return True

    def update_screen(self):
        self.screen.displayNums(self.original, self.player)
