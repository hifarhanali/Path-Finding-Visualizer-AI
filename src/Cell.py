from enums.Celll_Status import Cell_Status


class Cell:
    def __init__(self, x, y, parent=None, color=Cell_Status.NOT_VISITED.value, width=5, count=0, action=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.color = color
        self.width = width
        self.g = self.h = float('inf')
        self.neighbours = []
        self.count = count
        self.action = action

    def f(self):
        return self.g + self.h

    def get_coord(self):
        return (self.x, self.y)

    def get_position(self):
        return (self.x * self.width, self.y * self.width)

    def __add_non_obstacle_neighbour(self, grid, neighbour_coord):
        neighbour_x, neighbour_y = neighbour_coord
        if neighbour_x >= 0 and neighbour_x < grid.COLS and neighbour_y >= 0 and neighbour_y < grid.ROWS:
            neighbour_cell = grid[neighbour_coord]
            if neighbour_cell and not neighbour_cell.is_obstacle():
                self.neighbours.append(neighbour_cell)

    def update_neighbours(self, grid):
        self.neighbours.clear()
        # add all eight members
        self.__add_non_obstacle_neighbour(
            grid, (self.x, self.y-1))         # up
        self.__add_non_obstacle_neighbour(
            grid, (self.x-1, self.y))         # left
        self.__add_non_obstacle_neighbour(
            grid, (self.x+1, self.y))         # right
        self.__add_non_obstacle_neighbour(
            grid, (self.x, self.y+1))         # down
        self.__add_non_obstacle_neighbour(
            grid, (self.x-1, self.y-1))       # up left
        self.__add_non_obstacle_neighbour(
            grid, (self.x+1, self.y+1))       # down right
        self.__add_non_obstacle_neighbour(
            grid, (self.x+1, self.y-1))       # up right
        self.__add_non_obstacle_neighbour(
            grid, (self.x-1, self.y+1))       # down left

    def __lt__(self, other):
        return \
            self.f() < other.f() or (
                self.f() == other.f() and (
                    self.h < other.h or (
                        self.h == other.h and (
                            self.g < other.g or (
                                self.g == other.g and self.count < other.count
                            )
                        )
                    )
                )
            )

    def is_not_visited(self):
        return self.color == Cell_Status.NOT_VISITED.value

    def is_opened(self):
        return self.color == Cell_Status.OPENED.value

    def is_visited(self):
        return self.color == Cell_Status.VISITED.value

    def is_start(self):
        return self.color == Cell_Status.START.value

    def is_goal(self):
        return self.color == Cell_Status.GOAL.value

    def is_obstacle(self):
        return self.color == Cell_Status.OBSTACLE.value

    def is_in_path(self):
        return self.color == Cell_Status.IN_PATH.value

    def make_not_visited(self):
        self.color = Cell_Status.NOT_VISITED.value

    def make_opened(self):
        self.color = Cell_Status.OPENED.value

    def make_visited(self):
        self.color = Cell_Status.VISITED.value

    def make_start(self):
        self.color = Cell_Status.START.value

    def make_goal(self):
        self.color = Cell_Status.GOAL.value

    def make_obstacle(self):
        self.color = Cell_Status.OBSTACLE.value

    def make_in_path(self):
        self.color = Cell_Status.IN_PATH.value
