import sys

import pygame.event
import pygame.mixer as mixer

import colors
import logic
from components import *
from string_vars import *
import dimen

mixer.music.load('assets/button_click.mp3')
mixer.music.set_volume(0.5)

player = 2
chosen_w = None
m_player = 2


def board_callback(board: Board, box: int):
    global player
    if player is None:
        return
    board.check(box, player)
    if player == 1:
        player = 2
    else:
        player = 1


def mp_board_callback(board: Board, box: int):
    global m_player
    if m_player is None:
        return
    done = board.check(box, m_player)
    if done:
        if m_player == 1:
            m_player = 2
        else:
            m_player = 1

        won = logic.check_who_won(board.checked)
        print(won)
        if won[0]:
            end_mp_components[0].update(text_x_win if won[1] == 2 else text_o_win, colors.cross if won[1] == 2 else colors.circle)
            game_state.currentState = 'end_m'
        else:
            tie = logic.check_draw(board.checked)
            if tie:
                end_mp_components[0].update(text_draw, colors.black)
                game_state.currentState = 'end_m'
            else:
                multiplayer_components[2].update(text_x_turn if m_player == 2 else text_o_turn, colors.cross if m_player == 2 else colors.circle)


def button_callback(button: Button):
    mixer.music.play()
    print("button clicked")
    if button.text == text_play_on:
        print("Play online clicked")
        game_state.currentState = 'online'
    elif button.text == text_play_ai:
        print("Play against ai clicked")
        game_state.currentState = 'single'
    elif button.text == text_start:
        print("Start button clicked, Single player")
        if chosen_w == 1 or chosen_w == 2:
            game_state.currentState = 'single_r'
    elif button.text == text_play_off:
        print("Play Offline")
        game_state.currentState = 'offline'
    elif button.text == text_main_menu:
        clean()
        game_state.currentState = 'main'
    elif button.text == text_play_again:
        clean()
        game_state.currentState = 'offline'


def select_cross(cross: Cross):
    print("Cross Selected")
    mixer.music.play()
    single_player_selection_screen[2].unselect()
    cross.select()
    global chosen_w
    chosen_w = 2
    pass


def select_circle(circle: Circle):
    print("Circle Selected")
    mixer.music.play()
    single_player_selection_screen[3].unselect()
    circle.select()
    global chosen_w
    chosen_w = 1
    pass


def clean():
    single_player_components[1].clean()
    multiplayer_components[1].clean()
    global chosen_w, player, m_player
    player = 2
    m_player = 2
    chosen_w = None
    multiplayer_components[2].update(text_x_turn if m_player == 2 else text_o_turn, colors.cross if m_player == 2 else colors.circle)
    single_player_selection_screen[2].unselect()
    single_player_selection_screen[3].unselect()


def symbol_callback(text: Text):
    mixer.music.play()
    if text.text == back_symbol:
        clean()
        game_state.currentState = 'main'


def input_callback(_: InputField):
    mixer.music.play()
    print("called", _.text)
    pass


main_screen_components = [
    Image('assets/logo_big.png', dimen.logo_pos),
    Text(app_name, dimen.size_heading, colors.primary, dimen.title_pos, f='Righteous'),
    Button(text_play_ai, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.single_pl_btn_pos),
    Button(text_play_off, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.multi_pl_off_pos),
    Button(text_play_on, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.multi_pl_on_pos),
    Text(text_cpy_msg, dimen.size_copy_msg, colors.black, dimen.cpy_pos)
]

online_connect_components = [
    TextButton(back_symbol, dimen.size_symbol, colors.primary, symbol_callback, dimen.back_pos),
    Image('assets/logo_big.png', dimen.logo_pos),
    Text(text_with_friends, dimen.size_heading_small, colors.primary, dimen.title_pos, f='Righteous'),
    InputField(hint_code, dimen.input_size, dimen.code_input_pos),
    Button(text_join, dimen.button_text_size, dimen.button_small, colors.white, colors.red, button_callback, dimen.join_button_pos),
    Text(text_or, dimen.size_text_normal, colors.black, dimen.or_pos),
    Button(text_create, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.create_btn_pos)
]

single_player_components = [
    TextButton(back_symbol, dimen.size_symbol, colors.primary, symbol_callback, dimen.back_pos),
    Board(dimen.board_size, dimen.board_pos, dimen.board_mat, board_callback)
]

