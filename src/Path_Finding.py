import pygame
from Cell import Cell
from queue import PriorityQueue
from Heuristic import Heuristic

class Path_Finding:
    
    @staticmethod
    def __construct_path(draw, start, goal):
        if start == None or goal == None or start == goal: return
        current = goal.parent
        while current != start:
            current.make_in_path()
            current = current.parent
            draw()
    
    @staticmethod
    def a_star_algorithm(draw, start, goal):        
        time_count = 0
        
        opened_cells = PriorityQueue()
        opened_cells.put((start, time_count))        
        opened_cells_hash = {start}
        
        start.g = 0
        start.h = Heuristic.manhattan(start.get_coord(), goal.get_coord())
        while not opened_cells.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit()         

            current_cell = opened_cells.get()[0]
            opened_cells_hash.remove(current_cell)
            
            if current_cell == goal:
                goal.make_goal() 
                Path_Finding.__construct_path(draw, start, goal)
                return True
            
            for neighbour in current_cell.neighbours:
                if current_cell.g + 1 < neighbour.g:
                    neighbour.g = current_cell.g + 1
                    neighbour.h = Heuristic.manhattan(neighbour.get_coord(), goal.get_coord())
                    neighbour.parent = current_cell
                    
                    if neighbour not in opened_cells_hash:
                        time_count += 1
                        opened_cells.put((neighbour, time_count))
                        opened_cells_hash.add(neighbour)
                        neighbour.make_opened()
                        
            draw()
            if current_cell != start:
                current_cell.make_visited()
                
        return False