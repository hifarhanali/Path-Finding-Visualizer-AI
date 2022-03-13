from Grid import Grid
import pygame
from Helper import Helper
from Path_Finding import Path_Finding

class Visualizer:
    def __init__(self, WINDOW_WIDTH=900, WINDOW_HEIGHT=800, CELL_WIDTH=20, WINDOW_TITLE="A* Path Visualizer"):
        self.CELL_WIDTH = CELL_WIDTH            # width of a square cell
        self.WINDOW_WIDTH = WINDOW_WIDTH        # height of the window
        self.WINDOW_HEIGHT = WINDOW_HEIGHT      # width of the window
        self.WINDOW_TITLE = WINDOW_TITLE        # window title
        self.grid = Grid(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.CELL_WIDTH)

    def start(self):
        pygame.init()
        self.WINDOW = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(self.WINDOW_TITLE)

        start = goal = None
        should_quit = False
        is_simulation_started = False
        clock = pygame.time.Clock()

        while not should_quit:
            clock.tick(30)

            for event in pygame.event.get():
                # quit widnow
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE : should_quit = True

                # don't disturb simulation if it's already started
                if is_simulation_started: continue

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
                    if event.key == pygame.K_1 and not is_simulation_started:
                        Path_Finding.astar_algorithm(lambda: self.__draw_window(), start, goal)

                    elif event.key == pygame.K_2 and not is_simulation_started:
                        self.grid.update_cells_neighbours()
                        Path_Finding.learning_real_time_astar_algorithm(lambda: self.__draw_window(), start, goal)

                    elif event.key == pygame.K_3 and not is_simulation_started:
                        self.grid.update_cells_neighbours()
                        Path_Finding.real_time_astar_algorithm(lambda: self.__draw_window(), start, goal)
                        
                    elif event.key == pygame.K_SPACE:
                        start = goal = None
                        del self.grid
                        self.grid = Grid(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.CELL_WIDTH)

            self.__draw_window()
            pygame.display.flip()
        pygame.quit()

    def __draw_window(self):
        self.grid.draw(self.WINDOW)
        pygame.display.update()