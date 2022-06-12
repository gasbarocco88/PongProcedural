from math import copysign, ceil
import pygame
from pygame.locals import *
from random import randint, randrange

pygame.init()

#initial settings
w = 1400
h = 800
screen = pygame.display.set_mode((w, h))
clk = pygame.time.Clock()



#background creation
field = pygame.image.load("field.png").convert()
field = pygame.transform.scale(field, (w,h))
screen.blit(field,(0,0))


#ball creation
ball = pygame.image.load("ball.jpg").convert()
ball = pygame.transform.scale(ball,(40, 40))
rect_ball = ball.get_rect()
rect_ball.center = (w/2, h/2)
vel_ball = [randint(3,7),randint(3,7)]


#player1 creation
player1 = pygame.image.load("player1.jpg").convert()
player1 = pygame.transform.scale(player1,(50,150))
rect_player1 = player1.get_rect()
rect_player1.center = (50,h/2)
pressed = None


#AI player2 creation 
player2 = pygame.image.load("player2.jpg").convert()
player2 = pygame.transform.scale(player2,(50,150))
rect_player2 = player2.get_rect()
rect_player2.center = (1350,h/2)
vel_player2 = [0,30]

#score
score_player1 = 0
score_player2 = 0
font = pygame.font.SysFont("arial",50)
score1 = font.render(f"{score_player1}", True, (0,0,0))
score2 = font.render(f"{score_player2}", True, (0,0,0))



done = False
while not done:
    # windows event cycle
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True
        elif ev.type == KEYDOWN and ev.key in (K_UP, K_DOWN, K_RIGHT, K_LEFT):
            pressed = ev.key
        elif ev.type == KEYUP and ev.key == pressed:
            pressed = None


    #game logic

    #ball movement
    rect_ball.x -= vel_ball[0]
    rect_ball.y += vel_ball[1]
    if rect_ball.left < 0: # e punto fatto
        score_player2 += 1
        score2 = font.render(f"{score_player2}", True, (0,0,0))
        rect_ball.center = (w/2, h/2)
    if rect_ball.right > w:
        score_player1 += 1
        score1 = font.render(f"{score_player1}", True, (0,0,0))
        rect_ball.center = (w/2, h/2)
        vel_ball[0] = int(copysign(randint(5,10),-vel_ball[0]))
        vel_ball[1] = randrange(-10,10)

    if rect_ball.top < 0 or rect_ball.bottom > h:
        vel_ball[1] = -vel_ball[1]


    #player2 movement
    rect_player2.y -= vel_player2[1]
    if rect_player2.top < 0 or rect_player2.bottom > h:
        vel_player2[1] = -vel_player2[1]    


    #player1 movement
    if pressed == K_UP:
        if rect_player1.top <=0:
            rect_player1.top = 0
        else:
            rect_player1.top -= 5
    elif pressed == K_DOWN:
        if rect_player1.bottom >= h:
            rect_player1.bottom = h
        else:
            rect_player1.bottom += 5
    elif pressed == K_LEFT:
        if rect_player1.left <= 50:
            rect_player1.left = 50
        else:
            rect_player1.left -=5
    elif pressed == K_RIGHT:
        if rect_player1.right >= w/4:
            rect_player1.right = w/4
        else:
            rect_player1.right +=5
    
    #ball-player bounce
    if rect_ball.colliderect(rect_player1) or rect_ball.colliderect(rect_player2):
        #vel_ball[0] = -vel_ball[0]
        vel_ball[0] = int(copysign(randint(5,10),-vel_ball[0]))



    #render
    screen.blit(field, (0,0))
    screen.blit(ball, rect_ball)
    screen.blit(player1, rect_player1)
    screen.blit(player2, rect_player2)
    screen.blit(score1,(w//4,50))
    screen.blit(score2,(w*3//4,50))

    pygame.display.flip()

    clk.tick(60)



pygame.quit()
