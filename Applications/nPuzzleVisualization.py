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

import pygame
import sys

import os
from os.path import dirname
root_path = dirname(dirname(os.path.abspath(__file__)))
if root_path not in sys.path:
    sys.path.append(root_path)

from Algorithms.nPuzzle import n_puzzle


# the Board class represents n-puzzle board
class Board(object):

    # constructor for the board
    def __init__(self, square_width, color, number_color):
        self.color = color
        self.number_color = number_color
        self.grids_num = 3

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
        self.board = [list(state[0:3]), list(state[3:6]), list(state[6:9])]

    # the draw method draws the n-puzzle board
    def draw(self, screen):
        for i in range(self.grids_num):
            for j in range(self.grids_num):
                pygame.draw.rect(screen, self.color,
                                 pygame.Rect((0 + j * self.square_width, 0 + i * self.square_width,
                                              self.square_width, self.square_width)), 1)
                if self.board[i][j] != 0:
                    label = self.font.render(str(self.board[i][j]), 1, self.number_color)
                    screen.blit(label, (j*self.square_width + int(self.square_width/2), i*self.square_width +
                                        int(self.square_width/2)))


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
size = (540, 540)


def main(initial):
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('N-Puzzle')

    import time
    print("start")
    start = time.time()
    generator = iter(n_puzzle(initial))
    print(time.time() - start)
    running = True
    clock = pygame.time.Clock()
    board = Board(int(size[0] / 3), black, red)

    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        try:
            path = next(generator)
            board.update_board(path)
        except StopIteration:
            pass

        board.draw(screen)
        pygame.time.delay(750)

        pygame.display.flip()
        clock.tick()

    pygame.quit()


if __name__ == "__main__":
    initial_state = (4, 3, 2, 6, 1, 7, 8, 5, 0)
    main(initial_state)
