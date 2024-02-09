import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'Score: {current_time}', False,("black"))
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rectangle)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Spongebob Runner")
clock = pygame.time.Clock()
font = pygame.font.Font("Font/Pixeltype.ttf", 50)
game_active = True
start_time = 0

background_surface = pygame.image.load("Graphics/Pineapple.jpg").convert()
background_surface = pygame.transform.scale(background_surface, (800,400))
ground_surface = pygame.image.load("Graphics/Floor1.png").convert_alpha()
ground_surface = pygame.transform.scale(ground_surface, (800,60))
# text_surface = font.render("Spongebob Dash", False, "#2112EC")
# score_rectangle = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load("Graphics/Snail.png").convert_alpha()
snail_surface = pygame.transform.scale(snail_surface, (40, 40))
snail_x_pos = 800
snail_rectangle = snail_surface.get_rect(midbottom = (snail_x_pos, 342))

player_surface = pygame.image.load("Graphics/Player/Standing.png").convert_alpha()
player_y_cor = 110
player_gravity = 0
player_surface = pygame.transform.scale(player_surface,(80, player_y_cor))
player_rectangle = player_surface.get_rect(midbottom = (80, 342))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom == 342:
                    player_gravity -= 7
                    player_rectangle.top += player_gravity
            if event.type == pygame.KEYDOWN and player_rectangle.bottom >= 342:
                if event.key == pygame.K_SPACE:
                    player_gravity -= 11
                    player_rectangle.top += player_gravity
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                player_rectangle.bottom = 342
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(background_surface, (0, -30))
        screen.blit(ground_surface, (0, 340))
        # pygame.draw.rect(screen, "yellow", score_rectangle, 0, 5)
        # pygame.draw.rect(screen, "yellow", score_rectangle, 15,5)


        snail_rectangle.left -= 4
        if snail_rectangle.right < -50:
            snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)

        #Player
        player_gravity += 0.4
        player_rectangle.bottom += player_gravity
        if player_rectangle.bottom > 342:
            player_rectangle.bottom = 342
            player_gravity = 0
        screen.blit(player_surface, player_rectangle)

        # Text
        # screen.blit(text_surface, score_rectangle)
        display_score()

        #collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill("black")



    pygame.display.update()
    clock.tick(60)


