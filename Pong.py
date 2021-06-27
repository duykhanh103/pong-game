import pygame
import sys
pygame.init()
pygame.font.init() 



Screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
FPS = pygame.time.Clock()
running = True

Screen.fill((64, 64, 64))

# Draw some rectangles!
myfont = pygame.font.SysFont('Arial', 20)



Ball = pygame.Rect(375, 275, 20, 20)
Player1 = pygame.Rect(10, 160, 10, 100)
Player2 = pygame.Rect(780, 160, 10, 100)
Ball_x = 5
Ball_y = 5
Player1Score = 0
Player2Score = 0

def Game_restart():
    Ball.x = 375
    Ball.y = 275

def BallAnimation():


    global Ball_x, Ball_y, Player1Score, Player2Score
    Ball.x += Ball_x
    Ball.y += Ball_y

    if Ball.top <= 0 or Ball.bottom >= 600:
        Ball_y *= -1


    if Ball.left <= 0 or Ball.right >= 800:
        if Ball.left <= 0:
            Player2Score += 1
        if Ball.right >= 800:
            Player1Score += 1
        Game_restart()


    if Ball.colliderect(Player1) or Ball.colliderect(Player2):
        Ball_x *= -1

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    textsurface = myfont.render(f'Player 1 score : {Player1Score}', True, (255, 255, 255))
    textsurface2 = myfont.render(f'Player 2 score : {Player2Score}', True, (255, 255, 255))
    
    Keys = pygame.key.get_pressed()
    # Player1:
    if Keys[pygame.K_w] and Player1.y > 0:
        Player1.y -= 20
    if Keys[pygame.K_s] and Player1.y < 560:
        Player1.y += 20

    # Player2:
    if Keys[pygame.K_UP] and Player2.y > 0:
        Player2.y -= 20
    if Keys[pygame.K_DOWN] and Player2.y < 560:
        Player2.y += 20

    Screen.fill((64, 64, 64))

    BallAnimation()

    pygame.draw.rect(Screen, (255, 255, 255), Player1)
    pygame.draw.rect(Screen, (255, 255, 255), Player2)
    pygame.draw.ellipse(Screen, (255, 255, 255), Ball)
    
    Screen.blit(textsurface,(0,0))
    Screen.blit(textsurface2,(600,0))

    pygame.display.update()
    FPS.tick(60)
    pygame.display.flip()

