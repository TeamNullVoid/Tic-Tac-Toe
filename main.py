import pygame
import colors
import dimen
import state_manager

pygame.init()

window = pygame.display.set_mode(dimen.window_size)
pygame.display.set_caption(state_manager.app_name)

game_state = state_manager.GameState(window)

while True:
    window.fill(colors.bg_color)
    game_state.handle_current_state()
    pygame.display.flip()
