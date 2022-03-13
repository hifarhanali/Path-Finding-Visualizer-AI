from Helper import Helper
import pygame
from enums.Color import Color


class Grid:
    def __init__(self, WINDOW_WIDTH=1200, WINDOW_HEIGHT=1000, CELL_WIDTH=5):
        self.CELL_WIDTH = CELL_WIDTH                       # width of a square cell
        self.ROWS = WINDOW_HEIGHT // self.CELL_WIDTH       # # of rows in the grid
        self.COLS = WINDOW_WIDTH // self.CELL_WIDTH        # # of cols in the grid
        self.grid = Helper.make_grid(self.COLS, self.ROWS, self.CELL_WIDTH)

    # update neighbours of each node
    def update_cells_neighbours(self):
        for row in self.grid:
            for cell in row:
                cell.update_neighbours(self)        

    # to draw a grid
    def draw(self, WINDOW):
        WINDOW.fill(Color.WHITE.value)
        self.__draw_cells(WINDOW)
        self.__draw_lines(WINDOW)

    # to draw cells in a grid
    def __draw_cells(self, WINDOW):
        for row in self.grid:
            for cell in row:
                pygame.draw.rect(WINDOW, cell.color,
                                cell.get_position() + (cell.width, cell.width))

    # to draw horizontal and verical lines in a grid
    def __draw_lines(self, WINDOW):
        # draw horizontal lines
        for r in range(self.ROWS):
            pygame.draw.line(WINDOW, Color.WHITE.value, (0, r * self.CELL_WIDTH),
                             (self.COLS * self.CELL_WIDTH, r * self.CELL_WIDTH))

        # draw horizontal lines
        for c in range(self.COLS):
            pygame.draw.line(WINDOW, Color.WHITE.value, (c * self.CELL_WIDTH, 0),
                             (c * self.CELL_WIDTH, self.COLS * self.CELL_WIDTH))

    def __getitem__(self, cell_coord):
        col, row = cell_coord
        return self.grid[row][col] if (row >= 0 and row < self.ROWS and col >=0 and col < self.COLS) else None