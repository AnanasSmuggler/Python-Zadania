from board import Board
from tetrominos import *
import random

#Klasa zajmuje się główną obsługa gry
"""
self.board - klasa Board obsługująca planszę do gry
self.tetrominos - lista zawierająca klasy z odpowiednimi rodzajami bloków
self.current_block - obecny blok którym operujemy na planszy
self.next_block - następny blok którym będziemy operować
self.game_over - bool określający koniec gry
self.score - wynik gracza
"""

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.tetrominos = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    #Uaktualnienie wyniku na bazie wyczyszczonych linii
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared % 2 == 0:
            self.score += (lines_cleared/2) * 300
        elif lines_cleared % 3 == 0:
            self.score += (lines_cleared/3) * 500
        self.score += move_down_points
        
    #Losuje klasę bloku z listy i go zwraca
    def get_random_block(self):
        if len(self.tetrominos) == 0:
            self.tetrominos = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.tetrominos)
        self.tetrominos.remove(block)
        return block
    
    #Metoda obsługująca przesuwanie bloku w lewo (<-)
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    #Metoda obsługująca przesuwanie bloku w prawo (->)
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    #Metoda obsługująca przesuwanie się bloku w dół
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    #Metoda, która zmienia bloki, które obsługuje gracz i ustawia w pozycji końcowej blok, który obsługiwaliśmy     
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            self.board.grid[tile[0]][tile[1]] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.board.clear_full_rows()
        self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    #Metoda sprawdza czy blok może się pojawić się na planszy [obsługa game over]
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.board.is_empty(tile[0], tile[1]) == False:
                return False
        return True

    #Metoda obraca blok, który kontroluje gracz
    def rotate_block(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotate()

    #Metoda sprawdza czy blok znajduje się w granicach planszy
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.board.is_inside(tile[0], tile[1]) == False:
                return False
        return True

    #Metoda resetuje status gry
    def reset(self):
        self.board.reset()
        self.tetrominos = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        
    #Metoda rysuje na ekranie obiekty potrzebne do gry
    def draw(self, screen):
        self.board.draw(screen)
        self.current_block.draw(screen, 11, 11)
        
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)