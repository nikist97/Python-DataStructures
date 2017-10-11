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

import sys

try:
    import pygame
except ImportError:
    print("You need to install pygame in order to run the applications. Use 'pip install pygame'.")
    sys.exit("Pygame is not installed")

import os
from os.path import dirname
root_path = dirname(dirname(os.path.abspath(__file__)))
if root_path not in sys.path:
    sys.path.append(root_path)

from Algorithms.nPuzzle import n_puzzle


# the Board class represents n-puzzle board
class Board(object):

    # constructor for the board
    def __init__(self, square_width, grids_num, color, number_color):
        self.color = color
        self.number_color = number_color
        self.grids_num = int(grids_num)

        # the board used for n-puzzle algorithm
        self.board = []
        for i in range(self.grids_num):
            to_add = []
            for j in range(self.grids_num):
                to_add.append(0)
            self.board.append(to_add)

        # square width must be positive
        if square_width > 0:
            self.square_width = square_width
        else:
            raise ValueError("Square width must be positive")

        self.font = pygame.font.SysFont("monospace", 45)

    # the update method updates the board relative to the current state
    def update_board(self, state):
        self.board = [list(state[i:i+self.grids_num]) for i in range(0, self.grids_num**2, self.grids_num)]

    # the draw method draws the n-puzzle board
    def draw(self, screen):
        for i in range(self.grids_num):
            for j in range(self.grids_num):
                pygame.draw.rect(screen, self.color,
                                 pygame.Rect((0 + j * self.square_width, 0 + i * self.square_width,
                                              self.square_width, self.square_width)), 1)
                if self.board[i][j] != 0:
                    label = self.font.render(str(self.board[i][j]), 1, self.number_color)
                    rect = label.get_rect()
                    screen.blit(label, (j*self.square_width + int(self.square_width/2) - int(rect.width/2),
                                        i*self.square_width + int(self.square_width/2) - int(rect.height/2)))


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
size = (540, 540)


def main(initial):
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('N-Puzzle')

    n = len(initial)
    grid_width = n**0.5
    generator = iter(n_puzzle(initial))
    running = True
    clock = pygame.time.Clock()
    board = Board(int(size[0] / grid_width), grid_width, black, red)

    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        try:
            path = next(generator)
            board.update_board(path)
            pygame.time.delay(750)
        except StopIteration:
            pass

        board.draw(screen)

        pygame.display.flip()
        clock.tick()

    pygame.quit()


# the algorithm uses a manhattan distance as a heuristic function, however, this could be slow for n > 8
# a possible optimization for bigger grids will be to use a pattern database lookup heuristic
if __name__ == "__main__":
    # 3x3 grid example
    initial_state = (4, 0, 2, 7, 6, 1, 8, 5, 3)

    # 4x4 grid example
    # initial_state = (2, 3, 6, 4, 1, 5, 11, 7, 13, 9, 8, 0, 14, 15, 10, 12)

    # 5x5 grid example
    # initial_state = (0, 2, 3, 4, 5, 1, 6, 8, 9, 10, 11, 7, 12, 14, 15, 16, 17, 13, 18, 20, 21, 22, 23, 19, 24)

    main(initial_state)
