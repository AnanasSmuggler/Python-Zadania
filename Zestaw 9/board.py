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

    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for col in range(self.cols):
            if self.grid[row][col] == 0:
                return False
        return True
    
    def clear_row(self, row):
        self.grid[row] = [0 for i in range(self.cols)]
        
    def move_row_down(self, row, num_rows):
        self.grid[row+num_rows] = self.grid[row]
        self.clear_row(row)

    def clear_full_rows(self):
        completed = 0
        #Od ostatniego rzędu do pierwszego
        for row in range(self.rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        self.grid = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size+11, row*self.cell_size+11, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)