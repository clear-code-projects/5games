import pygame

# general setup to initialize pygame and make sure everything run well
# always include this
pygame.init()
# create screen with dimensions provided in variables (uppercase cause constants)
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True
# make code run until we want to close intentionally to open window
while running:
    # event loop
    for event in pygame.event.get():  # get events
        # check for ui, keyboard, mouse inputs
        if event.type == pygame.QUIT:  # QUIT = closing the game (a constant)
            running = False
    # draw the elements of the game 
    display_surface.fill("purple")
    # Take elements we run in while loop and draw them on the display surface
    pygame.display.update()  

# always write this after while loop- uninitializes everything 
pygame.quit()