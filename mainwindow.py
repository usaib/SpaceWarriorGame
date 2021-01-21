import pygame
from level1 import *
# activate the py game library
# initiate py game and give permission
# to use py game's functionality.
pygame.init()

# define the RGB value for white,
# green, blue colour .
white = (255, 255, 255)
green = (0, 155, 0)
blue = (0, 0, 128)
bg_open = pygame.image.load("background.jpg")
# assigning values to X and Y variable
X = 800
Y = 600

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))


# set the py game window name
pygame.display.set_caption('Space Invaders')

# create a font object.
# 1st parameter is the font file
# which is present in py game
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
play_game = font.render('Play Game', True, white, green)
instructions = font.render('Instruction', True, white, green)

# create a rectangular object for the
# text surface object
play_game_btn = play_game.get_rect()
instructions_btn = instructions.get_rect()
# set the center of the rectangular object.
play_game_btn.center = (390, 225)
instructions_btn.center = (390, 310)


def game_intro():
    display_surface.fill(white)
    display_surface.blit(bg_open, (0, 0))
    font = pygame.font.SysFont("comicsansms", 32)
    text = font.render("Space Invaders", True, (250, 0, 0))
    display_surface.blit(text, (280, 115))
    font = pygame.font.SysFont("comicsansms", 32)
    text = font.render("Press Space To Start", True, (0, 255, 0))
    display_surface.blit(text, (240, 240))
    font = pygame.font.SysFont("comicsansms", 32)
    text = font.render("Press ESC to Quit", True, (10, 200, 255))
    display_surface.blit(text, (255, 345))
    font = pygame.font.SysFont("comicsansms", 32)
    text = font.render("Press I for Instructions", True, (0,0,255))
    display_surface.blit(text, (223, 450))
    pygame.display.update()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    level1()
                if event.key == pygame.K_UP:
                    font = pygame.font.SysFont("comicsansms", 32)
                    text = font.render("If you ", True, (10,200,255))
                    display_surface.blit(text, (223, 450))
                    

                if event.key == pygame.K_ESCAPE or event.key == pygame.QUIT:
                    pygame.quit()
                    quit()
game_intro()
