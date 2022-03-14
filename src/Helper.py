from Cell import Cell


class Helper:
    @staticmethod
    def make_grid(cols_count, rows_count, cell_width):
        return [[Cell(x, y, width=cell_width) for x in range(cols_count)] for y in range(rows_count)]

    @staticmethod
    def get_cell_coord(cell_width, mouse_pos):
        return (mouse_pos[0] // cell_width, mouse_pos[1] // cell_width)

    @staticmethod
    def show_path(draw, path, start, goal):
        if path:
            for cell in path:
                if cell != start and cell != goal:
                    cell.make_in_path()
            draw()
