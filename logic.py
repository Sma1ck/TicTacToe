import pygame
from buttons import EasyButton, MediumButton, HardButton, XButton, OButton, BackButton
from buttons import StartButton, VSAIButton, VSPlayerButton, ResetButton
from winnertext import Xwin, Owin, Draw
from board import Board
from figure import Figure
from settings import Settings


WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]

clock = pygame.time.Clock()
FPS = 60

ai = Settings()


def menu_screen(play_btn, ai_set_btn, quit_btn, window):
    while True:
        window.fill(WHITE)
        play_btn.draw_btn()
        ai_set_btn.draw_btn()
        quit_btn.draw_btn()
        pygame.draw.line(window, BLACK, (880, 100), (880, 700), 5)
        pygame.draw.line(window, BLACK, (1080, 100), (1080, 700), 5)
        pygame.draw.line(window, BLACK, (680, 300), (1280, 300), 5)
        pygame.draw.line(window, BLACK, (680, 500), (1280, 500), 5)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        quit_button_clicked = quit_btn.rect.collidepoint(mouse_x, mouse_y)
        ai_set_button_clicked = ai_set_btn.rect.collidepoint(mouse_x, mouse_y)
        play_btn_clicked = play_btn.rect.collidepoint(mouse_x, mouse_y)
        if play_btn_clicked and click:
            prepare_screen(window)
        if ai_set_button_clicked and click:
            settings_screen(window)
        if quit_button_clicked and click:
            exit()
        clock.tick(FPS)
        pygame.display.update()


def settings_screen(window):
    window.fill(WHITE)
    font = pygame.font.SysFont('arial', 50)
    dif_btn_text = font.render('Difficulty', True, 50)
    dif_btn_text_rect = dif_btn_text.get_rect(center=(340, 100))
    window.blit(dif_btn_text, dif_btn_text_rect)

    ai_plays_btn_text = font.render('AI plays', True, 50)
    ai_plays_btn_text_rect = ai_plays_btn_text.get_rect(center=(340, 600))
    window.blit(ai_plays_btn_text, ai_plays_btn_text_rect)

    easy_btn = EasyButton(window)
    medium_btn = MediumButton(window)
    hard_btn = HardButton(window)
    x_btn = XButton(window)
    o_btn = OButton(window)
    back_btn = BackButton(window)

    easy_btn.draw_btn()
    medium_btn.draw_btn()
    hard_btn.draw_btn()
    x_btn.draw_btn()
    o_btn.draw_btn()
    back_btn.draw_btn()


    pygame.draw.line(window, BLACK, (880, 100), (880, 700), 5)
    pygame.draw.line(window, BLACK, (1080, 100), (1080, 700), 5)
    pygame.draw.line(window, BLACK, (680, 300), (1280, 300), 5)
    pygame.draw.line(window, BLACK, (680, 500), (1280, 500), 5)

    # Default difficulty settings
    pygame.draw.ellipse(window, RED, (240, 150, 200, 100), 5)

    # Default AI figure settings
    pygame.draw.circle(window, RED, (400, 700), 50, 5)

    settings = True
    while settings:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        easy_btn_clicked = easy_btn.rect.collidepoint(mouse_x, mouse_y)
        medium_btn_clicked = medium_btn.rect.collidepoint(mouse_x, mouse_y)
        hard_btn_clicked = hard_btn.rect.collidepoint(mouse_x, mouse_y)
        x_btn_clicked = x_btn.rect.collidepoint(mouse_x, mouse_y)
        o_btn_clicked = o_btn.rect.collidepoint(mouse_x, mouse_y)
        back_btn_clicked = back_btn.rect.collidepoint(mouse_x, mouse_y)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if easy_btn_clicked and click:
            pygame.draw.ellipse(window, RED, (240, 150, 200, 100), 5)
            pygame.draw.ellipse(window, WHITE, (220, 250, 250, 100), 5)
            pygame.draw.ellipse(window, WHITE, (240, 350, 200, 100), 5)
            ai.set_easy_difficulty()
            print('You picked easy mode')
        elif medium_btn_clicked and click:
            pygame.draw.ellipse(window, WHITE, (240, 150, 200, 100), 5)
            pygame.draw.ellipse(window, RED, (220, 250, 250, 100), 5)
            pygame.draw.ellipse(window, WHITE, (240, 350, 200, 100), 5)
            ai.set_medium_difficulty()
            print('You picked medium mode')
        elif hard_btn_clicked and click:
            pygame.draw.ellipse(window, WHITE, (240, 150, 200, 100), 5)
            pygame.draw.ellipse(window, WHITE, (220, 250, 250, 100), 5)
            pygame.draw.ellipse(window, RED, (240, 350, 200, 100), 5)
            ai.set_hard_difficulty()
            print('You picked hard mode')
        elif back_btn_clicked and click:
            settings = False
        elif x_btn_clicked and click:
            pygame.draw.circle(window, RED, (280, 700), 50, 5)
            pygame.draw.circle(window, WHITE, (400, 700), 50, 5)
            ai.switch_the_turn()
            print('Now AI plays with X')
        elif o_btn_clicked and click:
            pygame.draw.circle(window, RED, (400, 700), 50, 5)
            pygame.draw.circle(window, WHITE, (280, 700), 50, 5)
            ai.switch_the_turn()
            print('Now AI plays with O')
        pygame.display.update()
        clock.tick(FPS)

