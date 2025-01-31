class Board:
    def __init__(self):
        self.size = 8
        self.board = self.initialize_board()

    def initialize_board(self):
        board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        mid = self.size // 2
        board[mid - 1][mid - 1] = 'B'
        board[mid][mid] = 'B'
        board[mid - 1][mid] = 'W'
        board[mid][mid - 1] = 'W'
        return board

    def display(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * (self.size * 4 - 1))

    def place_piece(self, row, col, color):
        if self.is_valid_move(row, col, color):
            self.board[row][col] = color
            self.flip_pieces(row, col, color)

    def is_valid_move(self, row, col, color):
        # ここに有効な手の判定ロジックを実装
        pass

    def flip_pieces(self, row, col, color):
        # ここに石をひっくり返すロジックを実装
        pass

    def check_winner(self):
        # 勝者判定のロジックを実装
        pass