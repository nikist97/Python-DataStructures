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
    new_state = [num for num in state]
    index = new_state.index(0)
    if index in range(0, 3):
        return None
    else:
        new_state[index] = new_state[index-3]
        new_state[index-3] = 0

    return tuple(new_state)


# the down method, which returns the tuple state after making a move downwards
def down(state):
    new_state = [num for num in state]
    index = new_state.index(0)
    if index in range(6, 9):
        return None
    else:
        new_state[index] = new_state[index+3]
        new_state[index+3] = 0

    return tuple(new_state)


# the left method, which returns the tuple state after making a move on the left
def left(state):
    new_state = [num for num in state]
    index = new_state.index(0)
    if index in [0, 3, 6]:
        return None
    else:
        new_state[index] = new_state[index-1]
        new_state[index-1] = 0

    return tuple(new_state)


# the right method, which returns the tuple state after making a move on the right
def right(state):
    new_state = [num for num in state]
    index = new_state.index(0)
    if index in [2, 5, 8]:
        return None
    else:
        new_state[index] = new_state[index+1]
        new_state[index+1] = 0

    return tuple(new_state)


# the heuristic function - manhattan distance
def heuristic_func(state):
    heuristic_val = 0
    for index, num in enumerate(state):
        x = index % 3
        if 0 <= index < 3:
            y = 0
        elif 3 <= index < 6:
            y = 1
        else:
            y = 2

        if num == 0:
            x_goal = 2
            y_goal = 2
        else:
            goal_index = num - 1
            x_goal = goal_index % 3
            if 0 <= goal_index < 3:
                y_goal = 0
            elif 3 <= goal_index < 6:
                y_goal = 1
            else:
                y_goal = 2

        heuristic_val += abs(x_goal - x) + abs(y_goal - y)

    return heuristic_val


# the is_solvable function, which checks if a given state has a solution
def is_solvable(state):
    inversions = 0
    covered_nums = []
    for num in state:
        if num == 0:
            continue

        for test_num in covered_nums:
            if num > test_num:
                inversions += 1
        covered_nums.append(num)

    return inversions % 2 == 0


# the is_end_state function checks if a state is our goal state
def is_end_state(state):
    return state == (1, 2, 3, 4, 5, 6, 7, 8, 0)


# IDA* search - increasing depth limits combined with A* search
def n_puzzle(initial_state):
    if initial_state is None:
        raise ValueError("Initial state cannot be None")

    if type(initial_state) != tuple:
        raise TypeError("Initial state must be a tuple of ints")

    sorted_state = [num for num in initial_state]
    sorted_state.sort()
    if sorted_state != list(range(9)):
        raise ValueError("The initial state must contain only the integers from 0 to 8")

    if not is_solvable(initial_state):
        raise ValueError("There are no solutions for the initial state")

    limit = heuristic_func(initial_state)
    path = Stack()
    path.push(initial_state)

    while True:
        result = a_star_search(path, limit)
        if type(result) == Stack:
            print(len(result) - 1)
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


# a utility method to reverse the elements in a stack into a new stack
def reverse_stack(stack):
    reversed_stack = Stack()
    while not stack.is_empty():
        reversed_stack.push(stack.pop())
    return reversed_stack
