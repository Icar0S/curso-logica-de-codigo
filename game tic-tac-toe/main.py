import pygame
import sys

from screen import WIDTH, HEIGHT, BOARD_ROWS, BOARD_COLS, SQUARE_SIZE
from colors import BG_COLOR
from draw_game import draw_lines, draw_figures
from game_logic import mark_square, available_square, check_win, restart

# Inicialização do Pygame
pygame.init()

# Configuração da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha - Tic Tac Toe")
screen.fill(BG_COLOR)

# Inicializa o tabuleiro (0 = vazio, 1 = jogador X, 2 = jogador O)
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]


# --- Função Principal ---
def main():
    draw_lines(screen)
    player = 1  # Jogador 1 começa (X)
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Processa o clique do mouse (jogada)
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if available_square(board, clicked_row, clicked_col):
                    mark_square(board, clicked_row, clicked_col, player)
                    if check_win(screen, board, player):
                        game_over = True
                    player = 2 if player == 1 else 1
                    draw_figures(screen, board)

            # Reinicia o jogo ao pressionar a tecla "R"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart(board, screen, draw_lines, BG_COLOR)
                    player = 1
                    game_over = False

        pygame.display.update()


if __name__ == "__main__":
    main()
