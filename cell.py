import pygame

class Cell:
    # initiates a new cell with the given parameters
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched = None
        self.row = row
        self.col = col
        self.screen = screen

    # sets cell value to the given value
    def set_cell_value(self, value):
        self.value = value

    # sets sketched values to the given value
    def set_sketched_values(self, value):
        self.sketched = value

    # draws the cell (with its value) on the screen
    def draw(self):
        pass