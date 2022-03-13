from tkinter.tix import ROW
from sklearn import neighbors
from enums.Color import Color

class Cell:
    def __init__(self, x, y, parent=None, color=Color.WHITE.value, is_obstacle=False, width=5, action=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.color = color
        self.width = width
        self.g = self.h = float('inf')
        self.neighbours = []
        self.action = action

    def f(self):
        return self.g + self.h

    def get_coord(self):
        return (self.x, self.y)

    def get_position(self):
        return (self.x * self.width, self.y * self.width)

    def __add_non_obstacle_neighbour(self, grid, neighbour_coord):
        neighbour_x, neighbour_y = neighbour_coord        
        if neighbour_x >=0 and neighbour_x < grid.COLS and neighbour_y >= 0 and neighbour_y < grid.ROWS:
            neighbour_cell = grid[neighbour_coord]
            if neighbour_cell and not neighbour_cell.is_obstacle():
                self.neighbours.append(neighbour_cell)        

    def update_neighbours(self, grid):
        self.neighbours.clear()
        # add all eight members
        self.__add_non_obstacle_neighbour(grid, (self.x-1, self.y-1))       # up left
        self.__add_non_obstacle_neighbour(grid, (self.x, self.y-1))         # up
        self.__add_non_obstacle_neighbour(grid, (self.x+1, self.y-1))       # up right
        self.__add_non_obstacle_neighbour(grid, (self.x-1, self.y))         # left
        self.__add_non_obstacle_neighbour(grid, (self.x+1, self.y))         # right
        self.__add_non_obstacle_neighbour(grid, (self.x-1, self.y+1))       # down left
        self.__add_non_obstacle_neighbour(grid, (self.x, self.y+1))         # down
        self.__add_non_obstacle_neighbour(grid, (self.x+1, self.y+1))       # down right
            
    def __lt__(self, other):
        return self.f() < other.f()
    
    def is_not_visited(self):
        return self.color == Color.WHITE.value
    
    def is_opened(self):
        return self.color == Color.STEEL_BLUE.value
    
    def is_visited(self):
        return self.color == Color.CYAN.value

    def is_start(self):
        return self.color == Color.GREEN.value

    def is_goal(self):
        return self.color == Color.PURPLE.value

    def is_obstacle(self):
        return self.color == Color.BLACK.value

    def is_in_path(self):
        return self.color == Color.YELLOW.value

    def make_not_visited(self):
        self.color = Color.WHITE.value
    
    def make_opened(self):
        self.color = Color.STEEL_BLUE.value
    
    def make_visited(self):
        self.color = Color.CYAN.value

    def make_start(self):
        self.color = Color.GREEN.value

    def make_goal(self):
        self.color = Color.PURPLE.value

    def make_obstacle(self):
        self.color = Color.BLACK.value

    def make_in_path(self):
        self.color = Color.YELLOW.value
