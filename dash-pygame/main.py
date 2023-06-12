import pygame
from sys import exit



pygame.init() #starts executing

mongus = pygame.Color('#a3be8c')
screenlmao = pygame.display.set_mode((800, 400)) #sets window resolution

pygame.display.set_caption('DASH') #sets top title bar text

clock = pygame.time.Clock()
coolfont = pygame.font.Font('SFM/Pixeltype.ttf', 50)

#position_of_snail_x = 600
sky = pygame.image.load('SFM/Sky.png').convert()

ground = pygame.image.load('SFM/ground.png').convert()

textkek = coolfont.render('Score:', False, 'black')
text_rect = textkek.get_rect(center= (400, 50))

snail_surface = pygame.image.load('SFM/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('SFM/player_walk_1.png').convert_alpha()
player_rectangle = player_surf.get_rect(midbottom = (80, 300))





while True:
    for sex in pygame.event.get():
        if sex.type == pygame.QUIT:
            pygame.quit()
            exit()
        if sex.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(sex.pos):
                print("sexysex")
    # draw all elemement
    # update everything
    
    

    screenlmao.blit(sky, (0,0)) #location of surface
    screenlmao.blit(ground, (0,300)) #location of surface
    pygame.draw.rect(screenlmao,'Pink', text_rect)
    pygame.draw.rect(screenlmao,'Pink', text_rect,10)
    screenlmao.blit(textkek, text_rect)
    
    snail_rectangle.x -= 4
    if snail_rectangle.right < 0:
        snail_rectangle.left = 800;


    screenlmao.blit(snail_surface,snail_rectangle)
    screenlmao.blit(player_surf, player_rectangle)

    #player_rectangle.colliderect(snail_rectangle):
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60) 