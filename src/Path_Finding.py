from hashlib import new
from operator import ne
from tkinter import N
import pygame
from Cell import Cell
from queue import PriorityQueue
from Heuristic import Heuristic


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
    def astar_algorithm(draw, start, goal):
        time_count = 0
        opened_cells = PriorityQueue()
        opened_cells.put((start, time_count))

        start.g = 0
        start.h = Heuristic.octile(start.get_coord(), goal.get_coord())
        while not opened_cells.empty():

            # if user quit during algorithm simulation, quit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()

            current_cell = opened_cells.get()[0]

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
                        neighbour.h = Heuristic.octile(
                            neighbour.get_coord(), goal.get_coord())
                        neighbour.parent = current_cell

                        if not neighbour.is_opened():
                            time_count += 1
                            opened_cells.put((neighbour, time_count))
                            neighbour.make_opened()
            draw()
            if current_cell != start:
                current_cell.make_visited()
        return None

    @staticmethod
    def learning_real_time_astar_algorithm(draw, start, goal):
        start.g = 0
        start.h = Heuristic.octile(start.get_coord(), goal.get_coord())
        current_cell = start
        while current_cell != goal:
            # if user quit during algorithm simulation, quit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()

            nearest_cell = None
            for neighbour in current_cell.neighbours:
                neighbour.g = 1
                neighbour.h = Heuristic.octile(
                    neighbour.get_coord(), goal.get_coord())
                if not neighbour.is_visited():
                    if not nearest_cell or nearest_cell.f() > neighbour.f():
                        nearest_cell = neighbour

            if current_cell != start:
                current_cell.make_visited()

            if nearest_cell:
                nearest_cell.parent = current_cell
                nearest_cell.make_opened()
                current_cell.h = nearest_cell.f()
                current_cell = nearest_cell
                draw()
            else:
                return None
        goal.make_goal()
        return Path_Finding.__construct_path(start, goal)

    @staticmethod
    def real_time_astar_algorithm(draw, start, goal):
        start.g = 0
        start.h = Heuristic.octile(start.get_coord(), goal.get_coord())
        current_cell = start
        while current_cell != goal:
            # if user quit during algorithm simulation, quit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()

            nearest_cell = None
            second_nearest_cell = None
            for neighbour in current_cell.neighbours:
                if not neighbour.is_visited():
                    neighbour.g = 1
                    neighbour.h = Heuristic.octile(
                        neighbour.get_coord(), goal.get_coord())
                    if nearest_cell:
                        if nearest_cell.f() > neighbour.f():
                            second_nearest_cell = nearest_cell
                            nearest_cell = neighbour
                    else:
                        nearest_cell = neighbour

            if current_cell != start:
                current_cell.make_visited()

            if nearest_cell:
                nearest_cell.parent = current_cell
                nearest_cell.make_opened()
                if second_nearest_cell:
                    current_cell.h = second_nearest_cell.f()
                current_cell = nearest_cell
                draw()
            else:
                return None
        goal.make_goal()
        return Path_Finding.__construct_path(start, goal)

    @staticmethod
    def real_time_astar(draw, start, goal):
        start.g = 0
        start.h = Heuristic.octile(start.get_coord(), goal.get_coord())
        current_cell = start

        path = []
        while current_cell != goal:
            # if user quit during algorithm simulation, quit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()

            nearest_cell = current_cell.neighbours[0]
            second_nearest_cell = current_cell.neighbours[0]
            for neighbour in current_cell.neighbours:
                neighbour.g = 1
                if not neighbour.is_visited() and not neighbour.is_start():
                    neighbour.h = Heuristic.octile(
                        neighbour.get_coord(), goal.get_coord())

                if neighbour == goal:
                    nearest_cell = goal
                    break

                if nearest_cell > neighbour:
                    second_nearest_cell = nearest_cell
                    nearest_cell = neighbour

            if current_cell != start:
                current_cell.make_visited()

            if current_cell.parent == nearest_cell:
                current_cell.parent = None
            nearest_cell.parent = current_cell
            current_cell.h = second_nearest_cell.f()
            current_cell = nearest_cell
            draw()

        start.make_start()
        goal.make_goal()
        return Path_Finding.__construct_path(start, goal)
