import pygame

BLACK = [0, 0, 0]


class PlayButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('Play', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (340, 200)
        self.play_btn_rect = self.btn_text.get_rect()
        self.play_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.play_btn_rect)


class AIsettingsButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('AI settings', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 200, 50)
        self.rect.center = (340, 400)
        self.AI_settings_btn_rect = self.btn_text.get_rect()
        self.AI_settings_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.AI_settings_btn_rect)


class QuitButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('Quit', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (340, 600)
        self.quit_btn_rect = self.btn_text.get_rect()
        self.quit_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.quit_btn_rect)

class Ellipse:
    def __init__(self, window):
        self.window = window
        self.ellipse = pygame.Rect(340, 200, 100, 50)

    def draw_ellipse(self, window):
        pygame.draw.ellipse(window, [255, 0, 0], self.ellipse)

class EasyButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('Easy', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (340, 200)
        self.easy_btn_rect = self.btn_text.get_rect()
        self.easy_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.easy_btn_rect)


class MediumButton:
    def __init__(self, window):
        self.window = window
        self.window_rect = window.get_rect()
        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('Medium', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (340, 300)
        self.medium_btn_rect = self.btn_text.get_rect()
        self.medium_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.medium_btn_rect)


class HardButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('Hard', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (340, 400)
        self.hard_btn_rect = self.btn_text.get_rect()
        self.hard_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.hard_btn_rect)

class XButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('X', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = (280, 700)
        self.x_btn_rect = self.btn_text.get_rect()
        self.x_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.x_btn_rect)


class OButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('O', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = (400, 700)
        self.o_btn_rect = self.btn_text.get_rect()
        self.o_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.o_btn_rect)


class BackButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('Back', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (100, 750)
        self.back_btn_rect = self.btn_text.get_rect()
        self.back_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.back_btn_rect)


class StartButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('Start', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (340, 200)
        self.start_btn_rect = self.btn_text.get_rect()
        self.start_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.start_btn_rect)


class VSAIButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('VS AI', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (340, 400)
        self.vs_ai_btn_rect = self.btn_text.get_rect()
        self.vs_ai_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.vs_ai_btn_rect)


class VSPlayerButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('VS Player', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (340, 600)
        self.vs_player_btn_rect = self.btn_text.get_rect()
        self.vs_player_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.vs_player_btn_rect)


class ResetButton:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont('arial', 50)
        self.btn_text = self.font.render('Reset', 1, BLACK)

        self.rect = pygame.Rect(0, 0, 100, 50)
        self.rect.center = (340, 600)
        self.reset_btn_rect = self.btn_text.get_rect()
        self.reset_btn_rect.center = self.rect.center

    def draw_btn(self):
        self.window.blit(self.btn_text, self.reset_btn_rect)