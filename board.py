import pygame
from cell import Cell

class Board:
    # initiates a new board with the given parameters
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected = None
        self.cells = []
        self.locked = []

        for col in range(height):
            self.cells.append([0] * width)

    # draws the board on the given screen
    def draw(self):
        pass

    # marks cell at (row, col) as the currently selected cell
    def select(self, row, col):
        selected = cells[row][col]

    # given an x and y, returns the corresponding row and column
    def click(self, x, y):
        pass

    # clears the selected cell (granted it was put in by the user)
    def clear(self):
        pass

    # sets the sketched value of the current selected cell to the given value
    def sketch(self, value):
        pass

    # sets the value of the current selected cell to the entered value
    def place_number(self, value):
        pass

    # resets all cells in the board to their original values
    def reset_to_original(self):
        pass

    # returns a boolean indicating whether the board is full
    def is_full(self):
        pass

    # updates the underlying 2d board
    def update_board(self):
        pass

    # finds an empty cell and returns its row and col as a tuple
    def find_empty(self):
        pass

    # checks whether the board is solved
    def check_board(self):
        pass