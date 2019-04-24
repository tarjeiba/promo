import pygame
import random
 
# R(ed), G(reen), B(lue)
SCREEN_COLOR = (255, 255, 0)
BALL_COLOR = (255, 255, 255)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25
 
class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vel_x = 0
        self.vel_y = 0

 
def make_ball():
    ball = Ball()
    
    # Setter posisjonen til ballen
    ball.x = 350
    ball.y = 100
 
    # Setter farten til ballen
    ball.vel_x = 0
    ball.vel_y = 5
    return ball
 
# Herfra er hovedprogrammet
pygame.init()

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Balls")

done = False

clock = pygame.time.Clock()

ball_list = []

ball = make_ball()
ball_list.append(ball)
 
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True

    if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
        ball.vel_y *= -1
    if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
        ball.vel_x *= -1

    if ball.vel_y < 1:
        ball.y += ball.vel_y
        ball.vel_y += 1
    else:
        ball.vel_y += 1
        ball.y += ball.vel_y
        
    
    screen.fill(SCREEN_COLOR)

    # Draw the balls
    for ball in ball_list:
        pygame.draw.circle(screen, BALL_COLOR, [ball.x, ball.y], BALL_SIZE)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
 
