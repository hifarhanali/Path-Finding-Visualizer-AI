from Grid import Grid
import pygame
from Helper import Helper
from Path_Finding import Path_Finding
from enums.Celll_Status import Cell_Status
from enums.Color import Color


class Visualizer:
    def __init__(self, WINDOW_WIDTH=1200, WINDOW_HEIGHT=700, CELL_WIDTH=20, WINDOW_TITLE="Rescue Path Simulator"):
        self.CELL_WIDTH = CELL_WIDTH            # width of a square cell
        self.WINDOW_WIDTH = WINDOW_WIDTH        # height of the window
        self.WINDOW_HEIGHT = WINDOW_HEIGHT      # width of the window
        self.WINDOW_TITLE = WINDOW_TITLE        # window title
        self.grid = Grid(self.WINDOW_WIDTH,
                         self.WINDOW_HEIGHT, self.CELL_WIDTH)

    def make_grid_from_file(self, filename, obstacle_symbol='@'):
        with open(filename) as f:
            cols_count = int(f.readline())
            rows_count = int(f.readline())
            self.WINDOW_WIDTH = cols_count * self.CELL_WIDTH
            self.WINDOW_HEIGHT = rows_count * self.CELL_WIDTH
            del self.grid
            self.grid = Grid(self.WINDOW_WIDTH,
                             self.WINDOW_HEIGHT, self.CELL_WIDTH)

            for y in range(rows_count):
                row = f.readline()
                for x in range(cols_count):
                    if row[x] == obstacle_symbol:
                        self.grid[(x, y)].color = Cell_Status.OBSTACLE.value

    def __draw_window(self):
        self.grid.draw(self.WINDOW)
        pygame.display.update()

    def start(self):
        pygame.init()
        self.WINDOW = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(self.WINDOW_TITLE)
        self.WINDOW.fill(Color.WHITE.value)

        start = goal = None
        should_quit = False
        clock = pygame.time.Clock()

        while not should_quit:
            clock.tick(30)
            for event in pygame.event.get():
                # quit widnow
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    should_quit = True

                # mosue clicks
                mouse_pos = pygame.mouse.get_pos()
                cell_coord = Helper.get_cell_coord(self.CELL_WIDTH, mouse_pos)
                cell = self.grid[cell_coord]

                if cell:
                    LEFT_CLICK, MIDDLE_CLICK, RIGHT_CLICK = pygame.mouse.get_pressed()

                    # mouse left click
                    if LEFT_CLICK:
                        if not start and cell != goal:
                            start = cell
                            start.make_start()
                        elif not goal and cell != start:
                            goal = cell
                            goal.make_goal()
                        elif cell != start and cell != goal:
                            cell.make_obstacle()
                    # mouse right click
                    elif RIGHT_CLICK:
                        cell.make_not_visited()
                        if cell == start:
                            start = None
                        if cell == goal:
                            goal = None

                if event.type == pygame.KEYDOWN:
                    self.grid.update_cells_neighbours()
                    path = None
                    if start and goal:
                        if event.key == pygame.K_1:
                            path = Path_Finding.astar(
                                lambda: self.__draw_window(), self.grid, start, goal)

                        elif event.key == pygame.K_2:
                            path = Path_Finding.learning_real_time_astar(
                                lambda: self.__draw_window(), self.grid, start, goal, self.WINDOW, self.CELL_WIDTH)

                        elif event.key == pygame.K_3:
                            path = Path_Finding.real_time_astar(
                                lambda: self.__draw_window(), self.grid, start, goal, self.WINDOW, self.CELL_WIDTH)

                        self.__draw_window()
                        Helper.show_path(path, self.WINDOW)

                    if event.key == pygame.K_SPACE:
                        self.grid.reset(should_remove_obstacles=False)
            self.__draw_window()
        pygame.quit()
