from tkinter.messagebox import RETRY
import chess


class ChessGame():
    def __init__(self) -> None:
        self.board = chess.Board()
        # self.board = chess.Board("3k4/8/8/8/8/8/8/3K4 b KQkq - 0 4")

    def is_draw(self):
        outcome = self.board.outcome()
        if hasattr(outcome, "winner"):
            if outcome.winner == None:
                return True
        return False

    def is_checkmate(self):
        return self.board.is_checkmate()

    def is_legal(self, uci):
        return uci in self.board.legal_moves

    def move(self, uci):
        m = chess.Move.from_uci(uci)
        self.board.push(m)

    def revert_last_move(self):
        self.board.pop()

    def print_board(self):
        print(self.board)
