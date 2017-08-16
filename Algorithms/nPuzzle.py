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


# an algorithm to solve the famous N-Puzzle problem
import math
from ADTs.AbstractDataStructures import Stack


# the up method, which returns the tuple state after making a move upwards
def up(state):
    n = len(state)
    grid_width = int(n**0.5)
    new_state = [num for num in state]
    index = new_state.index(0)
    # up move is not allowed if the blank tile is at the most upwards positions in the grid
    if index in range(0, grid_width, 1):
        return None
    else:
        new_state[index] = new_state[index-grid_width]
        new_state[index-grid_width] = 0

    return tuple(new_state)


# the down method, which returns the tuple state after making a move downwards
def down(state):
    n = len(state)
    grid_width = int(n**0.5)
    new_state = [num for num in state]
    index = new_state.index(0)
    # down move is not allowed if the blank tile is at the most downwards positions in the grid
    if index in range(n-grid_width, n, 1):
        return None
    else:
        new_state[index] = new_state[index+grid_width]
        new_state[index+grid_width] = 0

    return tuple(new_state)


# the left method, which returns the tuple state after making a move on the left
def left(state):
    n = len(state)
    grid_width = int(n**0.5)
    new_state = [num for num in state]
    index = new_state.index(0)
    # left move is not allowed if the blank tile is at the most left positions in the grid
    if index in [i for i in range(0, n, grid_width)]:
        return None
    else:
        new_state[index] = new_state[index-1]
        new_state[index-1] = 0

    return tuple(new_state)


# the right method, which returns the tuple state after making a move on the right
def right(state):
    n = len(state)
    grid_width = int(n**0.5)
    new_state = [num for num in state]
    index = new_state.index(0)
    # right move is not allowed if the blank tile is at the most right positions in the grid
    if index in [i for i in range(grid_width - 1, n, grid_width)]:
        return None
    else:
        new_state[index] = new_state[index+1]
        new_state[index+1] = 0

    return tuple(new_state)


# the heuristic function - manhattan distance
def heuristic_func(state):
    n = len(state)
    grid_width = n**0.5
    heuristic_val = 0
    for index, num in enumerate(state):
        # finding the current indices of the tile
        x = index % 3
        y = index // 3

        # finding the goal indices of the tile
        if num == 0:
            # the blank tile represented by 0 must be at the bottom-right place in the grid
            x_goal, y_goal = grid_width - 1, grid_width - 1
        else:
            goal_index = num - 1
            x_goal = goal_index % 3
            y_goal = goal_index // 3

        # incrementing the heuristic value
        heuristic_val += abs(x_goal - x) + abs(y_goal - y)

    return heuristic_val


# the is_solvable function, which checks if a given state has a solution
def is_solvable(state):
    inversions = 0
    n = len(state)
    grid_width = n**0.5
    index_blank = None
    covered_nums = []
    for index, num in enumerate(state):
        if num == 0:
            index_blank = index
            continue

        for test_num in covered_nums:
            if test_num > num:
                inversions += 1
        covered_nums.append(num)

    # if the grid width is odd, the number of inversions must be even
    if grid_width % 2 == 1:
        return inversions % 2 == 0
    # if the grid width is even, check the position of the blank tile - the tile with a 0 in this implementation
    else:
        # finding the row of the blank tile counting from the bottom
        row_blank = (index_blank // grid_width)
        row_blank = grid_width - row_blank
        # if row is even, the number of inversions must be odd
        if row_blank % 2 == 0:
            return inversions % 2 == 1
        # if row is odd, the number of inversions must be even
        else:
            return inversions % 2 == 0


# the is_end_state function checks if a state is our goal state
def is_end_state(state):
    n = len(state)
    return state == tuple(range(1, n)) + (0,)


# IDA* search - increasing depth limits combined with A* search
def n_puzzle(initial_state):
    # perform some checks for the initial_state argument
    if initial_state is None:
        raise ValueError("Initial state cannot be None")

    if type(initial_state) != tuple:
        raise TypeError("Initial state must be a tuple of ints")

    n = len(initial_state)
    grid_width = n**0.5

    if grid_width != int(grid_width):
        raise ValueError("The grid width must be an integer - the size of the state list must be 8, 15, 24, etc.")

    # assert the grid width is at least 3 tiles
    if grid_width < 3:
        raise ValueError("The grid width must be at least three")

    # check if the state contains the right numbers
    sorted_state = [num for num in initial_state]
    sorted_state.sort()
    if sorted_state != list(range(len(initial_state))):
        raise ValueError("The initial state must contain only the integers from 0 to the number of tiles + 1")

    # check if the initial state is solvable
    if not is_solvable(initial_state):
        raise ValueError("There are no solutions for the initial state")

    limit = heuristic_func(initial_state)
    path = Stack()
    path.push(initial_state)

    while True:
        result = a_star_search(path, limit)
        if type(result) == Stack:
            return list(iter(reverse_stack(result)))
        elif result == math.inf:
            raise ValueError("No solutions")
        else:
            limit = result


# helper function for the IDA* search
def a_star_search(path, limit):
    state = path.peek()
    total_cost = len(path) - 1 + heuristic_func(state)

    if is_end_state(state):
        return path

    if total_cost > limit:
        return total_cost

    min_cost = math.inf
    neighbours = [up(state), down(state), left(state), right(state)]
    for neighbour in neighbours:
        if neighbour is not None and neighbour not in path:
            path.push(neighbour)
            result = a_star_search(path, limit)
            if type(result) == Stack:
                return result
            elif min_cost > result:
                min_cost = result
            path.pop()

    return min_cost


# a utility method to reverse the elements in a stack
def reverse_stack(stack):
    reversed_stack = Stack()
    while not stack.is_empty():
        reversed_stack.push(stack.pop())
    return reversed_stack
