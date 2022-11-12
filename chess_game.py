import chess
import chess.engine


PIECES_SCORE = {'p': 10, 'n': 30, 'b': 30, 'r': 50, 'q': 90, 'k': 900}


class ChessGame():
    WHITE = True
    BLACK = False

    def __init__(self, **kwargs) -> None:
        self.board = chess.Board(**kwargs)

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

    def print_board(self):
        print(self.board)

    def color_score(self, color: chess.Color):
        score = 0
        for piece, symbol in zip(chess.PIECE_TYPES, chess.PIECE_SYMBOLS[1:]):
            pieces = self.board.pieces(piece, color)
            score += len(pieces)*PIECES_SCORE[symbol]

        outcome = self.board.outcome()
        if hasattr(outcome, "winner"):
            if outcome.winner is None:
                pass
            elif outcome.winner is not color:
                score -= PIECES_SCORE['k']

        return score

    def eval_score_diff(self, color: chess.Color):
        diff = self.color_score(color) - self.color_score(not color)
        return diff
