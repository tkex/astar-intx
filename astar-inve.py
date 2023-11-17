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
        # Set the color of the cell
        self.color = color
        print(f"Cell [{self.row}, {self.col}] set to color {color}")

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

def main(win, width):
    # Create grid
    grid = make_grid(ROWS, width)

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Left mouse click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                # Change the color of the clicked cell
                cell.set_color(BLACK)
                print(f"Mouse click at: [{row}, {col}]")

    pygame.quit()

# Create the window
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Visualization - Example")
main(WIN, WIDTH)