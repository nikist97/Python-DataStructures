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
    if turn == 1:
        optimal_value = -20
    else:
        optimal_value = 20
    position = -1, -1

    # check if the board is not in an end state
    if not end_state(board)[0]:
        # searching for the first available space
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    # choosing this place and calling minimax recursively to calculate the score if we choose this place
                    board[i][j] = turn
                    result = minimax(board, turn*(-1))
                    if turn == 1 and optimal_value < result[1]:
                        optimal_value = result[1]
                        position = (i, j)
                    elif turn == -1 and optimal_value > result[1]:
                        optimal_value = result[1]
                        position = (i, j)

                    # resetting the available space
                    board[i][j] = 0

    # if the board is in an end state put the score from the end state of the board: 10 for win, 0 for tie, -10 for loss
    else:
        position = -1, -1
        optimal_value = end_state(board)[1]

    return position, optimal_value


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
                    break

        if filled_board:
            return True, 0
        else:
            return False, 0


# minimax algorithm with alpha-beta pruning
def pruned_minimax(board, turn=1, alpha=None, beta=None):
    if alpha is None:
        alpha = -float("inf")
    if beta is None:
        beta = float("inf")

    state = end_state(board)
    position = -1, -1

    # check if the board is not in an end state
    if not state[0]:
        # searching for the first available space
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    # choosing this place and calling minimax recursively to calculate the score if we choose this place
                    board[i][j] = turn
                    result = pruned_minimax(board, turn * (-1), alpha, beta)

                    if turn == 1 and result[2] > alpha:
                        alpha = result[2]
                        position = (i, j)
                    elif turn == -1 and result[1] < beta:
                        position = (i, j)
                        beta = result[1]

                    # resetting the available space
                    board[i][j] = 0

                    if alpha >= beta:
                        return position, alpha, beta

        return position, alpha, beta

    # if the board is in an end state put the score from the end state of the board: 10 for win, 0 for tie, -10 for loss
    else:
        if turn == 1 and state[1] > alpha:
            alpha = state[1]
        elif turn == -1 and state[1] < beta:
            beta = state[1]
        return position, alpha, beta
