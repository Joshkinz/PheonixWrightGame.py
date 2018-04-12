import pygame
import random

#The game will loop until the user closes it.
gameLoop = True

#The clock will be used to control how fast the screen updates
clock = pygame.Time.Clock()

#--------Main Loop--------
while gameLoop:
	#----Main event loop
	for event in pygame.event.get(): #User did something
		if event.type == pygame.QUIT(): #If User closed program then...
			gameLoop = False #...Quit the program
			
	#----Game Logic
	
	#--------
	
	#----Drawing code
	
	#--------
	
	pygame.display.flip() #Update the display
	
	#----FPS Limit
	clock.tick(60)

pygame.quit() #Once the main loop is left, we quit the game.
