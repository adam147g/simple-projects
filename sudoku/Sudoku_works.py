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

board_place = [[None for _ in range(board_size)] for _ in range(board_size)]
numbers = [None for _ in range(board_size)]

for i in range(board_size):
    for j in range(board_size):
        x = board_x + j * cell_size
        y = board_y + i * cell_size
        new_button = Button((x, y), cell_size)
        board_place[i][j] = new_button

starter_x = board_x
starter_y = board_y + (board_size + 1) * cell_size
for i in range(board_size):
    new_button = Button((starter_x + cell_size * i, starter_y), cell_size, True, str(i))
    numbers[i] = new_button


def draw_komorki():
    for i in range(board_size):
        for j in range(board_size):
            to_draw = board_place[i][j]

            # Rysuj prostokąt
            pygame.draw.rect(screen, to_draw.color,
                             (to_draw.position[0], to_draw.position[1], to_draw.size, to_draw.size))

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
                board_place[i][j].position[0], board_place[i][j].position[1],
                3 * board_place[i][j].size, 3 * board_place[i][j].size), 3)

    for i in range(board_size):
        to_draw = numbers[i]
        # Rysuj prostokąt
        pygame.draw.rect(screen, to_draw.color, (to_draw.position[0], to_draw.position[1], to_draw.size, to_draw.size))

        # Rysuj obramowanie
        pygame.draw.rect(screen, black, (to_draw.position[0], to_draw.position[1], to_draw.size, to_draw.size), 1)

        confirm_text = font.render(to_draw.name, True, black)
        confirm_rect = confirm_text.get_rect(
            center=(to_draw.position[0] + to_draw.size // 2, to_draw.position[1] + to_draw.size // 2)
        )
        screen.blit(confirm_text, confirm_rect)


# Główna pętla gry
clicked_button = None
active_number = None
running = True
while running:
    screen.fill(white)
    draw_komorki()
    pygame.display.flip()  # Uaktualnij ekran


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_index_x = (mouse_y - board_y) // cell_size
            button_index_y = (mouse_x - board_x) // cell_size

            if active_number is not None:
                active_number.active = False
                active_number = None

            if 0 <= button_index_y < board_size and 0 <= button_index_x < board_size:
                if clicked_button is not None:
                    clicked_button.active = False
                    clicked_button = None
                clicked_button = board_place[button_index_x][button_index_y]
                clicked_button.active = True
            elif 0 <= button_index_y < board_size and button_index_x == board_size + 1:
                active_number = numbers[button_index_y]
                active_number.active = True
            elif clicked_button is not None:
                clicked_button.active = False
                clicked_button = None

            if active_number is not None and clicked_button is not None:
                clicked_button.name = active_number.name
