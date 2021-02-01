import copy

''' create an state that the Suduko is in based on the possible values of each square and the correct inputs already known in any relevant squares '''
class State():
    def __init__(self, possibilitiesIn, valuesIn):
        self.possibilities = possibilitiesIn
        self.values = valuesIn

''' creates a state where no correct values are known and so any values are possible '''
def create_empty_state():
    possibility_grid = [[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
                        [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
                        [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
                        [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
                        [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
                        [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
                        [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
                        [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
                        [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]]
    
    empty_values = [[None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None, None]]

    return State(possibility_grid, empty_values)

''' updates the known correct values in a suduko to the ones given as a parameter '''
def change_values_grid(stateIn, gridIn):
    stateIn.values = gridIn

''' updates the possible values for any of the variables (squares) in the suduko grid, using the known values of the grid '''
def update_possibility_grid(stateIn):
    for x in range(9):
        for y in range(9):
            if stateIn.values[x][y] != None:
                value = stateIn.values[x][y]
                for i in range(9):
                    if value in stateIn.possibilities[i][y] and i != x:
                        stateIn.possibilities[i][y].remove(value)
                        #print(f"removing value: {value} from position: ({i}, {y})")
                    elif i == x:
                        stateIn.possibilities[i][y] = [value]
                    if value in stateIn.possibilities[x][i] and i != y:
                        stateIn.possibilities[x][i].remove(value)
                        #print(f"removing value: {value} from position: ({x}, {i})")
                    elif i == y:
                        stateIn.possibilities[x][i] = [value]
                for a in range(3):
                    for b in range(3):
                        x1 = a + ((x)//3)*3
                        y1 = b + ((y)//3)*3
                        if value in stateIn.possibilities[x1][y1] and not (x1 == x and y1 == y):
                            stateIn.possibilities[x1][y1].remove(value)
                        elif x1 == x and y1 == y:
                            stateIn.possibilities[x][y] = [value]

''' uses the possibile values of each varible to update the known correct values of the grid '''
def fill_squares(stateIn):
    for x in range(9):
        for y in range(9):
            if len(stateIn.possibilities[x][y]) == 1 and stateIn.values[x][y] == None:
                value = stateIn.possibilities[x][y][0]
                stateIn.values[x][y] = value
                return "space filled"

    for x in range(9):
        domain = [1,2,3,4,5,6,7,8,9]
        for y in range(9):
            if stateIn.values[x][y] != None:
                domain.remove(stateIn.values[x][y])
        for num in domain:
            counter = 0
            locs = []
            for y in range(9):
                if num in stateIn.possibilities[x][y]:
                    counter += 1
                    locs.append([x, y])
            if counter == 1:
                stateIn.values[locs[0][0]][locs[0][1]] = num
                return "space filled"

    for y in range(9):
        domain = [1,2,3,4,5,6,7,8,9]
        for x in range(9):
            if stateIn.values[x][y] != None:
                domain.remove(stateIn.values[x][y])
        for num in domain:
            counter = 0
            locs = []
            for x in range(9):
                if num in stateIn.possibilities[x][y]:
                    counter += 1
                    locs.append([x, y])
            if counter == 1:
                stateIn.values[locs[0][0]][locs[0][1]] = num
                return "space filled"
    
    for x in range(3):
        for y in range(3):
            domain = [1,2,3,4,5,6,7,8,9]
            for a in range(3):
                for b in range(3):
                    X = 3*x + a
                    Y = 3*y + b
                    if stateIn.values[X][Y] != None:
                        domain.remove(stateIn.values[X][Y])
            for num in domain:
                counter = 0
                locs = []
                for a in range(3):
                    for b in range(3):
                        X = 3*x + a
                        Y = 3*y + b
                        if num in stateIn.possibilities[X][Y]:
                            counter += 1
                            locs.append([X, Y])
                            #print(f"num: {num}")
                            #print(f"pos: ({X}, {Y})")
                            #print(f"counter: {counter}")
                            #print(f"possibilities: {stateIn.possibilities[X][Y]}")
                            #print()
                if counter == 1:
                    stateIn.values[locs[0][0]][locs[0][1]] = num
                    return "space filled"

    return "cannot fill"

''' returns the variable (square) of the sudoku grid with the least possible values that does not have an already known value'''
def get_most_contrained_cell(stateIn):
    lengths = [[999999999, -999, -999]]
    for x in range(9):
        for y in range(9):
            possiblities_length = len(stateIn.possibilities[x][y])
            if possiblities_length > 1:
                current = lengths.pop()
                current_min = current[0]

                if possiblities_length < current_min:
                    lengths.append([possiblities_length, x, y])
                else:
                    lengths.append(current)
    return lengths[0]

''' determines if the suduko is solved '''
def goal_test(stateIn):
    for x in range(9):
        for y in range(9):
            if stateIn.values[x][y] == None:
                return False
    return True

''' determines if a sudoku grid is solvable given the current 'known correct' values '''
def valid(stateIn):
    for x in range(9):
        for y in range(9):
            if len(stateIn.possibilities[x][y]) == 0:
                return False
    return True

''' creates a suduko to solve - any 9x9 suduko can be inputed here to test or use this program '''
grid = [[6, None, 9, 7, 5, 1, None, 8, None],
        [None, None, None, None, None, 3, None, None, 4],
        [None, None, None, None, None, None, None, None, None],
        [2, None, None, None, None, None, 8, None, None],
        [None, None, 8, None, 6, 7, None, None, None],
        [None, None, None, None, None, 9, 1, 5, 6],
        [1, 5, None, 2, None, None, 4, None, None],
        [None, None, None, None, None, None, None, None, 5],
        [7, None, None, None, None, None, None, 6, None]]

''' solves the given suduko '''
def solve_sudoku(gridIn):
    state = create_empty_state()
    change_values_grid(state, gridIn)
    update_possibility_grid(state)
    result = fill_squares(state)
    while result != "cannot fill":
        update_possibility_grid(state)
        result = fill_squares(state)
    if goal_test(state):
        return state
    frontier = [state]
    while len(frontier) > 0:
        state = frontier.pop()
        cell = get_most_contrained_cell(state)
        for num in range(cell[0]):
            #print(f"range: {cell[0]}")
            #print(f"trying num: {num} from cell: {cell}")
            new_values = copy.deepcopy(state.values)
            new_possibilities = copy.deepcopy(state.possibilities)
            new_state = State(new_possibilities, new_values)
            new_state.values[cell[1]][cell[2]] = new_state.possibilities[cell[1]][cell[2]][num]
            update_possibility_grid(new_state)
            result = fill_squares(new_state)
            while result != "cannot fill":
                update_possibility_grid(new_state)
                result = fill_squares(new_state)
            if goal_test(new_state):
                return new_state
            if valid(new_state):
                frontier.append(new_state)
                #for row in new_state.possibilities:
                #    print(row)
                #print()
    print("cannot solve suduko")

''' displays the solved suduko to the user '''
for row in solve_sudoku(grid).values:
    print(row)
