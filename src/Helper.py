from Cell import Cell
from enums.Color import Color
import pygame


class Helper:
    @staticmethod
    def make_grid(cols_count, rows_count, cell_width):
        return [[Cell(x, y, width=cell_width) for x in range(cols_count)] for y in range(rows_count)]

    @staticmethod
    def get_cell_coord(cell_width, mouse_pos):
        return (mouse_pos[0] // cell_width, mouse_pos[1] // cell_width)

    @staticmethod
    def get_path_points(path):
        return [(cell.x * cell.width + cell.width // 2, cell.y * cell.width + cell.width // 2) for cell in path if not cell.is_start() and not cell.is_goal()] if path else None

    @staticmethod
    def __set_path_points_color(path):
        if path:
            for cell in path:
                if not cell.is_start() and not cell.is_goal():
                    cell.make_in_path()

    @staticmethod
    def __draw_path(window, points, path_color):
        if points and len(points) >= 2:
            pygame.draw.lines(window, path_color, False, points, 5)
            pygame.display.update()

    @staticmethod
    def show_path(path, window, path_color=Color.LIGHT_BLACK.value):
        if path and len(path) >= 2:
            Helper.clear_path(path, window, mark_not_visited=False)
            Helper.__set_path_points_color(path)
            points = Helper.get_path_points(path)
            Helper.__draw_path(window, points, path_color)

    @staticmethod
    def clear_path(path, window, mark_not_visited=True):
        if path:
            for cell in path:
                if not cell.is_start() and not cell.is_goal():
                    if mark_not_visited:
                        cell.make_not_visited()
                    else:
                        cell.make_visited()
                    pygame.draw.rect(window, cell.color,
                                     cell.get_position() + (cell.width, cell.width))
