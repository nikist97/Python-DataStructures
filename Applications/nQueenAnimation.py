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

from Algorithms.nQueen import n_queen_generator


# the Board class represents n-queen board
class Board(object):

    # constructor for the board
    def __init__(self, grids, square_width, color, queen_color):
        self.color = color
        self.queen_color = queen_color
        self.grids_num = grids

        # the board used for n-queen algorithm
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

    def update_board(self, path):
        self.board = []
        for i in range(self.grids_num):
            to_add = []
            for j in range(self.grids_num):
                try:
                    if j != path[i]:
                        to_add.append(0)
                    else:
                        to_add.append(1)
                except IndexError:
                    to_add.append(0)

            self.board.append(to_add)

    # the draw method draws the n-queen board
    def draw(self, screen):
        for i in range(self.grids_num):
            for j in range(self.grids_num):
                pygame.draw.rect(screen, self.color,
                                 pygame.Rect((0 + j * self.square_width, 0 + i * self.square_width,
                                              self.square_width, self.square_width)), 1)
                if self.board[j][i]:
                    pygame.draw.circle(screen, self.queen_color, (i * self.square_width + int(self.square_width / 2),
                                                                  j * self.square_width + int(self.square_width / 2)),
                                       int(self.square_width / 4), 0)


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
size = (540, 540)


def main(n):
    generator = n_queen_generator(n)

    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('N-Queen')

    running = True
    clock = pygame.time.Clock()
    board = Board(n, int(size[0] / n), black, red)

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
        pygame.time.delay(400)

        pygame.display.flip()
        clock.tick()

    pygame.quit()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        queens = int(sys.argv[1])
        if queens >= 4:
            main(queens)
        else:
            main(4)
    else:
        main(4)
