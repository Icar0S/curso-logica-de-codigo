# drawing.py
import pygame
from colors import BLUE, LINE_COLOR, RED
from screen import (
    WIDTH,
    HEIGHT,
    SQUARE_SIZE,
    LINE_WIDTH,
    CIRCLE_RADIUS,
    CIRCLE_WIDTH,
    CROSS_WIDTH,
    SPACE,
    BOARD_ROWS,
    BOARD_COLS,
)


def draw_lines(screen):
    """Desenha as linhas do tabuleiro."""
    # Linhas horizontais
    pygame.draw.line(
        screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH
    )
    pygame.draw.line(
        screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH
    )
    # Linhas verticais
    pygame.draw.line(
        screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH
    )
    pygame.draw.line(
        screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH
    )


def draw_figures(screen, board):
    """Desenha os X e O no tabuleiro conforme as jogadas."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                # Desenha o X (jogador 1)
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (
                    (col + 1) * SQUARE_SIZE - SPACE,
                    (row + 1) * SQUARE_SIZE - SPACE,
                )
                pygame.draw.line(screen, RED, start_desc, end_desc, CROSS_WIDTH)
                start_asc = (col * SQUARE_SIZE + SPACE, (row + 1) * SQUARE_SIZE - SPACE)
                end_asc = ((col + 1) * SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, RED, start_asc, end_asc, CROSS_WIDTH)
            elif board[row][col] == 2:
                # Desenha o O (jogador 2)
                center = (
                    col * SQUARE_SIZE + SQUARE_SIZE // 2,
                    row * SQUARE_SIZE + SQUARE_SIZE // 2,
                )
                pygame.draw.circle(screen, BLUE, center, CIRCLE_RADIUS, CIRCLE_WIDTH)


def draw_vertical_winning_line(screen, col, player):
    """Desenha a linha vertical que indica a vitória."""
    pos_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (pos_x, 15), (pos_x, HEIGHT - 15), LINE_WIDTH)


def draw_horizontal_winning_line(screen, row, player):
    """Desenha a linha horizontal que indica a vitória."""
    pos_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (15, pos_y), (WIDTH - 15, pos_y), LINE_WIDTH)


def draw_asc_diagonal(screen, player):
    """Desenha a diagonal ascendente que indica a vitória."""
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)


def draw_desc_diagonal(screen, player):
    """Desenha a diagonal descendente que indica a vitória."""
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)
