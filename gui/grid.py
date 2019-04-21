from constants.dimensions import TILE_WIDTH, TILE_HEIGHT, TILE_MARGIN
from constants.images import ENTRANCE


def draw_grid(environment, screen):
    for row in range(environment.grid_width):
        for column in range(environment.grid_length):
            tile = environment.grid[row][column]
            # This is going to be deleted soon
            if tile.is_kitchen_entrance:
                _draw_object(screen, column, row, ENTRANCE)
            else:
                _draw_object(screen, column, row, tile.image)

            if tile.occupation is not None:
                _draw_object(screen, column, row, tile.occupation.image)


def _draw_object(screen, column, row, image):
    screen.blit(image, [(TILE_MARGIN + TILE_WIDTH) * column + TILE_MARGIN,
                        (TILE_MARGIN + TILE_HEIGHT) * row + TILE_MARGIN,
                        TILE_WIDTH, TILE_HEIGHT])
