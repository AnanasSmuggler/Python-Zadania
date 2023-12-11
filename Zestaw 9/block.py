from colors import Colors
import pygame

class Block:
    def __init__(self, id) -> None:
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation = 0
        self.colors = Colors.get_cell_colors()
    
    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    def get_cell_positions(self):
        tiles = self.cells[self.rotation]
        moved_tiles = []
        for position in tiles:
            position = (position[0] + self.row_offset, position[1] + self.col_offset)
            moved_tiles.append(position)

        return moved_tiles

    def rotate(self):
        self.rotation += 1
        if self.rotation >= len(self.cells):
            self.rotation = 0 

    def undo_rotate(self):
        self.rotation -= 1
        if self.rotation == 0:
            self.rotation = len(self.cells) - 1


    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile[1] * self.cell_size + offset_x, tile[0] * self.cell_size + offset_y, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)