import pygame

# initialize the imported pygame modules, returns the tuple of successful and failed imports
pygame.init()

# initializing the gamescreen
gameScreen=pygame.display.set_mode(size=(640,480))

# setting the title of the game window
pygame.display.set_caption('Snake')

GAMECLOSE=False
BLACK=(0,0,0)
while not GAMECLOSE:

    # gets all the events from event queue
    # event is nothing but the input from the user
    for event in pygame.event.get():
        print(event)
        # pygame.QUIT has a value 4
        if event.type==pygame.QUIT:
            GAMECLOSE=True
    gameScreen.fill((176,176,255))
    pygame.draw.rect(gameScreen,BLACK,(200,200,20,20))
    pygame.display.update()

# unintitialize all imported modules
pygame.quit()
