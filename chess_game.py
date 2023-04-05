import chess
import chess.engine


PIECES_SCORE = {'p': 10, 'n': 30, 'b': 30, 'r': 50, 'q': 90, 'k': 900}

PIECES_MAP = {
    "p": [
        0,  0,  0,  0,  0,  0,  0,  0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
        5,  5, 10, 25, 25, 10,  5,  5,
        0,  0,  0, 20, 20,  0,  0,  0,
        5, -5, -10,  0,  0, -10, -5,  5,
        5, 10, 10, -20, -20, 10, 10,  5,
        0,  0,  0,  0,  0,  0,  0,  0
    ],

    "n": [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20,  0,  0,  0,  0, -20, -40,
        -30,  0, 10, 15, 15, 10,  0, -30,
        -30,  5, 15, 20, 20, 15,  5, -30,
        -30,  0, 15, 20, 20, 15,  0, -30,
        -30,  5, 10, 15, 15, 10,  5, -30,
        -40, -20,  0,  5,  5,  0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50,
    ],

    "b": [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10,  0,  0,  0,  0,  0,  0, -10,
        -10,  0,  5, 10, 10,  5,  0, -10,
        -10,  5,  5, 10, 10,  5,  5, -10,
        -10,  0, 10, 10, 10, 10,  0, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10,  5,  0,  0,  0,  0,  5, -10,
        -20, -10, -10, -10, -10, -10, -10, -20,
    ],

    "r": [
        0,  0,  0,  0,  0,  0,  0,  0,
        5, 10, 10, 10, 10, 10, 10,  5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        0,  0,  0,  5,  5,  0,  0,  0
    ],

    "q": [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10,  0,  0,  0,  0,  0,  0, -10,
        -10,  0,  5,  5,  5,  5,  0, -10,
        -5,  0,  5,  5,  5,  5,  0, -5,
        0,  0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0, -10,
        -10,  0,  5,  0,  0,  0,  0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20
    ],

    "k": [
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -10, -20, -20, -20, -20, -20, -20, -10,
        20, 20,  0,  0,  0,  0, 20, 20,
        20, 30, 10,  0,  0, 10, 30, 20
    ],

    "k_end": [
        -50, -40, -30, -20, -20, -30, -40, -50,
        -30, -20, -10,  0,  0, -10, -20, -30,
        -30, -10, 20, 30, 30, 20, -10, -30,
        -30, -10, 30, 40, 40, 30, -10, -30,
        -30, -10, 30, 40, 40, 30, -10, -30,
        -30, -10, 20, 30, 30, 20, -10, -30,
        -30, -30,  0,  0,  0,  0, -30, -30,
        -50, -30, -30, -30, -30, -30, -30, -50
    ]
}


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
        pieces_count = 0
        for piece_type, symbol in zip(chess.PIECE_TYPES, chess.PIECE_SYMBOLS[1:]):
            squares = self.board.pieces(piece_type, color)
            pieces_count += len(squares)
            score += len(squares)*PIECES_SCORE[symbol]
            for square in squares:
                if symbol == 'k' and pieces_count <= 6:
                    score += PIECES_MAP["k_end"][square]
                    continue
                score += PIECES_MAP[symbol][square]

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
