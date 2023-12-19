import pygame
import sys
from colors import Colors
from game import Game

#Funkcja main - ustawia wszystkie parametry gry i obsługuje pętle zdarzeń
def main() -> None:
    pygame.init()
    
    colors = Colors() #Klasa z kolorami
    
    #Ustawienia HUD-a
    title_font = pygame.font.Font(None, 40)
    next_font = pygame.font.Font(None, 32)
    score_surface = title_font.render("Wynik:", True, colors.white)
    next_surface = next_font.render("Nastepny blok:", True, colors.white)
    game_over_surface = title_font.render("KONIEC GRY", True, colors.white)
    score_rect = pygame.Rect(320,55,170,60)
    next_rect = pygame.Rect(320,215,170,180)
    
    #Ustawienie ekranu oraz nazwy okna
    screen = pygame.display.set_mode((500,620))
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()

    game = Game() #Główna obsługa gry
    
    #Customowy event służący do obsługi opadania bloków
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 300)

    #Pętla zdarzeń - obługa klawiszy
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.reset()
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate_block()
                    
            #Automatyczne opadanie bloków
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()
                
        #Wypisanie labeli na ekranie
        score_value_surface = title_font.render(f'{game.score}', True, colors.white)
        screen.fill(colors.background_color)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (330, 180, 50, 50))
        
        #Wypisanie komunikatu Game Over
        if game.game_over == True:
            screen.blit(game_over_surface, (320, 450, 50, 50))

        #Rysowanie HUD-a
        pygame.draw.rect(screen, Colors.foreground_color, score_rect, 0)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
        pygame.draw.rect(screen, Colors.foreground_color, next_rect, 0)
        game.draw(screen)
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()