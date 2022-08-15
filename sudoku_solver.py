import copy


class SudokuState:
    """ Object to define the current state of a sudoku with the values and possible values as lists of lists. """
    def __init__(self, possible_values_grid, values_grid):
        self.possible_values_grid = possible_values_grid
        self.values_grid = values_grid

    def set_values_grid(self, values_grid):
        self.values_grid = values_grid

    def set_possible_values_grid(self, possible_values_grid):
        self.possible_values_grid = possible_values_grid

    def update_possible_values_grid(self):
        """ Update the possible values grid using the current known values grid. """
        for x_cell_coord in range(9):
            for y_cell_coord in range(9):
                cell_value = self.values_grid[x_cell_coord][y_cell_coord]
                if cell_value is not None:
                    for temp_cell_coord in range(9):

                        # Set new horizontal cell possible values.
                        if temp_cell_coord == x_cell_coord:
                            self.possible_values_grid[temp_cell_coord][y_cell_coord] = {cell_value}
                        elif temp_cell_coord != x_cell_coord and cell_value in self.possible_values_grid[temp_cell_coord][y_cell_coord]:
                            self.possible_values_grid[temp_cell_coord][y_cell_coord].remove(cell_value)

                        # Set new vertical cell possible values.
                        if temp_cell_coord != y_cell_coord and cell_value in self.possible_values_grid[x_cell_coord][temp_cell_coord]:
                            self.possible_values_grid[x_cell_coord][temp_cell_coord].remove(cell_value)

                    # Set new 3 x 3 cage cell possible values
                    for temp_x_cell_coord_addition in range(3):
                        for temp_y_cell_coord_addition in range(3):
                            temp_x_cell_coord = temp_x_cell_coord_addition + (x_cell_coord // 3) * 3
                            temp_y_cell_coord = temp_y_cell_coord_addition + (y_cell_coord // 3) * 3
                            if (cell_value in self.possible_values_grid[temp_x_cell_coord][temp_y_cell_coord] and
                                not (temp_x_cell_coord == x_cell_coord and temp_y_cell_coord == y_cell_coord)):
                                self.possible_values_grid[temp_x_cell_coord][temp_y_cell_coord].remove(cell_value)

    def update_values_grid(self):
        ''' Update values grid using the current known possible values grid. '''

        changes_made = 0

        # If only 1 possible value in a cell, set the cell to be that value.
        for x_cell_coord in range(9):
            for y_cell_coord in range(9):
                if (len(self.possible_values_grid[x_cell_coord][y_cell_coord]) == 1 and
                        self.values_grid[x_cell_coord][y_cell_coord] is None):
                    self.values_grid[x_cell_coord][y_cell_coord] = (
                        self.possible_values_grid[x_cell_coord][y_cell_coord].pop()
                    )
                    changes_made += 1

        # If a possible value is only found in 1 cell in a vertical line
        # set that cell the be said value.
        for x_cell_coord in range(9):
            possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for y_cell_coord in range(9):
                if self.values_grid[x_cell_coord][y_cell_coord] is not None:
                    value = self.values_grid[x_cell_coord][y_cell_coord]
                    if value in possible_values:
                        possible_values.remove(value)
                    else:
                        # Invalid sudoku
                        # multiple of the same value in the same vertical line.
                        return -1
            for value in possible_values:
                counter = 0
                cell_coords = []
                for y_cell_coord in range(9):
                    if value in self.possible_values_grid[x_cell_coord][y_cell_coord]:
                        counter += 1
                        cell_coords.append([x_cell_coord, y_cell_coord])
                if counter == 1:
                    self.values_grid[cell_coords[0][0]][cell_coords[0][1]] = value
                    changes_made += 1

        # If a possible value is only found in 1 cell in a horizontal line
        # set that cell the be said value.
        for y_cell_coord in range(9):
            possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for x_cell_coord in range(9):
                if self.values_grid[x_cell_coord][y_cell_coord] is not None:
                    value = self.values_grid[x_cell_coord][y_cell_coord]
                    if value in possible_values:
                        possible_values.remove(value)
                    else:
                        # Invalid sudoku
                        # multiple of the same value in the same horizontal line.
                        return -1
            for value in possible_values:
                counter = 0
                cell_coords = []
                for x_cell_coord in range(9):
                    if value in self.possible_values_grid[x_cell_coord][y_cell_coord]:
                        counter += 1
                        cell_coords.append([x_cell_coord, y_cell_coord])
                if counter == 1:
                    self.values_grid[cell_coords[0][0]][cell_coords[0][1]] = value
                    changes_made += 1

        # If a possible value is only found in 1 cell in a 3 x 3 cell cage
        # set that cell the be said value.
        for x in range(3):
            for y in range(3):
                possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for temp_x_cell_coord_addition in range(3):
                    for temp_y_cell_coord_addition in range(3):
                        x_cell_coord = 3 * x + temp_x_cell_coord_addition
                        y_cell_coord = 3 * y + temp_y_cell_coord_addition
                        if self.values_grid[x_cell_coord][y_cell_coord] is not None:
                            value = self.values_grid[x_cell_coord][y_cell_coord]
                            if value in possible_values:
                                possible_values.remove(value)
                            else:
                                # Invalid sudoku
                                # multiple of the same value in the same 3 x 3 cage.
                                return -1
                for value in possible_values:
                    counter = 0
                    cell_coords = []
                    for temp_x_cell_coord_addition in range(3):
                        for temp_y_cell_coord_addition in range(3):
                            x_cell_coord = 3 * x + temp_x_cell_coord_addition
                            y_cell_coord = 3 * y + temp_y_cell_coord_addition
                            if value in self.possible_values_grid[x_cell_coord][y_cell_coord]:
                                counter += 1
                                cell_coords.append([x_cell_coord, y_cell_coord])
                    if counter == 1:
                        self.values_grid[cell_coords[0][0]][cell_coords[0][1]] = value
                        changes_made += 1

        return changes_made

    def is_solved(self):
        """ Determine if the sudoku is in a solved state. """
        for x_cell_coord in range(9):
            for y_cell_coord in range(9):
                if self.values_grid[x_cell_coord][y_cell_coord] is None:
                    return False
        return True

    def has_cell_without_possible_value(self):
        """ Determine if the sudoku state has any cells without a possible value. """
        for x_cell_coord in range(9):
            for y_cell_coord in range(9):
                if set() in self.possible_values_grid[x_cell_coord][y_cell_coord]:
                    # This cell has no possible values.
                    return True
        else:
            return False

    def solve_by_deduction(self):
        self.update_possible_values_grid()
        changes_made = self.update_values_grid()
        while changes_made > 0:
            self.update_possible_values_grid()
            changes_made = self.update_values_grid()
        if changes_made < 0:
            return "Has invalid value"

    def get_most_constrained_cell_coordinates(self):
        ''' returns the variable (square) of the sudoku grid with the least possible values that does not have an already known value'''
        least_possible_values = 10
        for x_cell_coord in range(9):
            for y_cell_coord in range(9):
                num_possible_values = len(self.possible_values_grid[x_cell_coord][y_cell_coord])
                if 1 < num_possible_values < least_possible_values:
                    most_constrained_coords = [x_cell_coord, y_cell_coord]

        return most_constrained_coords

    def solve_sudoku(self):
        has_invalid_value = self.solve_by_deduction()
        if has_invalid_value:
            return "Invalid"

        if self.has_cell_without_possible_value():
            return "Invalid"

        if self.is_solved():
            return "Solved"
        else:
            x_cell_coord, y_cell_coord = self.get_most_constrained_cell_coordinates()

            for value in self.possible_values_grid[x_cell_coord][y_cell_coord]:
                possible_values_grid_copy = copy.deepcopy(self.possible_values_grid)
                values_grid_copy = copy.deepcopy(self.values_grid)

                self.values_grid[x_cell_coord][y_cell_coord] = value
                self.possible_values_grid[x_cell_coord][y_cell_coord] = {value}

                result = self.solve_sudoku()

                if result == "Invalid":
                    self.set_possible_values_grid(possible_values_grid_copy)
                    self.set_values_grid(values_grid_copy)

                if result == "Solved":
                    return "Solved"

        return "Invalid"


def create_empty_state():
    """ Create an initial 9 x 9 sudoku state with no filled cells or excluded possible values. """
    possible_values_grid = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for i in range(9)] for i in range(9)]

    empty_values_grid = [[None for i in range(9)] for i in range(9)]

    return SudokuState(possible_values_grid=possible_values_grid, values_grid=empty_values_grid)


