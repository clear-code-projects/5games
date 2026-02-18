import pygame

# initializing the pygame - essential for setup

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

while running:
    # event loop - UX packs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # this bit closes the window so running statement is important in this loop
    
    # draw the game
    # will take the elements in the event loop and display in the display surface
    display_surface.fill('pink')
    pygame.display.update() # update: updates the netire window  or flip: you can specify if you want to update a part of the window (less common)

# If not placed there can be anormalies with how the game runs -uninitializes

pygame.quit()
