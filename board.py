import pygame

WHITE = [255, 255, 255]


class Board:
    def __init__(self, window):
        self.window = window
        self.cell_00 = pygame.Rect(680, 100, 198.5, 198.5)
        self.cell_01 = pygame.Rect(883, 100, 195.5, 198.5)
        self.cell_02 = pygame.Rect(1083, 100, 198.5, 198.5)
        self.cell_10 = pygame.Rect(680, 302.5, 198.5, 196.5)
        self.cell_11 = pygame.Rect(883, 302.5, 195.5, 196.5)
        self.cell_12 = pygame.Rect(1083, 302.5, 198.5, 196.5)
        self.cell_20 = pygame.Rect(680, 502.5, 198.5, 198.5)
        self.cell_21 = pygame.Rect(883, 502.5, 195.5, 198.5)
        self.cell_22 = pygame.Rect(1083, 502.5, 198.5, 198.5)

    def draw_board(self):
        pygame.draw.rect(self.window, WHITE, self.cell_00)
        pygame.draw.rect(self.window, WHITE, self.cell_01)
        pygame.draw.rect(self.window, WHITE, self.cell_02)
        pygame.draw.rect(self.window, WHITE, self.cell_10)
        pygame.draw.rect(self.window, WHITE, self.cell_11)
        pygame.draw.rect(self.window, WHITE, self.cell_12)
        pygame.draw.rect(self.window, WHITE, self.cell_20)
        pygame.draw.rect(self.window, WHITE, self.cell_21)
        pygame.draw.rect(self.window, WHITE, self.cell_22)

    def stop_board(self):
        self.cell_00 = pygame.Rect(0, 0, 0, 0)
        self.cell_01 = pygame.Rect(0, 0, 0, 0)
        self.cell_02 = pygame.Rect(0, 0, 0, 0)
        self.cell_10 = pygame.Rect(0, 0, 0, 0)
        self.cell_11 = pygame.Rect(0, 0, 0, 0)
        self.cell_12 = pygame.Rect(0, 0, 0, 0)
        self.cell_20 = pygame.Rect(0, 0, 0, 0)
        self.cell_21 = pygame.Rect(0, 0, 0, 0)
        self.cell_22 = pygame.Rect(0, 0, 0, 0)