def solve_sudoku(input_sudoku_values_grid=None, print_result=True):
    """
    :param input_sudoku_values_grid: example: [
        [None, 8, None,    6, None, None,    None, None, None],
        [None, None, None,    5, None, None,    1, None, None],
        [None, None, 4,    None, 1, 8,    None, 2, None],

        [7, None, None,    None, None, None,    None, 4, None],
        [None, None, None,    1, None, None,    None, None, None],
        [None, 5, None,    None, 3, 9,    2, None, None],

        [None, 9, None,    None, 8, 2,    3, None, None],
        [None, None, 5,    None, None, None,    None, None, 9],
        [None, None, None,    None, None, 6,    None, None, None],
    ]

    :return example:
    Solving
    Sudoku solved.
    [5, 8, 1, 6, 2, 3, 7, 9, 4]
    [3, 7, 2, 5, 9, 4, 1, 8, 6]
    [9, 6, 4, 7, 1, 8, 5, 2, 3]
    [7, 1, 3, 2, 6, 5, 9, 4, 8]
    [8, 2, 9, 1, 4, 7, 6, 3, 5]
    [4, 5, 6, 8, 3, 9, 2, 1, 7]
    [6, 9, 7, 4, 8, 2, 3, 5, 1]
    [2, 4, 5, 3, 7, 1, 8, 6, 9]
    [1, 3, 8, 9, 5, 6, 4, 7, 2]
    """
    sudoku_state = create_empty_state()
    if input_sudoku_values_grid:
        sudoku_state.set_values_grid(input_sudoku_values_grid)
    result = sudoku_state.solve_sudoku()
    if result != "Solved":
        if print_result:
            print("Sudoku cannot be solved.")
        return None
    if result == "Solved":
        if print_result:
            print("Sudoku solved.")
            for line in sudoku_state.values_grid:
                print(line)
        return sudoku_state.values_grid
