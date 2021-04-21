import pygame

BLACK = [0, 0, 0]


class Xwin:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 100)
        self.btn_text = self.font.render('X win', 1, BLACK)
        self.btn_text_rect = self.btn_text.get_rect(center=(340, 300))

    def draw_xwin(self):
        self.window.blit(self.btn_text, self.btn_text_rect)


class Owin:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 100)
        self.btn_text = self.font.render('O win', 1, BLACK)
        self.btn_text_rect = self.btn_text.get_rect(center=(340, 300))

    def draw_owin(self):
        self.window.blit(self.btn_text, self.btn_text_rect)


class Draw:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 100)
        self.btn_text = self.font.render('Draw', 1, BLACK)
        self.btn_text_rect = self.btn_text.get_rect(center=(340, 300))

    def draw_draw(self):
        self.window.blit(self.btn_text, self.btn_text_rect)