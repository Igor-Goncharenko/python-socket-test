from typing import TypeAlias
import pygame
from .constants import *


Color: TypeAlias = tuple[int, int, int]


class ScrollableWindowBlock(pygame.sprite.Sprite):
    def __init__(
            self,
            x: int = 0, y: int = 0,
            width: int = 500, height: int = 100,
            border: int = 5, border_color: Color = (0, 0, 0),
    ):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.display.get_surface()
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.border = border
        self.border_color = border_color

    def draw(self):
        """Draws empty block.
        You should remake this function.
        """
        pygame.draw.rect(
            self.surface, self.border_color,
            (self.x, self.y, self.width, self.height)
        )
        pygame.draw.rect(
            self.surface, WHITE,
            (self.x + self.border, self.y + self.border,
             self.width - self.border * 2, self.height - self.border * 2)
        )

    def center_x(self, x1: int, x2: int):
        self.x = (x2 - x1) // 2 - self.width // 2


class ScrollableWindow(pygame.sprite.Sprite):
    def __init__(
            self,
            x: int = 0, y: int = 0,
            width: int = 500, height: int = HEIGHT,
            scroll_speed: int = 10,
            blocks: list[ScrollableWindowBlock] = None
    ):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.blocks = blocks
        self.scroll_pos = 0
        self.scroll_speed = scroll_speed
        self.max_scroll = 0

    def scroll(self, up: bool = False, down: bool = False):
        """Change scroll_pos variable

        -Add this code to event loop:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.menu.scroll_window.scroll(up=True)
            elif event.button == 5:
                self.menu.scroll_window.scroll(down=True)

        :param up: to decrease scroll_pos
        :param down: to increase scroll_pos
        """
        if self.blocks is not None and len(self.blocks) > 0:
            self.max_scroll = len(self.blocks) * (self.blocks[0].height + 10) - HEIGHT + 100
        else:
            self.max_scroll = 0
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.max_scroll >= 0 and (self.x <= mouse_x <= self.x + self.width) \
                and (self.y <= mouse_y <= self.y + self.height):
            if up and self.scroll_pos >= 0:
                self.scroll_pos -= self.scroll_speed
            elif down and self.scroll_pos <= self.max_scroll:
                self.scroll_pos += self.scroll_speed

    def draw(self):
        """Drawing blocks"""
        if self.blocks is not None:
            y = self.y
            for block in self.blocks:
                block.center_x(0, self.width)
                block.y = y - self.scroll_pos
                block.draw()

                y += block.height + 10
