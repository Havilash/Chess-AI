from chess_game import ChessGame


def main():
    chess = ChessGame()

    is_running = True
    while is_running:
        chess.print_board()
        move = input("Move: ")
        while not chess.is_legal(move):
            move = input("Try another move: ")


if __name__ == "__main__":
    main()
