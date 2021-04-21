import pygame
import logic as lgc
from buttons import PlayButton, AIsettingsButton, QuitButton


pygame.init()

# screen size
width = 1360
height = 800

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

# set FPS
clock = pygame.time.Clock()
FPS = 60

# window settings
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('TicTacToe')
pygame.display.set_icon(pygame.image.load('icon.bmp'))


play_btn = PlayButton(window)
ai_set_btn = AIsettingsButton(window)
quit_btn = QuitButton(window)

lgc.menu_screen(play_btn, ai_set_btn, quit_btn, window)