def prepare_screen(window):
    window.fill(WHITE)

    start_btn = StartButton(window)
    vs_ai_btn = VSAIButton(window)
    vs_player_btn = VSPlayerButton(window)
    back_btn = BackButton(window)

    start_btn.draw_btn()
    vs_ai_btn.draw_btn()
    vs_player_btn.draw_btn()
    back_btn.draw_btn()

    pygame.draw.line(window, BLACK, (880, 100), (880, 700), 5)
    pygame.draw.line(window, BLACK, (1080, 100), (1080, 700), 5)
    pygame.draw.line(window, BLACK, (680, 300), (1280, 300), 5)
    pygame.draw.line(window, BLACK, (680, 500), (1280, 500), 5)

    versus_ai = 0

    prepare = True
    while prepare:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        start_btn_clicked = start_btn.rect.collidepoint(mouse_x, mouse_y)
        vs_ai_btn_clicked = vs_ai_btn.rect.collidepoint(mouse_x, mouse_y)
        vs_player_btn_clicked = vs_player_btn.rect.collidepoint(mouse_x, mouse_y)
        back_btn_clicked = back_btn.rect.collidepoint(mouse_x, mouse_y)

        if start_btn_clicked and click:
            game_screen(window, versus_ai)
            prepare = False
        if vs_ai_btn_clicked and click:
            pygame.draw.circle(window, RED, (250, 400), 20)
            pygame.draw.circle(window, WHITE, (200, 600), 20)
            versus_ai = 1
            print('You will play versus AI')
        if vs_player_btn_clicked and click:
            pygame.draw.circle(window, RED, (200, 600), 20)
            pygame.draw.circle(window, WHITE, (250, 400), 20)
            print('You will play versus player')
        if back_btn_clicked and click:
            prepare = False

        clock.tick(FPS)
        pygame.display.update()


def game_screen(window, versus_ai):
    window.fill(WHITE)

    pygame.draw.line(window, BLACK, (880, 100), (880, 700), 5)
    pygame.draw.line(window, BLACK, (1080, 100), (1080, 700), 5)
    pygame.draw.line(window, BLACK, (680, 300), (1280, 300), 5)
    pygame.draw.line(window, BLACK, (680, 500), (1280, 500), 5)

    board = Board(window)
    board.draw_board()

    xwin = Xwin(window)
    owin = Owin(window)
    draw = Draw(window)

    reset_btn = ResetButton(window)

    figure = Figure(window)
    game = True

    board_list = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    while game:
        if versus_ai == 1:
            gameVS_AI(window, board, figure, board_list, reset_btn)
        else:
            gameVSplayer(window, board, figure, board_list, reset_btn)
        winner = check_winner(board_list)
        if winner == 'X wins':
            xwin.draw_xwin()
            reset_btn.draw_btn()
            board.stop_board()
            ai.turn = 0
        if winner == 'O wins':
            owin.draw_owin()
            reset_btn.draw_btn()
            board.stop_board()
            ai.turn = 0
        if winner == 'Draw':
            draw.draw_draw()
            reset_btn.draw_btn()
            board.stop_board()
            ai.turn = 0


