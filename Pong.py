import pygame
import sys
pygame.init()
pygame.font.init() 


# Set display, width : 800px, height : 600px
Screen = pygame.display.set_mode((800, 600))
# Set title or caption or whatever
pygame.display.set_caption("Pong")
# Set clock for control FPS.
FPS = pygame.time.Clock()

#I set running = True just for creating game loop
running = True

# Our screen color - Grey, this is RGB color.
Screen.fill((64, 64, 64))

# Draw some rectangles!
myfont = pygame.font.SysFont('Arial', 15)


# The basic set-up for Pong game : Ball and 2 players.
# pygame.Rect(x, y, width, height) - x, y is Rect position, You should check how Pygame works to have a better overview!
Ball = pygame.Rect(375, 275, 20, 20)
Player1 = pygame.Rect(10, 160, 10, 100)
Player2 = pygame.Rect(780, 160, 10, 100)

Ball_x = 5
Ball_y = 5

Player1Score = 0
Player2Score = 0

def Game_restart():
    # I just simply reset the Ball position (exactly the same)
    Ball.x = 375
    Ball.y = 275

def BallAnimation():

    # These variables are local variables, which mean you can only use it within this function, to use it outside the function,
    # Just turn it into global variables (Learn more about Scope).
    global Ball_x, Ball_y, Player1Score, Player2Score
    Ball.x += Ball_x
    Ball.y += Ball_y

    if Ball.top <= 0 or Ball.bottom >= 600:
        # When the ball hits the top and bottom wall, it bounces.
        Ball_y *= -1


    if Ball.left <= 0 or Ball.right >= 800:
        if Ball.left <= 0:
            Player2Score += 1
        if Ball.right >= 800:
            Player1Score += 1
        Game_restart()

    # Check for collisons!
    if Ball.colliderect(Player1) or Ball.colliderect(Player2):
        Ball_x *= -1

while running:

    # This for loop keeps window visible
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

    # My above function!
    BallAnimation()

    # We have to draw some rects we have created above!
    pygame.draw.rect(Screen, (255, 255, 255), Player1)
    pygame.draw.rect(Screen, (255, 255, 255), Player2)
    pygame.draw.ellipse(Screen, (255, 255, 255), Ball)
    

    Screen.blit(textsurface,(0,0))
    Screen.blit(textsurface2,(600,0))

    pygame.display.update()

    # From the pygame.time.Clock(), just to make FPS
    FPS.tick(60)
    pygame.display.flip()


