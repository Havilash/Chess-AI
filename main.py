
from chess_game import ChessGame
import chess as chess_lib

POINTS = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 15}


def white_turn(chess):
    move = input("Move (WHITE): ")
    while not chess.is_legal(move):
        move = input("Try another move (WHITE): ")

    chess.move(move)


def minimax(chess: ChessGame, depth, is_maximizing):
    if depth <= 0:
        return 0 + caputre_score

    if chess.is_checkmate():
        if is_maximizing:
            return 50 + caputre_score
        else:
            return -50 + caputre_score
    if chess.is_draw():
        return 0 + caputre_score

    if is_maximizing:
        best_score = float("-inf")
        for move in chess.board.legal_moves:
            # capture = str(chess.board.piece_at(
            #     chess_lib.parse_square(str(move)[-2:])))

            # caputre_score += POINTS[capture.lower()
            #                         ] if capture.lower() in POINTS.keys() else 0

            chess.board.push(move)
            score = minimax(chess, depth-1, False)
            chess.board.pop()
            if (score > best_score):
                best_score = score
        return best_score
    else:
        best_score = float("inf")
        for move in chess.board.legal_moves:
            # capture = str(chess.board.piece_at(
            #     chess_lib.parse_square(str(move)[-2:])))

            # caputre_score -= POINTS[capture.lower()
            #                         ] if capture.lower() in POINTS.keys() else 0

            chess.board.push(move)
            score = minimax(chess, depth-1, True)
            chess.board.pop()
            if (score < best_score):
                best_score = score
        return best_score


def black_turn(chess: ChessGame):  # bot
    best_score = float("-inf")
    best_move = None
    for move in chess.board.legal_moves:
        chess.board.push(move)
        score = minimax(chess, 3, False)
        chess.board.pop()
        if (score > best_score):
            best_score = score
            best_move = move

    chess.board.push(best_move)


def main():
    chess = ChessGame()

    is_running = True
    while is_running:
        print()
        chess.print_board()
        print()

        if chess.turn == chess.WHITE:
            white_turn(chess)
        else:
            black_turn(chess)


if __name__ == "__main__":
    main()
