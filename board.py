import pygame
import copy
from cell import Cell
from sudoku_generator import generate_sudoku as generate

class Board:
    # initiates a new board with the given parameters
    def __init__(self, width, height, screen, difficulty):
        self.size = 9
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected = None
        self.cells = None
        self.original = []

        removed = None
        # determines number of squares to remove
        if difficulty == "easy":
            removed = 30
        elif difficulty == "medium":
            removed = 40
        elif difficulty == "hard":
            removed = 50

        # convert 2d array of numbers to 2d array of cells
        generated = generate(self.size, removed)
        for row in range(len(generated)):
            new_row = []

            for col in range(len(generated)):
                value = generated[row][col]
                new_row.append(Cell(value, row, col, screen))
            
            self.original.append(new_row)

        self.cells = copy.deepcopy(self.original)

    # draws the board on the given screen
    def draw(self):
        for row in range(9):
            pygame.draw.line(self.screen,"Black",(0,row*(self.height//9)),(self.width,row*(self.height//9)),10)
        for col in range(9):
            pygame.draw.line(self.screen,"Black",(col*(self.width//9),0),(col*(self.width//9),self.height),10)



    def print_board(self):
        for row in self.cell:
            for cell in row:
                print(cell.value, end = " ")
            print()

    # marks cell at (row, col) as the currently selected cell
    def select(self, row, col):
        self.selected = (row, col)

    # given an x and y, returns the corresponding row and column
    def click(self, x, y):
        pass

    # clears the selected cell (granted it was put in by the user)
    def clear(self):
        row, col = self.selected[0], self.selected[1]

        cell = self.cells[row][col]
        original = self.original[row][col]

        cell.value = original

    # sets the sketched value of the current selected cell to the given value
    def sketch(self, value):
        row, col = self.selected[0], self.selected[1]
        cell = self.cells[row][col]

        cell.sketched = value

    # sets the value of the current selected cell to the entered value
    def place_number(self, value):
        row, col = self.selected[0], self.selected[1]

        cell = self.cells[row][col]
        original = self.original[row][col]

        if original.value == 0:
            cell.value = value
        else:
            print("Cannot place value here")

    # resets all cells in the board to their original values
    def reset_to_original(self):
        self.cells = copy.deepcopy(self.original)

    # returns a boolean indicating whether the board is full
    def is_full(self):
        for row in self.cells:
            nums = set(row)

            if 0 in nums:
                return False

        for col in range(self.width):
            nums = set()

            for row in self.cells:
                nums.add(row[col])

            if 0 in nums:
                return False

        return True

    # updates the board display
    def update_board(self):
        pass

    # finds an empty cell and returns its row and col as a tuple
    def find_empty(self):
        for row in range(self.size):
            for col in range(self.size):
                cell = self.cells[row][col]
                
                if cell.value == 0:
                    return (row, col)

        return (-1, -1)

    # checks whether the board is solved
    def check_board(self):
        # check if all rows have 1-9
        for row in self.cells:
            nums = set(map(lambda x: x.value, row))

            if len(nums) != 9 or (0 in nums):
                return False

        # check if all columns have 1-9
        for col in range(self.size):
            nums = set()

            for row in self.cells:
                nums.add(row[col].value)

            if len(nums) != 9 or (0 in nums):
                return False

        return True