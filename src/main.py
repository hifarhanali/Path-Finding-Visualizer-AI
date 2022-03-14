from Visualizer import Visualizer

if __name__ == "__main__":

    visualizer = Visualizer(CELL_WIDTH=12)
    visualizer.make_grid_from_file("input/map.txt")
    visualizer.start()
