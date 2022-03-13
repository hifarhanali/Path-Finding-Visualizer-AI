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
        if start is None or goal is None: return None
        path = [goal]
        current = goal.parent
        while current is not None:
            path.append(current)
            current = current.parent
        return path[::-1]

    @staticmethod
    def __show_path(draw, start, goal):
        path = Path_Finding.__construct_path(start, goal)
        Path_Finding.__draw_path(draw, path)
        start.make_start()
        goal.make_goal()        
    
    @staticmethod
    def __draw_path(draw, path):
        if path:
            for cell in path:
                cell.make_in_path()
                draw()
    
    @staticmethod
    def astar_algorithm(draw, start, goal):        
        time_count = 0
        
        opened_cells = PriorityQueue()
        opened_cells.put((start, time_count))        
        
        start.g = 0
        start.h = Heuristic.manhattan(start.get_coord(), goal.get_coord())
        while not opened_cells.empty():
            
            # if user quit during algorithm simulation, quit window 
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit()         

            current_cell = opened_cells.get()[0]
            
            # if we found goal node, construct path from start to goal node
            if current_cell == goal:
                Path_Finding.__show_path(draw, start, goal)
                return True
            
            # for each neighbour node update its evaluation function            
            for neighbour in current_cell.neighbours:
                
                # update neighbour cell a better g and h value
                if current_cell.g + 1 < neighbour.g:
                    neighbour.g = current_cell.g + 1
                    neighbour.h = Heuristic.manhattan(neighbour.get_coord(), goal.get_coord())
                    neighbour.parent = current_cell
                    
                    if not neighbour.is_opened():
                        time_count += 1
                        opened_cells.put((neighbour, time_count))
                        neighbour.make_opened()
                        
            draw()
            if current_cell != start:
                current_cell.make_visited()
                
        return False
    
    @staticmethod
    def learning_real_time_astar_algorithm(draw, start, goal):
        start.g = 0
        start.h = Heuristic.octile(start.get_coord(), goal.get_coord())
        current_cell = start
        while current_cell != goal:

            nearest_cell = None            
            for neighbour in current_cell.neighbours:
                neighbour.g = 1
                neighbour.h = Heuristic.octile(neighbour.get_coord(), goal.get_coord())
            
                if not neighbour.is_visited():
                    if not nearest_cell or nearest_cell.f() > neighbour.f():
                        nearest_cell = neighbour

            if current_cell != start: 
                current_cell.make_visited()
            
            if nearest_cell is None:
                break

            nearest_cell.parent = current_cell
            nearest_cell.make_opened()

            current_cell.h = max(current_cell.h, nearest_cell.f()) 
            current_cell = nearest_cell
            draw()

        Path_Finding.__show_path(draw, start, goal)