import sys

import pygame.event
import pygame.mixer as mixer

from components import *
from string_vars import *
import dimen

mixer.music.load('assets/button_click.mp3')
mixer.music.set_volume(0.5)

player = 2
chosen_w = None


def board_callback(board: Board, box: int):
    global player
    if player is None:
        return
    board.check(box, player)
    if player == 1:
        player = 2
    else:
        player = 1


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


def symbol_callback(text: Text):
    mixer.music.play()
    if text.text == back_symbol:
        single_player_components[1].clean()
        global chosen_w, player
        player = 2
        chosen_w = None
        single_player_selection_screen[2].unselect()
        single_player_selection_screen[3].unselect()
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

single_player_selection_screen = [
    TextButton(back_symbol, dimen.size_symbol, colors.primary, symbol_callback, dimen.back_pos),
    Text(text_choose_weapon, dimen.size_heading_small, colors.primary, dimen.choose_pos, f='Righteous'),
    Circle(dimen.cw_size, dimen.cw_center, dimen.cw_radius, dimen.cw_width, dimen.cw_pos, select_circle),
    Cross(dimen.cw_size, select_cross, dimen.cw_c_pos),
    Button(text_start, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.start_pos),
    Text(text_play_ai, dimen.size_heading_small, colors.primary, dimen.play_ai_pos, f='Righteous')
]

online_connect_components_rect = [component.rect for component in online_connect_components]
main_screen_components_rect = [component.rect for component in main_screen_components]
single_player_components_rect = [component.rect for component in single_player_components]
single_player_selection_screen_rect = [component.rect for component in single_player_selection_screen]


class GameState:
    def __init__(self, win: pygame.Surface, state):
        self.currentState = state
        self.window = win

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

    def handle_current_state(self):
        if self.currentState == 'main':
            self.draw_main()
        elif self.currentState == 'online':
            self.draw_multiplayer_online()
        elif self.currentState == 'single':
            self.draw_single_screen()
        elif self.currentState == 'single_r':
            self.draw_single_r_screen()


window = pygame.display.set_mode(dimen.window_size)
game_state = GameState(window, 'main')
