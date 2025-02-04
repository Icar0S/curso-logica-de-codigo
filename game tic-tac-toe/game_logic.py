# game_logic.py
from screen import BOARD_ROWS, BOARD_COLS
from draw_game import (
    draw_vertical_winning_line,
    draw_horizontal_winning_line,
    draw_asc_diagonal,
    draw_desc_diagonal,
)


def mark_square(board, row, col, player):
    """Marca uma célula do tabuleiro para o jogador."""
    board[row][col] = player


def available_square(board, row, col):
    """Verifica se a célula está disponível."""
    return board[row][col] == 0


def is_board_full(board):
    """Retorna True se o tabuleiro estiver completamente preenchido."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win(screen, board, player):
    """Verifica se o jogador venceu e desenha a linha vencedora."""
    # Checa linhas verticais
    for col in range(BOARD_COLS):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            draw_vertical_winning_line(screen, col, player)
            return True

    # Checa linhas horizontais
    for row in range(BOARD_ROWS):
        if (
            board[row][0] == player
            and board[row][1] == player
            and board[row][2] == player
        ):
            draw_horizontal_winning_line(screen, row, player)
            return True

    # Checa diagonal decrescente
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(screen, player)
        return True

    # Checa diagonal crescente
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(screen, player)
        return True

    return False


def restart(board, screen, draw_lines, BG_COLOR):
    """Reinicia o jogo, limpando o tabuleiro e redesenhando as linhas."""
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = 0
    screen.fill(BG_COLOR)
    draw_lines(screen)
