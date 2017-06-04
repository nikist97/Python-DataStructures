import pygame
from Algorithms.minimax import minimax, end_state


# the Board class represents the tic-tac-toe board
class Board(object):

    def __init__(self, square_width, color, player_1, player_2, message_colour=(0, 0, 0)):
        self.color = color
        self.message_colour = message_colour
        self.end_state = False, 0

        # the board used for minimax algorithm
        self.minimax_board = []
        for i in range(3):
            self.minimax_board.append([0, 0, 0])

        if player_1.player_type != player_2.player_type:
            self.players = (player_1, player_2)
        else:
            raise ValueError("The two players must be with different types - cross or circle.")

        # square width must be positive
        if square_width > 0:
            self.square_width = square_width
        else:
            raise ValueError("Square width must be positive")

    def clear(self, change_turns=False):
        self.end_state = False, 0

        self.minimax_board = []
        for i in range(3):
            self.minimax_board.append([0, 0, 0])

        self.players[0].clear()
        self.players[1].clear()

        if change_turns:
            self.players[1].add_position(0, 1, self.minimax_board, 1)

    # process_input takes the events that happened as an argument and processes them
    def process_input(self, events):
        if not self.end_state[0]:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_position = pygame.mouse.get_pos()
                        x = int(mouse_position[0] / self.square_width)
                        y = int(mouse_position[1] / self.square_width)
                        if (x, y) not in self.players[1].positions:
                            if self.players[0].add_position(x, y, self.minimax_board):
                                computer_position = minimax(self.minimax_board)
                                if not end_state(self.minimax_board)[0]:
                                    self.players[1].add_position(computer_position[1][0], computer_position[1][1],
                                                                 self.minimax_board, 1)
        else:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.clear()
                    elif event.key == pygame.K_SPACE:
                        self.clear(True)

    # the update method checks if the board is in an end state:
    def update(self):
        if not self.end_state[0]:
            self.end_state = end_state(self.minimax_board)

    # the draw method draws the tic-tac-toe board and the players shapes on their respective positions
    def draw(self, screen):
        if not self.end_state[0]:
            for i in range(3):
                for j in range(3):
                    pygame.draw.rect(screen, self.color,
                                     pygame.Rect((0 + j*self.square_width, 0 + i*self.square_width,
                                                  self.square_width, self.square_width)), 1)

            self.players[0].draw(screen)
            self.players[1].draw(screen)

        else:
            font = pygame.font.Font(None, 50)
            text = font.render("Game ended", True, self.message_colour)
            screen.blit(text,
                        (int(screen.get_width()/2 - text.get_width()/2),
                         int(screen.get_height()/2 - text.get_height()/2) - 30))
            if self.end_state[1] > 0:
                new_text = font.render("You lost", True, self.message_colour)
            elif self.end_state[1] == 0:
                new_text = font.render("It's a tie", True, self.message_colour)
            else:
                new_text = font.render("You won", True, self.message_colour)

            screen.blit(new_text,
                        (int(screen.get_width() / 2 - new_text.get_width() / 2),
                         int(screen.get_height() / 2 - new_text.get_height() / 2) + 20))


# Player class represents a player on the board
class Player(object):

    # a player has a x,y coordinates and a type
    def __init__(self, player_type, square_width, color):
        self.color = color
        self.positions = []

        # player_type is either a circle or a cross
        if player_type == "circle" or player_type == "cross":
            self.player_type = player_type
        else:
            raise ValueError("Sign must be a circle or cross.")

        # square width must be positive
        if square_width > 0:
            self.square_width = square_width
        else:
            raise ValueError("Square width must be positive")

    # a method to add a position to the player
    def add_position(self, x, y, minimax_board=None, turn=-1):
        # x belongs to [0 to 3)
        if not 0 <= x < 3:
            raise ValueError("x coordinate must be from 0 to 3.")

        # y belongs to [0 to 3)
        if not 0 <= y < 3:
            raise ValueError("y coordinate must be from 0 to 3.")

        # the position cannot already be added
        if (x, y) not in self.positions:
            self.positions.append((x, y))
            if minimax_board is not None:
                minimax_board[x][y] = turn
            return True
        else:
            return False

    def clear(self):
        self.positions = []

    # the draw method draws all the positions of the player on the board
    def draw(self, screen):
        for position in self.positions:
            player_x = position[0]*self.square_width
            player_y = position[1]*self.square_width

            # draw a circle shape
            if self.player_type == "circle":
                pygame.draw.circle(screen, self.color,
                                   (player_x + int(self.square_width/2), player_y + int(self.square_width/2)),
                                   int(self.square_width/4), 2)

            # draw a cross shape
            elif self.player_type == "cross":
                delta = self.square_width/4
                pygame.draw.line(screen, self.color, (player_x + delta, player_y + delta),
                                 (player_x + self.square_width - delta, player_y + self.square_width - delta), 2)
                pygame.draw.line(screen, self.color, (player_x + self.square_width - delta, player_y + delta),
                                 (player_x + delta, player_y + self.square_width - delta), 2)


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
size = (540, 540)


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Tic-Tac-Toe')

    running = True
    clock = pygame.time.Clock()
    player_1 = Player("circle", int(size[0]/3), red)
    player_2 = Player("cross", int(size[0]/3), blue)
    board = Board(size[0]/3, black, player_1, player_2, message_colour=green)

    while running:
        screen.fill(white)

        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                filtered_events.append(event)

            elif event.type == pygame.KEYDOWN:
                filtered_events.append(event)

        board.process_input(filtered_events)
        board.update()
        board.draw(screen)

        pygame.display.flip()
        clock.tick()

    pygame.quit()

if __name__ == "__main__":
    main()
