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
    def astar(draw, start, goal):
        move_generated_time = 0
        opened_cells = PriorityQueue()
        opened_cells.put(start)
        start.g = 0
        start.h = Heuristic.euclidean(start.get_coord(), goal.get_coord())
        while not opened_cells.empty():

            # if user quit during algorithm simulation, quit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()

            current_cell = opened_cells.get()

            # if we found goal node, construct path from start to goal node
            if current_cell == goal:
                goal.make_goal()
                return Path_Finding.__construct_path(start, goal)

            # for each neighbour node update its evaluation function
            for neighbour in current_cell.neighbours:
                if not neighbour.is_visited():
                    # update neighbour cell a better g and h value
                    if current_cell.g + 1 < neighbour.g:
                        neighbour.g = current_cell.g + 1
                        neighbour.h = Heuristic.euclidean(
                            neighbour.get_coord(), goal.get_coord())
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
    def learning_real_time_astar(draw, start, goal, window, cell_width):
        move_generated_time = 0
        should_run = True
        start.g = 0
        start.h = Heuristic.octile(start.get_coord(), goal.get_coord())

        prev_paths = []
        while should_run:
            current_cell = start
            new_path = [current_cell]
            while current_cell != goal:
                # if user quit during algorithm simulation, quit window
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()

                # get nearest neighbour
                nearest_cell = current_cell.neighbours[0]
                for neighbour in current_cell.neighbours:
                    neighbour.g = 1
                    if neighbour.h == float('inf'):
                        neighbour.h = Heuristic.octile(
                            neighbour.get_coord(), goal.get_coord())
                    if nearest_cell > neighbour:
                        nearest_cell = neighbour

                if current_cell != start:
                    current_cell.make_visited()

                try:
                    # remove additional nodes i.e backtracking
                    if nearest_cell != start:
                        cell_index = new_path.index(nearest_cell)
                        path_to_remove = new_path[cell_index:]
                        Helper.clear_path(path_to_remove, window)
                        new_path = new_path[: cell_index]
                except ValueError:
                    pass

                current_cell.h = nearest_cell.f()
                current_cell = nearest_cell

                current_cell.count = move_generated_time
                move_generated_time += 1
                new_path.append(current_cell)

            # remove previous path
            if len(prev_paths):
                Helper.clear_path(prev_paths[-1], window)

            if new_path in prev_paths:
                should_run = False

            # Helper.show_path(draw, new_path, start, goal)
            Helper.show_path(new_path, window)

            prev_paths.append(new_path)
        return new_path

    @staticmethod
    def real_time_astar(draw, grid, start, goal, window, cell_width):
        move_generated_time = 0
        start.g = 0
        start.h = Heuristic.octile(start.get_coord(), goal.get_coord())
        current_cell = start
        path = [current_cell]
        while current_cell != goal:
            # if user quit during algorithm simulation, quit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()

            Helper.show_path(path, window)
            # if user quit during algorithm simulation, quit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()

            # get nearest and second nearest neighbour
            nearest_cell = current_cell.neighbours[0]
            second_nearest_cell = current_cell.neighbours[0]
            for neighbour in current_cell.neighbours:
                neighbour.g = 1
                if neighbour.h == float('inf'):
                    neighbour.h = Heuristic.octile(
                        neighbour.get_coord(), goal.get_coord())
                if nearest_cell > neighbour:
                    second_nearest_cell = nearest_cell
                    nearest_cell = neighbour

            if current_cell != start:
                current_cell.make_visited()

            try:
                # remove additional nodes i.e backtracking
                if nearest_cell != start:
                    cell_index = path.index(nearest_cell)
                    path_to_remove = path[cell_index:]
                    Helper.clear_path(path_to_remove, window)
                    path = path[: cell_index]

            except ValueError:
                pass

            current_cell.h = second_nearest_cell.f()
            current_cell = nearest_cell
            current_cell.count = move_generated_time
            move_generated_time += 1
            path.append(current_cell)
        return path
