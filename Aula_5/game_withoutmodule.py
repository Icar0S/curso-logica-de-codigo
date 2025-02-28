import pygame
import sys

# Inicialização do Pygame
pygame.init()

# --- Configurações da Tela e Constantes ---
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Cores
RED = (255, 0, 0)  # Jogador 1 (X)
BLUE = (0, 0, 255)  # Jogador 2 (O)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
WHITE = (255, 255, 255)

# Configuração da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha - Tic Tac Toe")
screen.fill(BG_COLOR)

# Inicializa o tabuleiro (0 = vazio, 1 = jogador X, 2 = jogador O)
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]


# --- Funções para desenhar o jogo ---
def draw_lines():
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


def draw_figures():
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


# --- Funções de Lógica do Jogo ---
def mark_square(row, col, player):
    """Marca uma célula do tabuleiro para o jogador."""
    board[row][col] = player


def available_square(row, col):
    """Verifica se a célula está disponível."""
    return board[row][col] == 0


def is_board_full():
    """Retorna True se o tabuleiro estiver completamente preenchido."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    """Verifica se o jogador venceu e desenha a linha vencedora."""
    # Checa linhas verticais
    for col in range(BOARD_COLS):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            draw_vertical_winning_line(col, player)
            return True

    # Checa linhas horizontais
    for row in range(BOARD_ROWS):
        if (
            board[row][0] == player
            and board[row][1] == player
            and board[row][2] == player
        ):
            draw_horizontal_winning_line(row, player)
            return True

    # Checa diagonal decrescente
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    # Checa diagonal crescente
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    """Desenha a linha vertical que indica a vitória."""
    pos_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (pos_x, 15), (pos_x, HEIGHT - 15), LINE_WIDTH)


def draw_horizontal_winning_line(row, player):
    """Desenha a linha horizontal que indica a vitória."""
    pos_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (15, pos_y), (WIDTH - 15, pos_y), LINE_WIDTH)


def draw_asc_diagonal(player):
    """Desenha a diagonal ascendente que indica a vitória."""
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)


def draw_desc_diagonal(player):
    """Desenha a diagonal descendente que indica a vitória."""
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)


def restart():
    """Reinicia o jogo, limpando o tabuleiro e redesenhando as linhas."""
    global board
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    screen.fill(BG_COLOR)
    draw_lines()


# --- Função Principal ---
def main():
    draw_lines()
    player = 1  # Jogador 1 começa (X)
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Processa o clique do mouse (jogada)
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x = event.pos[0]  # Coordenada X do clique
                mouse_y = event.pos[1]  # Coordenada Y do clique

                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = 2 if player == 1 else 1
                    draw_figures()

            # Reinicia o jogo ao pressionar a tecla "R"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

        pygame.display.update()
    return 0


if __name__ == "__main__":
    main()
