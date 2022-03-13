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
        
        start.g = 0
        start.h = Heuristic.manhattan(start.get_coord(), goal.get_coord())
        while not opened_cells.empty():
            
            # if user quit during algorithm simulation, quit window 
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit()         

            current_cell = opened_cells.get()[0]
            
            # if we found goal node, construct path from start to goal node
            if current_cell == goal:
                goal.make_goal()
                Path_Finding.__construct_path(draw, start, goal)
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