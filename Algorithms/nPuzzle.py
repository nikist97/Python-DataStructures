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


from ADTs.AbstractDataStructures import DuplicatePriorityQueue


# the n_puzzle function, which generates each move it tries until it reaches the goal state (up, down, left, right)
def n_puzzle(initial_state):
    if initial_state is None:
        raise ValueError("Initial state cannot be None")

    if type(initial_state) != tuple:
        raise TypeError("Initial state must be a tuple of ints")

    sorted_state = [num for num in initial_state]
    sorted_state.sort()
    if sorted_state != [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        raise ValueError("The initial state must contain only the integers from 0 to 8")

    if not is_solvable(initial_state):
        raise ValueError("There are no solutions for the initial state")

    queue = DuplicatePriorityQueue(tuple, reverse=True)
    explored = set()
    path_costs = {}
    queue.enqueue(initial_state, heuristic_func(initial_state))
    path_costs[initial_state] = []

    while not queue.is_empty():
        state = queue.dequeue()
        explored.add(state)
        path = path_costs[state]

        if is_end_state(state):
            path.append(state)
            print(len(explored), len(path)-1)
            return path

        neighbours = [up(state), down(state), left(state), right(state)]
        for neighbour in neighbours:
            if neighbour is not None:
                if not queue.contains_element(neighbour) and neighbour not in explored:
                    queue.enqueue(neighbour, len(path) + 1 + heuristic_func(neighbour))
                    path_costs[neighbour] = [x for x in path]
                    path_costs[neighbour].append(state)
                else:
                    try:
                        queue.replace_priority(neighbour, len(path) + 1 + heuristic_func(neighbour), -1)
                        path_costs[neighbour] = [x for x in path]
                        path_costs[neighbour].append(state)
                    except KeyError:
                        pass


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


# a utility method to get move between two consecutive states - "up", "down", "left" or "right"
def get_move(state, last_state):
    index = state.index(0)
    last_index = last_state.index(0)

    delta = index-last_index
    if delta == 1 and index not in [3, 6]:
        return "right"
    elif delta == -1 and index not in [2, 5]:
        return "left"
    elif delta == 3:
        return "down"
    elif delta == -3:
        return "up"


# the heuristic function - returns the number of improperly placed numbers
def heuristic_func(state):
    heuristic_val = 0
    for index, num in enumerate(state):
        if index != num-1 and num != 0:
            heuristic_val += 1
        elif index != 8 and num == 0:
            heuristic_val += 1
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
