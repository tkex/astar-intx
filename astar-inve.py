import pygame

# Width of windows
WIDTH = 800

# Window size (X * X)
WIN = pygame.display.set_mode((WIDTH, WIDTH))

# Set name of pygame program
pygame.display.set_caption("A* Visualisierung - Beispiel")

# Colour Constants in RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)

# Konstanten
WIDTH = 800
ROWS = 50  # Anzahl der Zeilen/Spalten im Gitter

# Initialisierung von Pygame
pygame.init()

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, rows, width):
    win.fill(WHITE)
    draw_grid(win, rows, width)
    pygame.display.update()

def main(win, width):
    run = True
    while run:
        draw(win, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

main(WIN, WIDTH)