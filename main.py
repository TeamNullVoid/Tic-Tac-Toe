import pygame
import colors
import state_manager

pygame.init()

pygame.display.set_caption(state_manager.app_name)

while True:
    state_manager.window.fill(colors.bg_color)
    state_manager.game_state.handle_current_state()
    pygame.display.flip()
