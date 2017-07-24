"""
Copyright 2017 Nikolay Stanchev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


# an algorithm to solve the famous N-queens problem


# the main method used to solve the n-queen puzzle, argument n is number of queens to be placed
def n_queen(n, test_path=None):

    assert type(n) is int and n > 0, "Argument n must be a positive integer"

    if test_path is not None:
        assert type(test_path) == list and len(test_path) == 0

    return next_row(n, 0, [], test_path)


# the next_row method which returns a list with indices representing the solution, if there is one
def next_row(n, current_row, solution, test_path=None):
    # if we reached the last row, we are done, return the solution
    if current_row == n:
        return solution

    # else go through each column
    for index in range(n):
        if test_path is not None:
            test_path.append(solution + [index])

        # if we have a legal queen solution for now, go to the next place
        if legal_queen(index, current_row, solution):
            # append the next place in solutions
            solution.append(index)
            # recursively call next_row to continue with the next row
            new_solution = next_row(n, current_row+1, solution, test_path)
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
