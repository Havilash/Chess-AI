
import chess_game
from chess_game import ChessGame
import chess as chess_lib


def sorted_moves(chess: ChessGame):
    def sort_func(x):
        score_guess = 0
        start_piece = chess.board.piece_at(
            chess_lib.parse_square(str(x)[:2]))
        capture_piece = chess.board.piece_at(
            chess_lib.parse_square(str(x)[2:4]))

        if capture_piece is not None:
            score_guess = chess_game.PIECES_SCORE[capture_piece.symbol().lower()] - \
                chess_game.PIECES_SCORE[start_piece.symbol().lower()]/10

        return score_guess

    return sorted(list(chess.board.legal_moves), key=sort_func, reverse=True)


def minimax(chess: ChessGame, depth, alpha, beta, is_maximizing):
    if depth <= 0 or chess.board.is_game_over():
        return chess.eval_score_diff(chess.BLACK)

    moves = sorted_moves(chess)
    moves = chess.board.legal_moves

    if is_maximizing:
        best_score = float("-inf")
        for move in moves:
            chess.board.push(move)
            score = minimax(chess, depth-1, alpha, beta, False)
            chess.board.pop()
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float("inf")
        for move in moves:
            chess.board.push(move)
            score = minimax(chess, depth-1, alpha, beta, True)
            chess.board.pop()
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def white_turn(chess: ChessGame):
    move = input("Move (WHITE): ")
    while not chess.is_legal(move):
        move = input("Try another move (WHITE): ")

    chess.move(move)


def black_turn(chess: ChessGame):  # bot
    best_score = float("-inf")
    best_move = None
    for move in chess.board.legal_moves:
        chess.board.push(move)
        score = minimax(chess, 4, float("-inf"), float("inf"), False)
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
