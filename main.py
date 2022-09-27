from xml.dom.minidom import Element
from chess_game import ChessGame


def white_turn(chess):
    move = input("Move (WHITE): ")
    while not chess.is_legal(move):
        move = input("Try another move (WHITE): ")

    chess.move(move)


def black_turn(chess):  # bot
    move = input("Move (BLACK): ")
    while not chess.is_legal(move):
        move = input("Try another move (BLACK): ")

    chess.move(move)


def main():
    chess = ChessGame()

    is_running = True
    while is_running:
        chess.print_board()

        if chess.turn == chess.WHITE:
            white_turn(chess)
        else:
            black_turn(chess)


if __name__ == "__main__":
    main()
