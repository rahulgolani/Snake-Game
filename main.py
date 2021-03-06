import pygame

# initialize the imported pygame modules, returns the tuple of successful and failed imports
pygame.init()

BLACK=(0,0,0)
RED=(255,0,0)
WHITE=(255,255,255)
# alpha is the 4th parameter which defines the opacity/ degree of transparency

# initializing the gamescreen (surface/canvas)
gameScreen=pygame.display.set_mode(size=(640,480))
# gameScreen is the surface object

# setting the title of the game window
pygame.display.set_caption('Snake')

GAMECLOSE=False

POS_X=100
POS_Y=100
POS_X_CHANGE=0
POS_Y_CHANGE=0

clock=pygame.time.Clock()
# returns a pygame clock object

while not GAMECLOSE:
    # gets all the events from event queue
    # event is nothing but the input from the user
    for event in pygame.event.get():
        # print(event)
        # pygame.QUIT has a value 4
        if event.type==pygame.QUIT:
            GAMECLOSE=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                POS_X_CHANGE = -10
                POS_Y_CHANGE = 0
                # on having pressed the key doesnt make the snake move because pygame doesnot considers that an event if we have one keypressed for a long time
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                POS_X_CHANGE = 10
                POS_Y_CHANGE = 0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                POS_Y_CHANGE = -10
                POS_X_CHANGE = 0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                POS_Y_CHANGE = 10
                POS_X_CHANGE = 0

    POS_X+=POS_X_CHANGE
    POS_Y+=POS_Y_CHANGE
    # draw on the surface
    gameScreen.fill((176,176,255))
    # another way to fill the screen is using sprites(images)

    # another way to create shapes using fill function
    # gameScreen.fill(RED,rect=(50,100,20,20))
    # draw snake and snake's food
    snake=pygame.draw.rect(gameScreen,BLACK,(POS_X,POS_Y,10,10))
    # (x,y,width,height) coordinates of the rectangle

    # pygame.draw.rect(gameScreen,RED,(100,290,20,20))
    # (x,y,width,height) of rectangle

    clock.tick(30)
    # fps affects the processing speed

    # render the content
    pygame.display.update()
    # pygame.display.flip() alternate to update()

# unintitialize pygame and  all imported modules
pygame.quit()
quit() #exits python
