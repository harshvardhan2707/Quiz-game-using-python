import math
import random
from sys import exit
import pygame
from pygame import mixer
import tkinter as tk
import sys
# import pdb

# Intialize the pygame
pygame.init()
# pdb.set_trace()
# Quizreturn=''

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Space_Invaders\\background.png')

# Sound
mixer.music.load("C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Space_Invaders\\background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Space_Invaders\\ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Space_Invaders\\player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Space_Invaders\\enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Space_Invaders\\bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
final_score_value=10
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    final_score_value=score_value

def game_won_text():
    won_text = over_font.render("YOU WON", True, (255, 255, 255))
    screen.blit(won_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
def StartGame():
    # pygame.init()
    global running
    global playerX
    global playerX_change
    global score_value
    global bulletX
    global bulletY
    global bullet_state
    while running:

        # RGB = Red, Green, Blue
        # screen.fill((0, 0, 0))
        # Background Image
        # pygame.display.update()
        screen.blit(background, (0, 0))
        # pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                running = False
                


            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletSound = mixer.Sound("C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Space_Invaders\\laser.wav")
                        bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736
        
        # if(final_score_value<10):
        #     for j in range(num_of_enemies):
        #         enemyY[j] = 2000
        #     game_won_text()
        #     mixer.music.stop()
        #     running=False

        if(score_value==1000):
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_won_text()
            mixer.music.stop()
            running=False
            # pygame.quit()
            
        else:
            # Enemy Movement
            for i in range(num_of_enemies):

                # Game Over
                if enemyY[i] > 440:
                    for j in range(num_of_enemies):
                        enemyY[j] = 2000
                    game_over_text()
                    running=False
                    # pygame.quit()
                    break

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 4
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -4
                    enemyY[i] += enemyY_change[i]

                # Collision
                collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    explosionSound = mixer.Sound("C:\\Users\\lenovo\\OneDrive\\Desktop\\CSE Project\\Space_Invaders\\explosion.wav")
                    explosionSound.play()
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(50, 150)

                enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state =="fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()
        pygame.init()