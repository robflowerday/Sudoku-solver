# Sudoku-Solver
This program can solve any 9 x 9 suduko and return the solved result to the user.

To use the program find or create a Sudoku input grid you wish to solve and pass it to the solve_sudoku() function in the following format (an empty sudoku would be accepted):

[
    [None, 8,    None,     6,    None, None,     None, None, None],
    [None, None, None,     5,    None, None,     1,    None, None],
    [None, None, 4,        None, 1,    8,        None, 2,    None],
    [7,    None, None,     None, None, None,     None, 4,    None],
    [None, None, None,     1,    None, None,     None, None, None],
    [None, 5,    None,     None, 3,    9,        2,    None, None],
    [None, 9,    None,     None, 8,    2,        3,    None, None],
    [None, None, 5,        None, None, None,     None, None, 9   ],
    [None, None, None,     None, None, 6,        None, None, None],
]

If a solution cannot be found you will be notified, otherwise the resulting sudoku will be returned and printed, unless print_result argument of the solve_sudoku() function is set to False.
