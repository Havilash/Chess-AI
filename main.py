from chess_game import ChessGame


def main():
    chess = ChessGame()
    chess.move("a2a4")

    chess.move("h7h6")
    chess.move("a4a5")

    chess.move("b7b5")
    chess.move("a5b6")

    chess.move("h6h5")
    chess.move("b6c7")

    chess.move("h5h4")
    chess.move("c7b8")

    chess.print_board()


if __name__ == "__main__":
    main()
