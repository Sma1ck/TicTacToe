import pygame

BLACK = [0, 0, 0]

class Figure:
    def __init__(self, window):
        self.window = window
        self.x_figure = 1

    def draw_x(self, cell):
        pygame.draw.line(self.window, BLACK, (cell[0], cell[1]), (cell[0] + cell[2], cell[1] + cell[3]), 4)
        pygame.draw.line(self.window, BLACK, (cell[0] + cell[2], cell[1]), (cell[0], cell[1] + cell[3]), 4)

    def draw_o(self, cell):
        pygame.draw.circle(self.window, BLACK, cell.center, 100, 4)

    def switch_figure(self):
        if self.x_figure == 1:
            self.x_figure = 2
        else:
            self.x_figure = 1