def gameVSplayer(window, board, figure, board_list, reset_btn):
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.button == 1:
                click = True

        # catch a mouse correlation
            cell_00_clicked = board.cell_00.collidepoint(mouse_x, mouse_y)
            cell_01_clicked = board.cell_01.collidepoint(mouse_x, mouse_y)
            cell_02_clicked = board.cell_02.collidepoint(mouse_x, mouse_y)
            cell_10_clicked = board.cell_10.collidepoint(mouse_x, mouse_y)
            cell_11_clicked = board.cell_11.collidepoint(mouse_x, mouse_y)
            cell_12_clicked = board.cell_12.collidepoint(mouse_x, mouse_y)
            cell_20_clicked = board.cell_20.collidepoint(mouse_x, mouse_y)
            cell_21_clicked = board.cell_21.collidepoint(mouse_x, mouse_y)
            cell_22_clicked = board.cell_22.collidepoint(mouse_x, mouse_y)
            reset_btn_clicked = reset_btn.rect.collidepoint(mouse_x, mouse_y)

            # draw a figure when click on cell
            if cell_00_clicked and click and board_list[0][0] == 0:
                if figure.x_figure == 1:
                    figure.draw_x(board.cell_00)
                else:
                    figure.draw_o(board.cell_00)
                board_list[0][0] = figure.x_figure
                figure.switch_figure()
            elif cell_01_clicked and click and board_list[0][1] == 0:
                if figure.x_figure == 1:
                    figure.draw_x(board.cell_01)
                else:
                    figure.draw_o(board.cell_01)
                board_list[0][1] = figure.x_figure
                figure.switch_figure()
            elif cell_02_clicked and click and board_list[0][2] == 0:
                if figure.x_figure == 1:
                    figure.draw_x(board.cell_02)
                else:
                    figure.draw_o(board.cell_02)
                board_list[0][2] = figure.x_figure
                figure.switch_figure()
            elif cell_10_clicked and click and board_list[1][0] == 0:
                if figure.x_figure == 1:
                    figure.draw_x(board.cell_10)
                else:
                    figure.draw_o(board.cell_10)
                board_list[1][0] = figure.x_figure
                figure.switch_figure()
            elif cell_11_clicked and click and board_list[1][1] == 0:
                if figure.x_figure == 1:
                    figure.draw_x(board.cell_11)
                else:
                    figure.draw_o(board.cell_11)
                board_list[1][1] = figure.x_figure
                figure.switch_figure()
            elif cell_12_clicked and click and board_list[1][2] == 0:
                if figure.x_figure == 1:
                    figure.draw_x(board.cell_12)
                else:
                    figure.draw_o(board.cell_12)
                board_list[1][2] = figure.x_figure
                figure.switch_figure()
            elif cell_20_clicked and click and board_list[2][0] == 0:
                if figure.x_figure == 1:
                    figure.draw_x(board.cell_20)
                else:
                    figure.draw_o(board.cell_20)
                board_list[2][0] = figure.x_figure
                figure.switch_figure()
            elif cell_21_clicked and click and board_list[2][1] == 0:
                if figure.x_figure == 1:
                    figure.draw_x(board.cell_21)
                else:
                    figure.draw_o(board.cell_21)
                board_list[2][1] = figure.x_figure
                figure.switch_figure()
            elif cell_22_clicked and click and board_list[2][2] == 0:
                if figure.x_figure == 1:
                    figure.draw_x(board.cell_22)
                else:
                    figure.draw_o(board.cell_22)
                board_list[2][2] = figure.x_figure
                figure.switch_figure()
            elif reset_btn_clicked and click:
                game_screen(window, versus_ai=0)

    clock.tick(FPS)
    pygame.display.update()


