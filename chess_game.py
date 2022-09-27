from tkinter.messagebox import RETRY
import chess


class ChessGame():
    WHITE = True
    BLACK = False

    def __init__(self) -> None:
        self.board = chess.Board()
        # self.board = chess.Board("3k4/8/8/8/8/8/8/3K4 b KQkq - 0 4")

    @property
    def turn(self):
        return self.board.turn

    def is_draw(self):
        outcome = self.board.outcome()
        if hasattr(outcome, "winner"):
            if outcome.winner == None:
                return True
        return False

    def is_checkmate(self):
        return self.board.is_checkmate()

    def is_legal(self, uci):
        try:
            m = chess.Move.from_uci(uci)
            return m in self.board.legal_moves
        except ValueError:
            return False

    def move(self, uci):
        m = chess.Move.from_uci(uci)
        self.board.push(m)

    def revert_last_move(self):
        self.board.pop()

    def print_board(self):
        print(self.board)
