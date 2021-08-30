import pygame

import colors
import dimen
import strings


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
    def __init__(self, text, size, color, pos=(-1, -1, -1, -1, -1, -1), sys_font=None, f='Ubuntu', callback=None):
        if sys_font is not None:
            font = pygame.font.SysFont(sys_font, size)
        else:
            font = pygame.font.Font(f'assets/{f}-Regular.ttf', size)
        self.text = text
        self.value = font.render(text, size, color)
        self.rect = self.value.get_rect()
        self.callback = callback
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(x, y):
                    self.callback(self)


class Button:
    def __init__(self, text, text_size, size, text_color, color, callback, pos=(-1, -1, -1, -1, -1, -1)):
        self.value = pygame.Surface(size)
        self.value.fill(colors.bg_color)
        self.callback = callback
        self.text = text
        self.rect = pygame.draw.rect(self.value, color, pygame.Rect(0, 0, *size), 0, dimen.button_radius)
        pygame.draw.rect(self.value, colors.primary, pygame.Rect(0, 0, *size), dimen.button_border_width, dimen.button_radius)
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])
        text_v = Text(text, text_size, text_color, (self.rect.width // 2, self.rect.height // 2, -1, -1, -1, -1))
        self.value.blit(text_v.value, text_v.rect)

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(x, y):
                    self.callback(self)


class TextButton:
    def __init__(self, text, size, color, callback, pos=(-1, -1, -1, -1, -1, -1)):
        font = pygame.font.SysFont('segoeuisymbol', size)
        self.text = text
        self.value = font.render(text, size, color)
        self.rect = self.value.get_rect()
        self.callback = callback
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(x, y):
                    self.callback(self)


class InputField:
    def __init__(self, text, size, pos=(-1, -1, -1, -1, -1, -1)):
        self.active = False
        self.value = pygame.Surface(size)
        self.value.fill(colors.bg_color)
        self.text = text
        self.size = size
        self.rect = pygame.draw.rect(self.value, colors.white, pygame.Rect(0, 0, *size), 0, dimen.button_radius)
        pygame.draw.rect(self.value, colors.red_dark, pygame.Rect(0, 0, *size), dimen.button_border_width, dimen.button_radius)
        self.font = pygame.font.Font('assets/Righteous-Regular.ttf', dimen.button_text_size)
        self.text_surface = self.font.render(text, True, colors.black)
        self.text_rect = self.text_surface.get_rect()
        set_position(self.text_rect,-1, self.rect.height // 2, 20, -1, -1, -1)
        self.value.blit(self.text_surface, self.text_rect)
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    if self.text == strings.hint_code:
                        pass
                    else:
                        self.text = self.text[:-2]
                    if self.text == '':
                        self.text = strings.hint_code
                else:
                    if len(self.text) == 12:
                        return
                    if self.text == strings.hint_code:
                        self.text = ''
                    self.text += event.unicode.upper() + ' '
                pygame.draw.rect(self.value, colors.white, pygame.Rect(0, 0, *self.size), 0, dimen.button_radius)
                pygame.draw.rect(self.value, colors.red_dark, pygame.Rect(0, 0, *self.size), dimen.button_border_width, dimen.button_radius)
                self.text_surface = self.font.render(self.text, True, colors.black)
                self.value.blit(self.text_surface, self.text_rect)
