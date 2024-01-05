import pygame
from Button import Button

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
window_size = (400, 700)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Sudoku")

# Kolor tła i planszy
white = (255, 255, 255)
black = (0, 0, 0)
grey = (100, 100, 100)

# Rozmiar planszy (9x9)
board_size = 9

# Rozmiar komórek
cell_size = window_size[0] // board_size

# Oblicz współrzędne X i Y, aby wyśrodkować planszę
board_x = (window_size[0] - (board_size * cell_size)) // 2
board_y = (window_size[1] - (board_size * cell_size)) // 2

# Czcionka dla wartości w komórkach
font = pygame.font.Font(None, 36)

buttons = [[None for _ in range(board_size)] for _ in range(board_size)]
for i in range(board_size):
    for j in range(board_size):
        x = board_x + j * cell_size
        y = board_y + i * cell_size
        new_button = Button((x, y), cell_size, str(i * board_size + j))
        buttons[i][j] = new_button


def draw_komorki():
    for i in range(board_size):
        for j in range(board_size):
            to_draw = buttons[i][j]

            # Rysuj prostokąt
            if to_draw.active:
                pygame.draw.rect(screen, grey, (to_draw.position[0], to_draw.position[1], to_draw.size, to_draw.size))
            else:
                pygame.draw.rect(screen, white, (to_draw.position[0], to_draw.position[1], to_draw.size, to_draw.size))

            # Rysuj obramowanie
            pygame.draw.rect(screen, black, (to_draw.position[0], to_draw.position[1], to_draw.size, to_draw.size), 1)

            confirm_text = font.render(to_draw.name, True, black)
            confirm_rect = confirm_text.get_rect(
                center=(to_draw.position[0] + to_draw.size // 2, to_draw.position[1] + to_draw.size // 2)
            )
            screen.blit(confirm_text, confirm_rect)
    for i in range(0, board_size, int(board_size ** (1 / 2))):
        for j in range(0, board_size, int(board_size ** (1 / 2))):
            pygame.draw.rect(screen, black, (
                buttons[i][j].position[0], buttons[i][j].position[1],
                3 * buttons[i][j].size, 3 * buttons[i][j].size), 3)


# Główna pętla gry
clicked_button = None
running = True
while running:

    screen.fill(white)
    draw_komorki()
    pygame.display.flip()  # Uaktualnij ekran

    # Uśpij kod na 1 sekundę
    # pygame.time.delay(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_index = (mouse_y - board_y) // cell_size * board_size + (mouse_x - board_x) // cell_size
            if 0 <= button_index < board_size**2:
                if clicked_button is not None:
                    clicked_button.active = False
                clicked_button = buttons[button_index // board_size][button_index % board_size]
                clicked_button.active = True
