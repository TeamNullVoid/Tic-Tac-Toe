import pygame

import colors
import dimen
import string_vars


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

    def change_image(self, src):
        self.value = pygame.image.load(src)
        self.rect = self.value.get_rect()


class Text:
    def __init__(self, text, size, color, pos=(-1, -1, -1, -1, -1, -1), sys_font=None, f='Ubuntu', callback=None):
        if sys_font is not None:
            font = pygame.font.SysFont(sys_font, size)
        else:
            font = pygame.font.Font(f'assets/{f}-Regular.ttf', size)
        self.text = text
        self.color = color
        self.font = font
        self.pos = pos
        self.size = size
        self.value = font.render(text, size, color)
        self.rect = self.value.get_rect()
        self.callback = callback
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

    def update(self, text, color=None):
        if color is not None:
            self.color = color
        self.text = text
        self.value.fill(colors.bg_color)
        self.value = self.font.render(text, self.size, self.color)
        self.rect = self.value.get_rect()

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(x, y):
                    self.callback(self)


class Button:
    def __init__(self, text, text_size, size, text_color, color, callback, pos=(-1, -1, -1, -1, -1, -1)):
        self.value = pygame.Surface(size, pygame.SRCALPHA)
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
        self.value = pygame.Surface(size, pygame.SRCALPHA)
        self.text = text
        self.size = size
        self.text_color = colors.grey
        self.rect = pygame.draw.rect(self.value, colors.white, pygame.Rect(0, 0, *size), 0, dimen.button_radius)
        pygame.draw.rect(self.value, colors.red_dark, pygame.Rect(0, 0, *size), dimen.button_border_width, dimen.button_radius)
        self.font = pygame.font.Font('assets/Righteous-Regular.ttf', dimen.button_text_size)
        self.text_surface = self.font.render(text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect()
        set_position(self.text_rect, -1, self.rect.height // 2, 20, -1, -1, -1)
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
                    if self.text == string_vars.hint_code:
                        pass
                    else:
                        self.text = self.text[:-3]
                    if self.text == '':
                        self.text = string_vars.hint_code
                        self.text_color = colors.grey
                else:
                    if len(self.text) == 18:
                        return
                    if self.text == string_vars.hint_code:
                        self.text = ''
                        self.text_color = colors.black
                    self.text += event.unicode.upper() + '  '
                pygame.draw.rect(self.value, colors.white, pygame.Rect(0, 0, *self.size), 0, dimen.button_radius)
                pygame.draw.rect(self.value, colors.red_dark, pygame.Rect(0, 0, *self.size), dimen.button_border_width, dimen.button_radius)
                self.text_surface = self.font.render(self.text, True, self.text_color)
                self.value.blit(self.text_surface, self.text_rect)


def get_box_from_pos(pos):
    x, y = pos[0], pos[1]
    if 115 <= x <= 298 and 115 <= y <= 298:
        return 0
    elif 312 <= x <= 488 and 115 <= y <= 298:
        return 1
    elif 502 <= x <= 683 and 115 <= y <= 298:
        return 2
    elif 115 <= x <= 298 and 312 <= y <= 488:
        return 3
    elif 312 <= x <= 488 and 312 <= y <= 488:
        return 4
    elif 502 <= x <= 683 and 312 <= y <= 488:
        return 5
    elif 115 <= x <= 298 and 502 <= y <= 683:
        return 6
    elif 312 <= x <= 488 and 502 <= y <= 683:
        return 7
    elif 502 <= x <= 683 and 502 <= y <= 683:
        return 8
    else:
        return None


class Board:
    def __init__(self, size, pos, lines, callback):
        self.callback = callback
        self.checked = [0 for _ in range(9)]
        self.size = size
        self.pos = pos
        self.lines = lines
        self.value = pygame.Surface(size, pygame.SRCALPHA)
        for x in range(0, len(lines), 2):
            pygame.draw.line(self.value, colors.primary, lines[x], lines[x + 1], dimen.board_thk)
        self.rect = self.value.get_rect()
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

    def is_checked(self, pos):
        if pos is None:
            return
        if self.checked[pos] == 0:
            return False
        else:
            return True

    def mark_cross(self, box, player):
        if box == 0:
            pos = (40, 40)
            pos1 = (143, 143)
            pos2 = (143, 40)
            pos3 = (40, 143)
        elif box == 1:
            pos = (235, 40)
            pos1 = (338, 143)
            pos2 = (338, 40)
            pos3 = (235, 143)
        elif box == 2:
            pos = (430, 40)
            pos1 = (533, 143)
            pos2 = (533, 40)
            pos3 = (430, 143)
        elif box == 3:
            pos = (40, 235)
            pos1 = (143, 338)
            pos2 = (143, 235)
            pos3 = (40, 338)
        elif box == 4:
            pos = (235, 235)
            pos1 = (338, 338)
            pos2 = (338, 235)
            pos3 = (235, 338)
        elif box == 5:
            pos = (430, 235)
            pos1 = (533, 338)
            pos2 = (533, 235)
            pos3 = (430, 338)
        elif box == 6:
            pos = (40, 430)
            pos1 = (143, 533)
            pos2 = (143, 430)
            pos3 = (40, 533)
        elif box == 7:
            pos = (235, 430)
            pos1 = (338, 533)
            pos2 = (338, 430)
            pos3 = (235, 533)
        elif box == 8:
            pos = (430, 430)
            pos1 = (533, 533)
            pos2 = (533, 430)
            pos3 = (430, 533)
        else:
            pos, pos1, pos2, pos3 = [(0, 0) for _ in range(4)]
        self.checked[box] = player
        pygame.draw.line(self.value, colors.cross, pos, pos1, 15)
        pygame.draw.line(self.value, colors.cross, pos2, pos3, 15)

    def mark_circle(self, box, player):
        if box == 0:
            pos = (91.5, 91.5)
        elif box == 1:
            pos = (288.5, 91.5)
        elif box == 2:
            pos = (478.5, 91.5)
        elif box == 3:
            pos = (91.5, 288.5)
        elif box == 4:
            pos = (288.5, 288.5)
        elif box == 5:
            pos = (478.5, 288.5)
        elif box == 6:
            pos = (91.5, 478.5)
        elif box == 7:
            pos = (288.5, 478.5)
        elif box == 8:
            pos = (478.5, 478.5)
        else:
            pos = (-dimen.circle_rad, -dimen.circle_rad)
        self.checked[box] = player
        pygame.draw.circle(self.value, colors.circle, pos, dimen.circle_rad, dimen.board_thk)
        pass

    def check(self, pos, player):
        if not self.is_checked(pos):
            self.checked[pos] = player
            if player == 1:
                self.mark_circle(pos, player)
            else:
                self.mark_cross(pos, player)
            return True
        else:
            print("Position Already Marked")
            return False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            box = get_box_from_pos(event.pos)
            if box is not None:
                self.callback(self, box)

    def clean(self):
        self.__init__(self.size, self.pos, self.lines, self.callback)


class Cross:
    def __init__(self, size, callback, pos):
        self.value = pygame.Surface(size, pygame.SRCALPHA)
        self.callback = callback
        self.size = size
        pygame.draw.line(self.value, colors.cross, (50, 50), (size[0] - 50, size[1] - 50), dimen.cw_width + 2)
        pygame.draw.line(self.value, colors.cross, (size[0] - 50, 50), (50, size[1] - 50), dimen.cw_width + 2)
        self.rect = self.value.get_rect()
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])
        pass

    def handle_click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(x, y):
                    self.callback(self)

    def select(self):
        pygame.draw.rect(self.value, colors.cross, pygame.Rect(0, 0, *self.size), dimen.cw_select_width, dimen.button_radius)

    def unselect(self):
        pygame.draw.rect(self.value, colors.bg_color, pygame.Rect(0, 0, *self.size), dimen.cw_select_width, dimen.button_radius)


class Circle:
    def __init__(self, size, center, radius, width, pos, callback):
        self.size = size
        self.value = pygame.Surface(size, pygame.SRCALPHA)
        self.callback = callback
        pygame.draw.circle(self.value, colors.circle, center, radius, width)
        self.rect = self.value.get_rect()
        set_position(self.rect, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

    def handle_click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(x, y):
                    self.callback(self)

    def select(self):
        pygame.draw.rect(self.value, colors.circle, pygame.Rect(0, 0, *self.size), dimen.cw_select_width, dimen.button_radius)

    def unselect(self):
        pygame.draw.rect(self.value, colors.bg_color, pygame.Rect(0, 0, *self.size), dimen.cw_select_width, dimen.button_radius)
