import pygame
import random
import config

#The game will loop until the user closes it.
gameLoop = True	

#Set other variables
position1 = 1 #There are 5 spots to stand in. The initial spot is the first. Pressing up or down will change this and move the player.
position2 = 1 #This is the enemy position

#Initialize the game.
pygame.init() #Initializes game engine
width, height = 700, 500 #Sets window width and height
screen = pygame.display.set_mode((width, height)) #Draws window
keys = [False, False, False, False, False, False]
phoenixSprite = pygame.image.load("resources/phoenix-sprite-A.png").convert()
playerXPos = 50
playerYPos = 650
object1Sprite = pygame.image.load("resources/object-sprite-1.png").convert()
object2Sprite = pygame.image.load("resources/object-sprite-2.png").convert()
object3Sprite = pygame.image.load("resources/object-sprite-3.png").convert()
objectSpeed = 7

#The clock will be used to control how fast the screen updates
clock = pygame.Time.Clock()

#--------Main Loop--------
while gameLoop:
	#----Main event loop
	for event in pygame.event.get(): #User did something
		if event.type == pygame.QUIT(): #If User closed program then...
			gameLoop = False #...Quit the program
		pressedKeys = pygame.key.get_pressed()
		if pressedKeys[eval(config.GO_UP)]:
			keys[0] = True
		if pressedKeys[eval(config.GO_DOWN)]:
			keys[1] = True
		if pressedKeys[eval(config.ITEM_A)]:
			keys[2] = True
		if pressedKeys[eval(config.ITEM_B)]:
			keys[3] = True
		if pressedKeys[eval(config.ITEM_C)]:
			keys[4] = True
		if pressedKeys[eval(config.ITEM_D)]:
			keys[5] = True
			
		if not pressedKeys[eval(config.GO_UP)]:
			keys[0] = False
		if not pressedKeys[eval(config.GO_DOWN)]:
			keys[1] = False
		if not pressedKeys[eval(config.ITEM_A)]:
			keys[2] = False
		if not pressedKeys[eval(config.ITEM_B)]:
			keys[3] = False
		if not pressedKeys[eval(config.ITEM_C)]:
			keys[4] = False
		if not pressedKeys[eval(config.ITEM_D)]:
			keys[5] = False
			
	#----Game Logic
	
	if keys[0] = True: #If "GO_UP" is pressed...
		if not position == 1: #If position is NOT already at the top...
			position += 1 #Go up one space
			playerYPos += 150 #Move the player sprite up
			keys[0] = False #Reset the keypress
			
	if keys[1] = True: #If "GO_DOWN" is pressed...
		if not position == 5: #If position is NOT already at the top...
			position -= 1 #Go up one space
			playerYPos -= 150 #Move the player sprite down
			keys[1] = False #Reset the keypress
			
	if keys[2] = True:
		object1XPos = 50
		object1YPos = playerYPos
		playerObject1 = True
		
	#----Drawing code
	
	screen.fill(255, 255, 255) #Clear the screen before drawing it again
	screen.blit(phoenixSprite, (playerXPos, playerYPos))
	if playerObject1 = True:
		object1XPos += objectSpeed
		screen.blit(object1Sprite, (50, playerYPos))
		if object1XPos > 450:
			playerObject1 = False
	if playerObject2 = True:
		object2XPos += objectSpeed
		screen.blit(object2Sprite, (50, playerYPos))
		if object3XPos > 450:
			playerObject1 = False
	f playerObject3 = True:
		object3XPos += objectSpeed
		screen.blit(object3Sprite, (50, playerYPos))
		if object3XPos > 450:
			playerObject1 = False
	pygame.display.flip() #Update the display
	
	#----FPS Limit
	clock.tick(60)

pygame.quit() #Once the main loop is left, we quit the game.
