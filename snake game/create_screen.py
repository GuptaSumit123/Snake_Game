#create the screen
import pygame
pygame.init()
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('snake Game made by Sumit Gupta')
game_over=False
while not game_over:
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           game_over=True
pygame.quit()
quit()
