import pygame

# *** Pygame constants ***
# Windows size (Width x height)
WIDTH = 800
# Number of rows/columns in the grid
ROWS = 50

# *** Colour constants (in RGB) ***
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)

# Init pygame
pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont('Consolas', 18, bold=True)


class GridCell:
    def __init__(self, row, col, width, total_rows):
        # Position of the cell in the grid
        self.row = row
        self.col = col
        # Pixel position of the cell
        self.x = row * width
        self.y = col * width
        # Initial color of the cell
        self.color = WHITE
        # Size of the cell
        self.width = width
        self.total_rows = total_rows

    def draw(self, win):
        # Draw cell on the window
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def set_color(self, color):
        # Set the color of the cell (if it is empty thus currently white)
        if self.color == WHITE:
            self.color = color
            print(f"Debug Log: Cell [{self.row}, {self.col}] set to color {color}")
        else:
            print(f"Debug Log: Cell [{self.row}, {self.col}] already occupied; not allowed to change color")

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = GridCell(i, j, gap, rows)
            grid[i].append(cell)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        # Draw horizontal grid lines
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            # Draw vertical grid lines
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    # Fill the window with a white background
    win.fill(WHITE)

    for row in grid:
        for cell in row:
            # Draw each cell in the grid
            cell.draw(win)

    # Draw grid lines on top
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    # Determine row and column number of the clicked position
    row = y // gap
    col = x // gap

    return row, col


def draw_instructions(win):
    # Render line separately
    text1 = FONT.render("Left mouse: Draw obstacle", True, BLACK)
    text2 = FONT.render("Right mouse: Set start and endpoint", True, BLACK)
    text3 = FONT.render("Reset grid: Space", True, BLACK)
    # Position the text in top-right corner
    win.blit(text1, (WIDTH - text1.get_width() - 10, 10))
    win.blit(text2, (WIDTH - text2.get_width() - 10, 35))
    win.blit(text3, (WIDTH - text3.get_width() - 10, 60))


def reset_grid():
    # Creates a new and empty grid and the start and end cells (complete reset)
    return make_grid(ROWS, WIDTH), None, None

def main(win, width):
    # Create grid
    grid = make_grid(ROWS, width)
    start_cell = None
    end_cell = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        draw_instructions(win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Left mouse click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                # Change the color of the clicked cell
                cell.set_color(BLACK)
                print(f"Mouse click at: [{row}, {col}]")

            # Right mouse click
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                # Set start and end cells
                if start_cell is None:
                    start_cell = cell
                    cell.set_color(BLUE)
                    print(f"Start at: [{row}, {col}]")
                elif end_cell is None and cell != start_cell:
                    end_cell = cell
                    cell.set_color(ORANGE)
                    print(f"End at: [{row}, {col}]")

            # Space
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Reset grid and all vars to empty
                    grid, start_cell, end_cell = reset_grid()
                    print("Resetted grid")

    pygame.quit()

# Create window and set name
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Visualization - Example")
main(WIN, WIDTH)