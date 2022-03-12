from math import sqrt

class Heuristic:
    # euclidian distance
    @staticmethod
    def euclidean(node, goal):
        return sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)
    
    # manhattan distance
    @staticmethod
    def manhattan(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])