multiplayer_components = [
    TextButton(back_symbol, dimen.size_symbol, colors.primary, symbol_callback, dimen.back_pos),
    Board(dimen.board_size, dimen.board_pos, dimen.board_mat, mp_board_callback),
    Text(text_x_turn, dimen.size_heading_small, colors.cross, dimen.turn_pos, f='Righteous')
]

single_player_selection_screen = [
    TextButton(back_symbol, dimen.size_symbol, colors.primary, symbol_callback, dimen.back_pos),
    Text(text_choose_weapon, dimen.size_heading_small, colors.primary, dimen.choose_pos, f='Righteous'),
    Circle(dimen.cw_size, dimen.cw_center, dimen.cw_radius, dimen.cw_width, dimen.cw_pos, select_circle),
    Cross(dimen.cw_size, select_cross, dimen.cw_c_pos),
    Button(text_start, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.start_pos),
    Text(text_play_ai, dimen.size_heading_small, colors.primary, dimen.play_ai_pos, f='Righteous')
]

start_new_game_screen = [
    TextButton(back_symbol, dimen.size_symbol, colors.primary, symbol_callback, dimen.back_pos),
    Image('assets/hooray.png', dimen.hooray_pos),
    Text("You Won!", dimen.size_heading_small, colors.primary, dimen.choose_pos, f='Righteous'),
    Button(text_new_game, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.start_pos),
]

end_mp_components = [
    Text(text_x_win, dimen.size_heading, colors.cross, dimen.center, f='Righteous'),
    Button(text_play_again, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.again_pos),
    Button(text_main_menu, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.menu_pos),
    Image('assets/hooray.png', dimen.hooray_pos_m)
]

end_mp_components_rect = [component.rect for component in end_mp_components]
online_connect_components_rect = [component.rect for component in online_connect_components]
main_screen_components_rect = [component.rect for component in main_screen_components]
single_player_components_rect = [component.rect for component in single_player_components]
start_new_game_screen_rect = [component.rect for component in start_new_game_screen]
single_player_selection_screen_rect = [component.rect for component in single_player_selection_screen]
multiplayer_components_rect = [component.rect for component in multiplayer_components]


class GameState:
    def __init__(self, win: pygame.Surface, state):
        self.currentState = state
        self.window = win

    def draw_end_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        for component, rect in zip(start_new_game_screen, start_new_game_screen_rect):
            self.window.blit(component.value, rect)

    def draw_main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            main_screen_components[3].click(event)
            main_screen_components[4].click(event)
            main_screen_components[2].click(event)

        for component, rect in zip(main_screen_components, main_screen_components_rect):
            self.window.blit(component.value, rect)

    def draw_multiplayer_online(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            online_connect_components[0].click(event)
            online_connect_components[3].handle_event(event)

        for component, rect in zip(online_connect_components, online_connect_components_rect):
            self.window.blit(component.value, rect)

    def draw_end_mp(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

            end_mp_components[1].click(e)
            end_mp_components[2].click(e)

        for component, rect in zip(end_mp_components, end_mp_components_rect):
            self.window.blit(component.value, rect)
        pass

    def draw_single_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            single_player_selection_screen[0].click(event)
            single_player_selection_screen[2].handle_click(event)
            single_player_selection_screen[3].handle_click(event)
            single_player_selection_screen[4].click(event)

        for component, rect in zip(single_player_selection_screen, single_player_selection_screen_rect):
            self.window.blit(component.value, rect)

    def draw_single_r_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            single_player_components[0].click(event)
            single_player_components[1].handle_event(event)

        for component, rect in zip(single_player_components, single_player_components_rect):
            self.window.blit(component.value, rect)

    def draw_multiplayer_offline(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            multiplayer_components[0].click(event)
            multiplayer_components[1].handle_event(event)

        for component, rect in zip(multiplayer_components, multiplayer_components_rect):
            self.window.blit(component.value, rect)

    def handle_current_state(self):
        if self.currentState == 'main':
            self.draw_main()
        elif self.currentState == 'online':
            self.draw_multiplayer_online()
        elif self.currentState == 'single':
            self.draw_single_screen()
        elif self.currentState == 'single_r':
            self.draw_single_r_screen()
        elif self.currentState == 'offline':
            self.draw_multiplayer_offline()
        elif self.currentState == 'end':
            self.draw_end_screen()
        elif self.currentState == 'end_m':
            self.draw_end_mp()


window = pygame.display.set_mode(dimen.window_size)
game_state = GameState(window, 'main')
