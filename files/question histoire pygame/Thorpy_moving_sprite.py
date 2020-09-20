import pygame, thorpy, os
def COLOR():
    os.system("color 0A")

COLOR()

pygame.init()
pygame.key.set_repeat(300, 30)
screen = pygame.display.set_mode((400,400))
screen.fill((255,255,255))
rect = pygame.Rect((0, 0, 50, 50))
rect.center = screen.get_rect().center
clock = pygame.time.Clock()

pygame.draw.rect(screen, (255,0,0), rect)
pygame.display.flip()

#when left arrow is pressed, the red rect goes to the left
playing_game = True
while playing_game:
    clock.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing_game = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.draw.rect(screen, (255,255,255), rect)
                pygame.display.update(rect)
                rect.move_ip((-5,0))
                pygame.draw.rect(screen, (255,0,0), rect)
                pygame.display.update(rect)
            elif event.key == pygame.K_RIGHT:
                pygame.draw.rect(screen, (255,255,255), rect)
                pygame.display.update(rect)
                rect.move_ip((5,0))
                pygame.draw.rect(screen, (255,0,0), rect)
                pygame.display.update(rect)
            elif event.key == pygame.K_UP:
                pygame.draw.rect(screen, (255,255,255), rect)
                pygame.display.update(rect)
                rect.move_ip((0,-5))
                pygame.draw.rect(screen, (255,0,0), rect)
                pygame.display.update(rect)
            elif event.key == pygame.K_DOWN:
                pygame.draw.rect(screen, (255,255,255), rect)
                pygame.display.update(rect)
                rect.move_ip((0,5))
                pygame.draw.rect(screen, (255,0,0), rect)
                pygame.display.update(rect)
            


pygame.quit()
