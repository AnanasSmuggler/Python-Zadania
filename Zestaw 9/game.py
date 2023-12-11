from board import Board
from tetrominos import *
import random

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.tetrominos = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.tetrominos) == 0:
            self.tetrominos = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.tetrominos)
        self.tetrominos.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False:
            self.current_block.move(-1, 0)

    def rotate_block(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.undo_rotate()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.board.is_inside(tile[0], tile[1]) == False:
                return False
        return True

    def draw(self, screen):
        self.board.draw(screen)
        self.current_block.draw(screen)