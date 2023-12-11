import pygame
from colors import Colors

class Board:
    def __init__(self) -> None:
        self.rows = 20
        self.cols = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.colors = Colors.get_cell_colors()
    
    def is_inside(self, row, col):
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
            return True
        return False


    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size+1, row*self.cell_size+1, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)