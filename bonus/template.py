import pygame
import random

#The game will loop until the user closes it.
gameLoop = True

#The clock will be used to control how fast the screen updates
clock = pygame.Time.Clock()

#Initialize the game.
pygame.init() #Initializes game engine
width, height = 700, 500 #Sets window width and height
screen = pygame.display.set_mode((width, height)) #Draws window

#--------Main Loop--------
while gameLoop:
	screen.fill(0) #Clear the screen before drawing it again.
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
