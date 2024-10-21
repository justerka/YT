import pygame 


pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Yerassyl Game")


running = True
while running:
    
    screen.fill('white')
    square = pygame.draw.circle(screen,'red',(600,250),160)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()