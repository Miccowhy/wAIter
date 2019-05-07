import pygame
from .spritesheet import Spritesheet
from constants.movement import Direction as Dir, MOVEMENT_ANIMATION_INTERVAL


class Animator:
    def __init__(self, entity, spritesheet):
        self.entity = entity
        self.spritesheet = Spritesheet(spritesheet)
        images = self.spritesheet.load_strip((0, 0, 64, 55), 9, colorkey=(64, 121, 78))
        # Standing positions are always at index 1
        self.sprites = {
                Dir.UP: [images[0], images[1], images[2]],
                Dir.DOWN: [images[6], images[7], images[8]],
                Dir.LEFT: [pygame.transform.flip(images[3], 1, 0),
                           pygame.transform.flip(images[4], 1, 0),
                           pygame.transform.flip(images[5], 1, 0)],
                Dir.RIGHT: [images[3], images[4], images[5]]
        }
        self.cur_frame = 1
        # Set timer for movement animation
        pygame.time.set_timer(pygame.USEREVENT, MOVEMENT_ANIMATION_INTERVAL)

    def change_direction(self, direction):
        if self.entity.direction != direction and direction is not None:
            self.entity.direction = direction
            self.entity.image = self.sprites[direction][1]

    def fix_standing_position(self):
        if not self.entity.actions:
            self.entity.image = self.sprites[self.entity.direction][1]

    def animate_movement(self):
        if pygame.event.poll():
            self.entity.image = self.sprites[self.entity.direction][self.cur_frame]
            self.cur_frame = self.cur_frame + 1
            if self.cur_frame == 3:
                self.cur_frame = 0
