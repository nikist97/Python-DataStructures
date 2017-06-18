# an algorithm to solve the famous N-queens problem


# the main method used to solve the n-queen puzzle, argument n is number of queens to be placed
def n_queen(n):

    assert type(n) is int and n > 0, "Argument n must be a positive integer"

    return next_row(n, 0, [])


# the next_row method which returns a list with indices representing the solution, if there is one
def next_row(n, current_row, solution):
    # if we reached the last row, we are done, return the solution
    if current_row == n:
        return solution

    # else go through each column
    for index in range(n):
        # if we have a legal queen solution for now, go to the next place
        if legal_queen(index, current_row, solution):
            # append the next place in solutions
            solution.append(index)
            # recursively call next_row to continue with the next row
            new_solution = next_row(n, current_row+1, solution)
            # if it didn't return None, return the solution
            if new_solution is not None:
                return new_solution

            # else backtrack and remove the index from solutions
            else:
                solution.remove(index)

    # returns None if invalid solution
    return None


# the legal_queen method which checks if the current solution is a valid one
def legal_queen(index, current_row, solution):
    # checks if any queen intermingles with another one, if so - return False
    for row in range(current_row):
        if solution[row] == index or solution[row] + current_row - row == index or\
                                        solution[row] - current_row + row == index:
            return False
    return True
