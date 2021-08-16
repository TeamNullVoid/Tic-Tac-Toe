import pygame

import colors
import dimen


def set_position(rect, centerx, centery, left, top, right, bottom):
    if centerx != -1:
        rect.centerx = centerx
    if centery != -1:
        rect.centery = centery
    if top != -1:
        rect.top = top
    if left != -1:
        rect.left = left
    if right != -1:
        rect.right = right
    if bottom != -1:
        rect.bottom = bottom


pygame.init()


class Image:
    def __init__(self, src, pos=(-1, -1, -1, -1, -1, -1)):
        self.value = pygame.image.load(src)
        self.rect = self.value.get_rect()
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])


class Text:
    def __init__(self, text, size, color, pos=(-1, -1, -1, -1, -1, -1), sys_font=None, f='Ubuntu'):
        if sys_font is not None:
            font = pygame.font.SysFont(sys_font, size)
        else:
            font = pygame.font.Font(f'assets/{f}-Regular.ttf', size)
        self.value = font.render(text, size, color)
        self.rect = self.value.get_rect()
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])


class Button:
    def __init__(self, text, text_size, size, text_color, color, pos=(-1, -1, -1, -1, -1, -1)):
        self.value = pygame.Surface(size)
        self.value.fill(colors.bg_color)
        self.rect = pygame.draw.rect(self.value, color, pygame.Rect(0, 0, *size), 0, dimen.button_radius)
        pygame.draw.rect(self.value, colors.primary, pygame.Rect(0, 0, *size), dimen.button_border_width, dimen.button_radius)
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])
        text_v = Text(text, text_size, text_color, (self.rect.width // 2, self.rect.height // 2, -1, -1, -1, -1))
        self.value.blit(text_v.value, text_v.rect)
