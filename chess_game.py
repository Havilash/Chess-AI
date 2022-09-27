import chess


class ChessGame():
    def __init__(self) -> None:
        self.board = chess.Board()

    def move(self, uci):
        m = chess.Move.from_uci(uci)
        if m in self.board.legal_moves:
            self.board.push(m)

    def print_board(self):
        print(self.board)
