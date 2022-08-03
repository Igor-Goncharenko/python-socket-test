from typing import TypeAlias
import pygame

Color: TypeAlias = tuple[int, int, int]


class InputLabel(pygame.sprite.Sprite):
    def __init__(
            self,
            x: int = 0, y: int = 0,
            width: int = 200, height: int = 70,
            main_color: Color = (255, 255, 255),
            border: int = 5, border_color: Color = (0, 0, 0),
            text_color: Color = (0, 0, 0), text_font: str = 'arial',
            max_chars: int = 12
    ):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.display.get_surface()
        # button general settings
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.main_color = main_color
        self.border = border
        self.border_color = border_color
        self.text_color = text_color
        self.text_font = text_font
        self.max_chars = max_chars

        self.font_size = int(self.height * 0.70)

        self.input_text = ""
        self.selected = False  # True if input active

    def _draw(self):
        """Drawing input label on the screen"""
        pygame.draw.rect(
            self.surface, self.border_color,
            (self.x, self.y, self.width, self.height)
        )
        pygame.draw.rect(
            self.surface, self.main_color,
            (self.x + self.border, self.y + self.border,
             self.width - self.border * 2, self.height - self.border * 2)
        )
        font = pygame.font.SysFont(self.text_font, self.font_size)
        text = font.render(self.input_text, True, self.text_color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.surface.blit(text, text_rect)

    def _get_input(self):
        """Gets input from keyboard"""
        keys = pygame.key.get_pressed()
        if self.selected and len(self.input_text) <= self.max_chars:
            for i in range(97, 123):
                if keys[i] and len(self.input_text) <= self.max_chars:
                    self.input_text += pygame.key.name(i)

        if keys[pygame.K_BACKSPACE] and self.selected:
            # remove last char
            self.input_text = self.input_text[0:-1]

    def _set_active(self):
        """Sets active input label if it was clicked"""
        mouse = pygame.mouse.get_pressed(3)
        keys = pygame.key.get_pressed()

        if mouse[0] and self._check_pos():
            self.selected = True
        elif mouse[0] or (self.selected and keys[pygame.K_RETURN]):
            self.selected = False

    def _check_pos(self) -> bool:
        """Returns True if mouse in button."""
        x, y = pygame.mouse.get_pos()
        if self.x <= x <= self.x + self.width and \
                self.y <= y <= self.y + self.height:
            return True
        return False

    def run(self):
        """Main run function"""
        self._set_active()
        self._draw()
        self._get_input()

    def get_input(self):
        return self.input_text

    def center_x(self, x1: int, x2: int):
        self.x = (x2 - x1) // 2 - self.width // 2

    def center_y(self, y1: int, y2: int):
        self.y = (y2 - y1) // 2 - self.height // 2
