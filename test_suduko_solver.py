import unittest

from suduko import solve_sudoku


class SudokuTests(unittest.TestCase):
    def test_empty_sudoku_input(self):
        empty_sudoku_input = [
            [None, None, None,    None, None, None,    None, None, None],
            [None, None, None,    None, None, None,    None, None, None],
            [None, None, None,    None, None, None,    None, None, None],

            [None, None, None,    None, None, None,    None, None, None],
            [None, None, None,    None, None, None,    None, None, None],
            [None, None, None,    None, None, None,    None, None, None],

            [None, None, None,    None, None, None,    None, None, None],
            [None, None, None,    None, None, None,    None, None, None],
            [None, None, None,    None, None, None,    None, None, None],
        ]

        empty_sudoku_expected_solution = [
            [2, 4, 6,    1, 3, 5,    8, 7, 9],
            [1, 3, 5,    8, 7, 9,    2, 4, 6],
            [8, 7, 9,    2, 4, 6,    1, 3, 5],

            [5, 6, 3,    4, 1, 2,    9, 8, 7],
            [4, 1, 2,    7, 9, 8,    5, 6, 3],
            [7, 9, 8,    5, 6, 3,    4, 1, 2],

            [6, 5, 4,    3, 2, 1,    7, 9, 8],
            [3, 2, 1,    9, 8, 7,    6, 5, 4],
            [9, 8, 7,    6, 5, 4,    3, 2, 1],
        ]

        empty_sudoku_solution = solve_sudoku(
            input_sudoku_values_grid=empty_sudoku_input,
            print_result=False
        )
        self.assertEqual(empty_sudoku_solution, empty_sudoku_expected_solution)

    def test_easy_sudoku_input(self):
        easy_sudoku_input = [
            [9, None, 6, None, 3, None, None, None, 1],
            [None, 3, None, None, None, None, 6, None, 8],
            [None, 5, None, 1, None, None, None, None, 3],

            [None, None, 9, None, 2, 4, None, None, None],
            [None, 8, None, None, None, None, None, 7, 2],
            [5, 7, 2, None, 9, 6, None, None, 4],

            [None, None, 7, None, None, None, 8, None, 9],
            [None, None, None, None, 8, None, 3, 4, None],
            [None, None, None, None, 1, None, 2, None, 5],
        ]

        easy_sudoku_expected_solution = [
            [9, 2, 6, 4, 3, 8, 7, 5, 1],
            [4, 3, 1, 2, 7, 5, 6, 9, 8],
            [7, 5, 8, 1, 6, 9, 4, 2, 3],

            [3, 1, 9, 7, 2, 4, 5, 8, 6],
            [6, 8, 4, 3, 5, 1, 9, 7, 2],
            [5, 7, 2, 8, 9, 6, 1, 3, 4],

            [2, 6, 7, 5, 4, 3, 8, 1, 9],
            [1, 9, 5, 6, 8, 2, 3, 4, 7],
            [8, 4, 3, 9, 1, 7, 2, 6, 5],
        ]

        easy_sudoku_solution = solve_sudoku(
            input_sudoku_values_grid=easy_sudoku_input,
            print_result=False
        )
        self.assertEqual(easy_sudoku_solution, easy_sudoku_expected_solution)

    def test_hard_sudoku_input(self):
        hard_sudoku_input = [
            [2, None, 5, 3, None, None, None, None, 9],
            [None, 3, None, 4, None, None, 8, 2, None],
            [None, 4, 8, None, None, None, 3, None, 1],

            [None, 2, None, None, None, None, None, None, None],
            [None, None, 4, None, None, None, 2, None, 8],
            [1, 6, 9, None, None, 4, 7, None, None],

            [None, None, 7, 1, None, None, 9, None, None],
            [None, None, None, None, 7, None, 1, None, None],
            [None, None, None, 2, None, None, None, None, 4],
        ]

        hard_sudoku_expected_solution = [
            [2, 1, 5, 3, 8, 7, 6, 4, 9],
            [9, 3, 6, 4, 1, 5, 8, 2, 7],
            [7, 4, 8, 9, 6, 2, 3, 5, 1],

            [8, 2, 3, 7, 5, 1, 4, 9, 6],
            [5, 7, 4, 6, 3, 9, 2, 1, 8],
            [1, 6, 9, 8, 2, 4, 7, 3, 5],

            [3, 5, 7, 1, 4, 6, 9, 8, 2],
            [4, 9, 2, 5, 7, 8, 1, 6, 3],
            [6, 8, 1, 2, 9, 3, 5, 7, 4],
        ]

        hard_sudoku_solution = solve_sudoku(
            input_sudoku_values_grid=hard_sudoku_input,
            print_result=False
        )
        self.assertEqual(hard_sudoku_solution, hard_sudoku_expected_solution)

    def test_expert_sudoku_input(self):
        expert_sudoku_input = [
            [None, None, None, None, 5, None, None, None, 9],
            [None, None, None, None, None, None, None, 8, None],
            [6, 8, 3, None, None, None, 4, None, None],

            [None, None, None, None, None, None, 9, None, None],
            [None, None, 8, None, 7, None, None, 6, 1],
            [7, None, None, None, 2, None, None, None, 5],

            [None, 5, None, None, 4, None, None, None, None],
            [None, None, 9, None, None, 1, 6, None, None],
            [None, 7, None, None, None, 6, None, None, 3],
        ]

        expert_sudoku_expected_solution = [
            [4, 2, 7, 6, 5, 8, 3, 1, 9],
            [9, 1, 5, 4, 3, 2, 7, 8, 6],
            [6, 8, 3, 9, 1, 7, 4, 5, 2],

            [1, 3, 2, 8, 6, 5, 9, 7, 4],
            [5, 9, 8, 3, 7, 4, 2, 6, 1],
            [7, 6, 4, 1, 2, 9, 8, 3, 5],

            [2, 5, 6, 7, 4, 3, 1, 9, 8],
            [3, 4, 9, 5, 8, 1, 6, 2, 7],
            [8, 7, 1, 2, 9, 6, 5, 4, 3],
        ]

        expert_sudoku_solution = solve_sudoku(
            input_sudoku_values_grid=expert_sudoku_input,
            print_result=False
        )
        self.assertEqual(expert_sudoku_solution, expert_sudoku_expected_solution)

    def test_evil_sudoku_input(self):
        evil_sudoku_input = [
            [None, 8, None, 6, None, None, None, None, None],
            [None, None, None, 5, None, None, 1, None, None],
            [None, None, 4, None, 1, 8, None, 2, None],

            [7, None, None, None, None, None, None, 4, None],
            [None, None, None, 1, None, None, None, None, None],
            [None, 5, None, None, 3, 9, 2, None, None],

            [None, 9, None, None, 8, 2, 3, None, None],
            [None, None, 5, None, None, None, None, None, 9],
            [None, None, None, None, None, 6, None, None, None],
        ]

        evil_sudoku_expected_solution = [
            [5, 8, 1, 6, 2, 3, 7, 9, 4],
            [3, 7, 2, 5, 9, 4, 1, 8, 6],
            [9, 6, 4, 7, 1, 8, 5, 2, 3],

            [7, 1, 3, 2, 6, 5, 9, 4, 8],
            [8, 2, 9, 1, 4, 7, 6, 3, 5],
            [4, 5, 6, 8, 3, 9, 2, 1, 7],

            [6, 9, 7, 4, 8, 2, 3, 5, 1],
            [2, 4, 5, 3, 7, 1, 8, 6, 9],
            [1, 3, 8, 9, 5, 6, 4, 7, 2],
        ]

        evil_sudoku_solution = solve_sudoku(
            input_sudoku_values_grid=evil_sudoku_input,
            print_result=False
        )
        self.assertEqual(evil_sudoku_solution, evil_sudoku_expected_solution)

    def test_impossible_sudoku_input(self):
        impossible_sudoku_input = [
            [1, 1, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],

            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],

            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
        ]

        impossible_sudoku_expected_solution = None

        impossible_sudoku_solution = solve_sudoku(
            input_sudoku_values_grid=impossible_sudoku_input,
            print_result=False
        )
        self.assertEqual(impossible_sudoku_solution, impossible_sudoku_expected_solution)