def gameVS_AI(window, board, figure, board_list, reset_btn):
    click = False
    print(ai.turn)

    if ai.turn == 1:
        if ai.difficulty == 1:
            mouse_x, mouse_y = ai.easy_turn()
            click = True
        if ai.difficulty == 2:
            for i in range(1, 2):
                for j in range(1, 2):
                    if board_list[i][j] == board_list[i][j+1]:
                        board_list[i][0] = figure.x_figure
                        ai.switch_the_turn()
                        figure.switch_figure()
                    if board_list[i][j] == board_list[i][j-1]:
                        board_list[i][2] = figure.x_figure
                        ai.switch_the_turn()
                        figure.switch_figure()
                    if board_list[i][j] == board_list[i+1][j]:
                        board_list[0][j] = figure.x_figure
                        ai.switch_the_turn()
                        figure.switch_figure()
                    if board_list[i][j] == board_list[i-1][j]:
                        board_list[2][j] = figure.x_figure
                        ai.switch_the_turn()
                        figure.switch_figure()
            mouse_x, mouse_y = ai.easy_turn()
            click = True
        if ai.difficulty == 3:
            pass
    else:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


    # catch a mouse correlation
    cell_00_clicked = board.cell_00.collidepoint(mouse_x, mouse_y)
    cell_01_clicked = board.cell_01.collidepoint(mouse_x, mouse_y)
    cell_02_clicked = board.cell_02.collidepoint(mouse_x, mouse_y)
    cell_10_clicked = board.cell_10.collidepoint(mouse_x, mouse_y)
    cell_11_clicked = board.cell_11.collidepoint(mouse_x, mouse_y)
    cell_12_clicked = board.cell_12.collidepoint(mouse_x, mouse_y)
    cell_20_clicked = board.cell_20.collidepoint(mouse_x, mouse_y)
    cell_21_clicked = board.cell_21.collidepoint(mouse_x, mouse_y)
    cell_22_clicked = board.cell_22.collidepoint(mouse_x, mouse_y)
    reset_btn_clicked = reset_btn.rect.collidepoint(mouse_x, mouse_y)

    if cell_00_clicked and click and board_list[0][0] == 0:
        if figure.x_figure == 1:
            figure.draw_x(board.cell_00)
        else:
            figure.draw_o(board.cell_00)
        board_list[0][0] = figure.x_figure
        ai.switch_the_turn()
        figure.switch_figure()
    elif cell_01_clicked and click and board_list[0][1] == 0:
        if figure.x_figure == 1:
            figure.draw_x(board.cell_01)
        else:
            figure.draw_o(board.cell_01)
        board_list[0][1] = figure.x_figure
        ai.switch_the_turn()
        figure.switch_figure()
    elif cell_02_clicked and click and board_list[0][2] == 0:
        if figure.x_figure == 1:
            figure.draw_x(board.cell_02)
        else:
            figure.draw_o(board.cell_02)
        board_list[0][2] = figure.x_figure
        ai.switch_the_turn()
        figure.switch_figure()
    elif cell_10_clicked and click and board_list[1][0] == 0:
        if figure.x_figure == 1:
            figure.draw_x(board.cell_10)
        else:
            figure.draw_o(board.cell_10)
        board_list[1][0] = figure.x_figure
        ai.switch_the_turn()
        figure.switch_figure()
    elif cell_11_clicked and click and board_list[1][1] == 0:
        if figure.x_figure == 1:
            figure.draw_x(board.cell_11)
        else:
            figure.draw_o(board.cell_11)
        board_list[1][1] = figure.x_figure
        ai.switch_the_turn()
        figure.switch_figure()
    elif cell_12_clicked and click and board_list[1][2] == 0:
        if figure.x_figure == 1:
            figure.draw_x(board.cell_12)
        else:
            figure.draw_o(board.cell_12)
        board_list[1][2] = figure.x_figure
        ai.switch_the_turn()
        figure.switch_figure()
    elif cell_20_clicked and click and board_list[2][0] == 0:
        if figure.x_figure == 1:
            figure.draw_x(board.cell_20)
        else:
            figure.draw_o(board.cell_20)
        board_list[2][0] = figure.x_figure
        ai.switch_the_turn()
        figure.switch_figure()
    elif cell_21_clicked and click and board_list[2][1] == 0:
        if figure.x_figure == 1:
            figure.draw_x(board.cell_21)
        else:
            figure.draw_o(board.cell_21)
        board_list[2][1] = figure.x_figure
        ai.switch_the_turn()
        figure.switch_figure()
    elif cell_22_clicked and click and board_list[2][2] == 0:
        if figure.x_figure == 1:
            figure.draw_x(board.cell_22)
        else:
            figure.draw_o(board.cell_22)
        board_list[2][2] = figure.x_figure
        ai.switch_the_turn()
        figure.switch_figure()
    elif reset_btn_clicked and click:
        game_screen(window, versus_ai=1)

    clock.tick(FPS)
    pygame.display.update()


def check_winner(board_list):
    if board_list[0][0] == board_list[1][1] == board_list[2][2] != 0:
        if board_list[1][1] == 1:
            return 'X wins'
        else:
            return 'O wins'
    if board_list[0][2] == board_list[1][1] == board_list[2][0] != 0:
        if board_list[1][1] == 1:
            return 'X wins'
        else:
            return 'O wins'
    for i in range(3):
        if board_list[i].count(1) == 3:
            return 'X wins'
        if board_list[i].count(2) == 3:
            return 'O wins'
        col = [j[i] for j in board_list]
        if col.count(1) == 3:
            return 'X wins'
        if col.count(2) == 3:
            return 'O wins'
    if any([i.count(0) for i in board_list]):
        return False
    return 'Draw'



