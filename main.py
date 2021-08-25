import pygame
import colors
import state_manager

pygame.init()

pygame.display.set_caption(state_manager.app_name)
print(
    """
    Welcome to Tic-Tac-Toe
    
    Modes - Single Player, Multiplayer, Online
    Have Fun and Enjoy!!,
    
    UI Components are designed and extended on pygame library and
    all these components are subject to copyright.
    
    The font is available open-source on Google Fonts(https://fonts.google.com).
    Ubuntu Regular - https://fonts.google.com/specimen/Ubuntu?query=ubuntu
    Righteous Regular - https://fonts.google.com/specimen/Righteous?query=right
    
    The backend used for online multiplayer is Firebase by Google and the
    server project is subject to copyright for all developers.
    
    Developed By - Nikhil, Aditya, Raghav
    """
)

while True:
    state_manager.window.fill(colors.bg_color)
    state_manager.game_state.handle_current_state()
    pygame.display.flip()
