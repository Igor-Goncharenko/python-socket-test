from typing import TypeAlias
import pygame
from interface.menu import Menu
from interface.button import DefaultButton
from interface.input_label import InputLabel
from interface.constants import *
from interface.scrollable_window import ScrollableWindow, ScrollableWindowBlock


Color: TypeAlias = tuple[int, int, int]


class JoinGameBlock(ScrollableWindowBlock):
    def __init__(
            self,
            game_name: str, user_name: str, opened: bool,
            x: int = 0, y: int = 0,
            width: int = 600, height: int = 100,
            border: int = 5, border_color: Color = (0, 0, 0),
    ):
        super(JoinGameBlock, self).__init__(
            x=x, y=y, width=width, height=height, border=border, border_color=border_color
        )
        self.game_name = game_name
        self.user_name = user_name
        self.opened = opened
        self.join_button = DefaultButton(width=100, height=self.height//2, border=3, text="join")
        self.join_button.center_x(0, WIDTH)
        self.text_font = "arial"
        self.font_size = 30

    def draw(self):
        """"""
        pygame.draw.rect(
            self.surface, self.border_color,
            (self.x, self.y, self.width, self.height)
        )
        pygame.draw.rect(
            self.surface, WHITE,
            (self.x + self.border, self.y + self.border,
             self.width - self.border * 2, self.height - self.border * 2)
        )
        # game name drawing
        font = pygame.font.SysFont(self.text_font, self.font_size)
        text = font.render(self.game_name, True, BLACK)
        self.surface.blit(text, (self.x + self.border + 5, self.y + self.border + 2))
        # user name drawing
        font = pygame.font.SysFont(self.text_font, int(self.font_size*0.5))
        text = font.render(self.user_name, True, DARKGREY)
        self.surface.blit(text, (self.x + self.border + 10, self.y + self.border + self.height//3 + 2))
        if self.opened:
            text = font.render("opened", True, DARKGREY)
        else:
            text = font.render("closed", True, DARKGREY)
        self.surface.blit(text, (self.x + self.border + 10, self.y + self.border + self.height//3*2 + 2))
        self.join_button.x = self.x + self.width - self.join_button.width - self.border - 5
        self.join_button.y = (self.y + self.height) - int(self.join_button.height * 1.5)
        self.join_button.run()


class SearchGameMenu(Menu):
    def __init__(self, user_name: str = ""):
        super(SearchGameMenu, self).__init__()
        self.top_bar_height = 50
        self.input_game = InputLabel(
            x=QUARTER_WIDTH+10, width=QUARTER_WIDTH*2-20, height=self.top_bar_height, border=4, max_chars=15
        )
        self.create_button = DefaultButton(
            x=QUARTER_WIDTH*3, width=int(QUARTER_WIDTH*0.95), height=self.top_bar_height, border=4, text="Create game"
        )
        self.update_button = DefaultButton(
            y=HEIGHT-self.top_bar_height,
            width=200, height=self.top_bar_height, border=4,
            text="update"
        )
        self.update_button.center_x(0, WIDTH)
        self.games = ScrollableWindow(
            x=0, y=self.top_bar_height+10, width=WIDTH, height=HEIGHT-self.top_bar_height-10, scroll_speed=30
        )
        self.user_name = user_name

        self.text_font = 'arial'
        self.font_size = min(40, 40 - len(self.user_name))

    def draw(self):
        """"""
        self.games.draw()
        pygame.draw.rect(self.surface, WHITE, (0, 0, WIDTH, self.top_bar_height))
        font = pygame.font.SysFont(self.text_font, self.font_size)
        text = font.render(self.user_name, True, (0, 0, 0))
        text_rect = text.get_rect(center=(2 + QUARTER_WIDTH//2, self.top_bar_height//2))
        self.surface.blit(text, text_rect)
        self.input_game.run()
        self.create_button.run()

        pygame.draw.rect(self.surface, WHITE, (0, HEIGHT-self.top_bar_height, WIDTH, self.top_bar_height))
        self.update_button.run()
