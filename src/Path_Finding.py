import pygame
from Cell import Cell
from queue import PriorityQueue
from Heuristic import Heuristic
from Helper import Helper


class Path_Finding:

    @staticmethod
    def __construct_path(start, goal):
        if start is None or goal is None:
            return None
        path = [goal]
        current = goal.parent
        while current is not None:
            path.append(current)
            current = current.parent
        return path[::-1]

    @staticmethod
    def __init_cells_h_value(grid, goal):
        for row in grid:
            for cell in row:
                cell.h = Heuristic.octile(
                    cell.get_coord(), goal.get_coord())

    @staticmethod
    def __init_cells_g_value(grid, value_to_set):
        for row in grid:
            for cell in row:
                cell.g = value_to_set

    @staticmethod
    def __check_quit():
        # to quit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()

    @staticmethod
    def astar(draw, grid, start, goal):
        move_generated_time = 0     # to break ties

        opened_cells = PriorityQueue()
        opened_cells.put(start)

        start.g = 0
        Path_Finding.__init_cells_h_value(grid.grid, goal)
        while not opened_cells.empty():
            Path_Finding.__check_quit()

            current_cell = opened_cells.get()

            # if we found goal node, construct path from start to goal node
            if current_cell == goal:
                goal.make_goal()
                return Path_Finding.__construct_path(start, goal)

            # for each neighbour node update its evaluation function
            for neighbour in current_cell.neighbours:
                if not neighbour.is_visited() and not neighbour.is_start():
                    # update neighbour cell a better g value
                    if current_cell.g + 1 < neighbour.g:
                        neighbour.g = current_cell.g + 1
                        neighbour.parent = current_cell

                        if not neighbour.is_opened():
                            move_generated_time += 1
                            neighbour.count = move_generated_time
                            opened_cells.put(neighbour)
                            neighbour.make_opened()
            draw()
            if current_cell != start:
                current_cell.make_visited()
        return None

    @staticmethod
    def learning_real_time_astar(draw, grid, start, goal, window, cell_width):
        move_generated_time = 0     # to break ties

        start.g = 0
        Path_Finding.__init_cells_h_value(grid.grid, goal)
        Path_Finding.__init_cells_g_value(grid.grid, value_to_set=1)

        prev_paths = []
        should_run = True
        while should_run:
            current_cell = start
            new_path = [current_cell]
            while current_cell != goal:
                Path_Finding.__check_quit()

                # not path exists b/w start and goal node
                if len(current_cell.neighbours) <= 0:
                    return None

                # get nearest neighbour
                nearest_cell = current_cell.neighbours[0]
                for neighbour in current_cell.neighbours:
                    nearest_cell = min(nearest_cell, neighbour)

                if current_cell != start:
                    current_cell.make_in_path()

                try:
                    # remove additional nodes i.e backtracking
                    cell_index = new_path.index(nearest_cell)
                    path_to_remove = new_path[cell_index:]
                    Helper.clear_path(path_to_remove, window,
                                      mark_not_visited=False)
                    grid.draw_lines(window)
                    new_path = new_path[: cell_index]
                except ValueError:
                    pass

                current_cell.h = nearest_cell.f()
                current_cell = nearest_cell

                current_cell.count = move_generated_time
                move_generated_time += 1
                new_path.append(current_cell)

            if new_path in prev_paths:
                should_run = False

            # remove previous path
            if len(prev_paths):
                Helper.clear_path(
                    prev_paths[-1], window, mark_not_visited=False)
                grid.draw_lines(window)

            # Helper.show_path(draw, new_path, start, goal)
            Helper.show_path(new_path, window)

            prev_paths.append(new_path)
        return new_path

    @staticmethod
    def real_time_astar(draw, grid, start, goal, window, cell_width):
        move_generated_time = 0     # to break ties

        start.g = 0
        Path_Finding.__init_cells_h_value(grid.grid, goal)
        Path_Finding.__init_cells_g_value(grid.grid, value_to_set=1)

        current_cell = start
        path = [current_cell]
        while current_cell != goal:

            Path_Finding.__check_quit()
            # not path exists b/w start and goal node
            if len(current_cell.neighbours) <= 0:
                return None

            # get nearest and second nearest neighbour
            nearest_cell = current_cell.neighbours[0]
            second_nearest_cell = current_cell.neighbours[0]
            for neighbour in current_cell.neighbours:
                if nearest_cell > neighbour:
                    second_nearest_cell = nearest_cell
                    nearest_cell = neighbour

            try:
                # remove additional nodes i.e backtracking
                cell_index = path.index(nearest_cell)
                path_to_remove = path[cell_index:]
                Helper.clear_path(path_to_remove, window,
                                  mark_not_visited=False)
                grid.draw_lines(window)
                path = path[: cell_index]
            except ValueError:
                pass

            if current_cell != start:
                current_cell.make_in_path()

            current_cell.h = second_nearest_cell.f()
            current_cell = nearest_cell
            current_cell.count = move_generated_time
            move_generated_time += 1
            path.append(current_cell)

            Helper.show_path(path, window)
        return path
