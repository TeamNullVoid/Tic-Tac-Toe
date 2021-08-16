import sys

from components import *
import dimen

app_name = 'Tic Tac Toe'
music_symbol = '♬'
text_play_on = 'Multiplayer Online'
text_play_off = 'Multiplayer Offline'
text_play_ai = 'Play against AI'
text_cpy_msg = "© Aditya Nagyal, Raghav Gupta, Nikhil"


def button_callback(button: Button):
    print('clicked', button.text)


main_screen_components = [
    Text(music_symbol, dimen.size_symbol, colors.primary, dimen.music_pos, sys_font='segoeuisymbol'),
    Image('assets/logo_big.png', dimen.logo_pos),
    Text(app_name, dimen.size_text, colors.primary, dimen.title_pos, f='Righteous'),
    Button(text_play_ai, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.single_pl_btn_pos),
    Button(text_play_off, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.multi_pl_off_pos),
    Button(text_play_on, dimen.button_text_size, dimen.button_size, colors.white, colors.red, button_callback, dimen.multi_pl_on_pos),
    Text(text_cpy_msg, dimen.size_copy_msg, colors.black, dimen.cpy_pos)
]

main_screen_components_rect = [component.rect for component in main_screen_components]


class GameState:
    def __init__(self, window: pygame.Surface):
        self.currentState = 'main'
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

    def handle_current_state(self):
        if self.currentState == 'main':
            self.draw_main()
