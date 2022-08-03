from typing import TypeAlias, Any
import pygame


Color: TypeAlias = tuple[int, int, int]


class DefaultButton(pygame.sprite.Sprite):
    """"""
    def __init__(
            self, x: int = 0, y: int = 0,
            width: int = 200, height: int = 70,
            main_color: Color = (255, 255, 255),
            border: int = 5, border_color: Color = (0, 0, 0),
            text: str = "button", text_color: Color = (0, 0, 0), text_font: str = 'arial',
            func: Any = None
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
        self.text = text
        self.text_color = text_color
        self.text_font = text_font
        self.func = func

        self.font_size = int(self.height * 0.70)

    def _draw(self, invert: bool = False) -> None:
        """Drawing button on display.

        :param invert: invert colors (can be used if button pressed)
        :return:
        """
        pygame.draw.rect(
            self.surface, self.border_color,
            (self.x, self.y, self.width, self.height)
        )

        font = pygame.font.SysFont(self.text_font, self.font_size)

        if not invert:
            pygame.draw.rect(
                self.surface, self.main_color,
                (self.x + self.border, self.y + self.border,
                 self.width - self.border * 2, self.height - self.border * 2)
            )
            text = font.render(self.text, True, self.text_color)
        else:
            pygame.draw.rect(
                self.surface, self.border_color,
                (self.x + self.border, self.y + self.border,
                 self.width - self.border * 2, self.height - self.border * 2)
            )
            text = font.render(self.text, True, self.main_color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.surface.blit(text, text_rect)

    def run(self, *args, **kwargs) -> None:
        """Activates function and switch button colors if button pressed.

        :param args: args for func
        :param kwargs: kwargs for func
        :return:
        """
        keys = pygame.mouse.get_pressed(3)

        if keys[0] and self._check_pos():
            if self.func is not None:
                self.func(*args, **kwargs)
            self._draw(invert=True)
        else:
            self._draw()

    def _check_pos(self) -> bool:
        """Returns True if mouse in button."""
        x, y = pygame.mouse.get_pos()
        if (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height):
            return True
        return False

    def center_x(self, x1: int, x2: int):
        self.x = (x2 - x1) // 2 - self.width // 2

    def center_y(self, y1: int, y2: int):
        self.y = (y2 - y1) // 2 - self.height // 2
