import chess

PIECES_SCORE = {'p': 10, 'n': 30, 'b': 30, 'r': 50, 'q': 90, 'k': 900}


class ChessGame():
    WHITE = True
    BLACK = False

    def __init__(self) -> None:
        self.board = chess.Board()

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

    def pieces_score(self, color: chess.Color):
        score = 0
        for square in chess.SQUARES:
            if self.board.color_at(square) == color:
                piece = self.board.piece_at(square)
                score += PIECES_SCORE[piece.symbol().lower()]

        return score

    def evaluate_score(self, color: chess.Color):
        score = self.pieces_score(
            color) - self.pieces_score(not color)

        outcome = self.board.outcome()
        if outcome is not None:
            if hasattr(outcome, "winner"):
                if outcome.winner == color:
                    score += 900
                else:
                    score -= 900

        return score
