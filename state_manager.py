import sys
import pygame.mixer as mixer
from components import *
import dimen

app_name = 'Tic Tac Toe'
music_symbol = '♬'
text_play_on = 'Multiplayer Online'
text_play_off = 'Multiplayer Offline'
text_play_ai = 'Play against AI'
text_with_friends = 'Play online with friends'
back_symbol = '⮜'
text_cpy_msg = "© Aditya Nagyal, Raghav Gupta, Nikhil"

mixer.music.load('assets/button_click.mp3')
mixer.music.set_volume(1)


def button_callback(button: Button):
    mixer.music.play()
    if button.text == text_play_on:
        game_state.currentState = 'online'


def symbol_callback(text: Text):
    mixer.music.play()
    if text.text == back_symbol:
        game_state.currentState = 'main'


main_screen_components = [
    Text(music_symbol, dimen.size_symbol, colors.primary, dimen.music_pos, sys_font='segoeuisymbol', callback=symbol_callback),
    Image('assets/logo_big.png', dimen.logo_pos),
    Text(app_name, dimen.size_heading, colors.primary, dimen.title_pos, f='Righteous'),
    Button(text_play_ai, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.single_pl_btn_pos),
    Button(text_play_off, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.multi_pl_off_pos),
    Button(text_play_on, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.multi_pl_on_pos),
    Text(text_cpy_msg, dimen.size_copy_msg, colors.black, dimen.cpy_pos)
]

online_connect_components = [
    TextButton(back_symbol, dimen.size_symbol, colors.primary, symbol_callback, dimen.back_pos),
    Text(music_symbol, dimen.size_symbol, colors.primary, dimen.music_pos, sys_font='segoeuisymbol'),
    Image('assets/logo_big.png', dimen.logo_pos),
    Text(text_with_friends, dimen.size_heading_small, colors.primary, dimen.title_pos, f='Righteous'),
]

online_connect_components_rect = [component.rect for component in online_connect_components]
main_screen_components_rect = [component.rect for component in main_screen_components]


class GameState:
    def __init__(self, window: pygame.Surface, state):
        self.currentState = state
        self.window = window

    def draw_main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            main_screen_components[3].click(event)
            main_screen_components[4].click(event)
            main_screen_components[5].click(event)

        for component, rect in zip(main_screen_components, main_screen_components_rect):
            self.window.blit(component.value, rect)

    def draw_multiplayer_online(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            online_connect_components[0].click(event)

        for component, rect in zip(online_connect_components, online_connect_components_rect):
            self.window.blit(component.value, rect)

    def handle_current_state(self):
        if self.currentState == 'main':
            self.draw_main()
        elif self.currentState == 'online':
            self.draw_multiplayer_online()


window = pygame.display.set_mode(dimen.window_size)
game_state = GameState(window, 'main')
