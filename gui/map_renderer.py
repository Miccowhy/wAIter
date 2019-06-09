import pygame
import lib.ptext as ptext
from constants.images import BANANA
from constants.bananas import BANANA_COST
from constants.colors import TRANSPARENT_BLUE
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT


class MapRenderer:
    def __init__(self, environment, screen, agent, customer):
        self.environment = environment
        self.screen = screen
        self.agent = agent
        self.customer = customer
        self.text_queue = []
        self.last_tick = pygame.time.get_ticks()
        self.textbox_duration = 4000
        self.current_text = None

    def render(self):
        self._draw_grid()
        self._draw(self.agent)
        self._draw(self.customer)
        self._display_textbox()

    def _draw_grid(self):
        for row in range(self.environment.grid_width):
            for col in range(self.environment.grid_length):
                #tile = self.environment.grid[row][col]
                tile = self.environment.grid[col][row]
                self._draw(tile)
                if tile.occupation is not None:
                    self._draw(tile.occupation)
                if tile.step_cost == BANANA_COST:
                    self._draw(tile, image=BANANA)

    def _draw(self, tile, image=None):
        if image is None:
            self.screen.blit(tile.image, tile.rect.topleft)
        else:
            self.screen.blit(pygame.transform.scale(image, (50, 50)), tile.rect.topleft)

    def _display_textbox(self):
        self._check_textbox_duration()
        if self.current_text is not None:
            ptext.draw(self.current_text, (0, 300), sysfontname='Comic Sans MS', fontsize=24)
            textbox = pygame.Surface((450, 350), pygame.SRCALPHA)
            textbox.fill(TRANSPARENT_BLUE)
            self.screen.blit(textbox, (0, 300))

    def _check_textbox_duration(self):
        now = pygame.time.get_ticks()
        if now - self.last_tick >= self.textbox_duration:
            if self.text_queue:
                self.current_text = self.text_queue.pop(0)
                self.last_tick = now
            else:
                self.current_text = None
