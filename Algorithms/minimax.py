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


# minimax algorithm for tic-tac-toe game


# board is a 2D array representing the playing board
# turn is a variable to represent which turn is it (1 for the player calling minimax or -1 for the other player)
def minimax(board, turn=1):
    # state_scores holds the scores for each possible state for the next movie to be made
    state_scores = {}

    # check if the board is not in an end state
    if not end_state(board)[0]:
        # searching for the first available space
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    # choosing this place and calling minimax recursively to calculate the score if we choose this place
                    board[i][j] = turn
                    state_scores[(i, j)] = minimax(board, turn*(-1))[0]
                    # resetting the available space
                    board[i][j] = 0

    # if the board is in an end state put the score from the end state of the board: 10 for win, 0 for tie, -10 for loss
    else:
        state_scores[(-1, -1)] = end_state(board)[1]

    # if the turn is the turn of the player calling minimax
    if turn == 1:
        # get the maximum score and return it and the position associated with this score
        max_value = -20
        i = -1
        j = -1
        for test in state_scores:
            if state_scores[test] > max_value:
                max_value = state_scores[test]
                i, j = test
        return max_value, (i, j)

    # if the turn is the turn of the other player
    else:
        # get the minimum score and return it and the positioc associated with this score
        min_value = 20
        i = -1
        j = -1
        for test in state_scores:
            if state_scores[test] < min_value:
                min_value = state_scores[test]
                i, j = test
        return min_value, (i, j)


# the end_state method takes a 2D array representing the board as an argument and check if there is an end state
def end_state(board):
    # check for any kind of wins, returns a pair (boolean, score)
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:
            return True, board[i][0] * 10

        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            return True, board[0][i] * 10

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        return True, board[0][0] * 10

    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:
        return True, board[0][2] * 10

    # check for a filled board with no wins - a tie, returns a pair (boolean, 0)
    else:
        filled_board = True
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    filled_board = False

        if filled_board:
            return True, 0
        else:
            return False, 0
