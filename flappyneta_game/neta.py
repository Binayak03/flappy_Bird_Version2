# import pygame
# from sys import exit
# import random

# GAME_WIDTH = 650
# GAME_HEIGHT = 850

# bird_X = GAME_WIDTH/8
# bird_y = GAME_HEIGHT/3
# bird_width = 110
# bird_height = 70



# class Bird(pygame.Rect):
#     def __init__(self, img):
#         pygame.Rect.__init__(self, bird_X, bird_y, bird_width, bird_height)
#         self.img = img

# # for pipe
# pipe_x = GAME_WIDTH
# pipe_y = 0
# pipe_width = 64
# pipe_height = 512


# class Pipe(pygame.Rect):
#     def __init__(self,img):
#         pygame.Rect.__init__(self, pipe_x, pipe_y, pipe_width, pipe_height)
#         self.img = img  
#         self.passed = False


# # # loading images
# # background_image = pygame.image.load("nepal_background.png").convert()
# # bird_image = pygame.image.load("flyNeta.png").convert_alpha()
# # bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))
# # top_pipe_image = pygame.image.load("toppipe.png").convert_alpha()
# # top_pipe_image = pygame.transform.scale(top_pipe_image, (pipe_width, pipe_height))
# # bottom_pipe_image = pygame.image.load("bottompipe.png").convert_alpha()
# # bottom_pipe_image = pygame.transform.scale(bottom_pipe_image, (pipe_width, pipe_height))
# pygame.init()

# window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
# pygame.display.set_caption("Neta Bhagau")
# clock = pygame.time.Clock()

# # NOW load and convert images
# background_image = pygame.image.load("nepal_background.png").convert()

# bird_image = pygame.image.load("flyNeta.png").convert_alpha()
# bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height)).convert_alpha()

# top_pipe_image = pygame.image.load("toppipe.png").convert_alpha()
# top_pipe_image = pygame.transform.scale(top_pipe_image, (pipe_width, pipe_height)).convert_alpha()

# bottom_pipe_image = pygame.image.load("bottompipe.png").convert_alpha()
# bottom_pipe_image = pygame.transform.scale(bottom_pipe_image, (pipe_width, pipe_height)).convert_alpha()




# # game logic
# bird = Bird(bird_image)
# pipes= []
# velocity_x = -2
# velocity_y = 0
# gravity = 0.4
# score = 0
# game_over = False


# def draw():
#     window.blit(background_image, (0, 0))
#     window.blit(bird.img, bird)

#     for pipe in pipes:
#         window.blit(pipe.img, pipe)

#     # score
#     text_str = str(int(score))
#     text_render = font_big.render(text_str, True, "white")
#     window.blit(text_render, (5, 0))

#     # game over message
#     if game_over:
#         go_text = "Game Over! Score: " + text_str
#         go_render = font_big.render(go_text, True, "white")
#         window.blit(go_render, (GAME_WIDTH/6, GAME_HEIGHT/2))


# # def draw():
# #     window.blit(background_image, (0,0))
# #     window.blit(bird.img, bird)
# #     for pipe in pipes:
# #         window.blit(pipe.img, pipe)
    
# #     text_str = str(int(score))
# #     font_big = pygame.font.SysFont("Comic Sans MS", 50)
# #     # text_render = text_font.render(text_str, True, "white")
# #     text_render = font_big.render(text_str, True, "white")

# #     window.blit(text_render, (5,0))
# #     if game_over:
# #         text_str = "Game Over! Score: " + text_str

# def move():
#     global velocity_y, score, game_over
#     velocity_y += gravity
#     bird.y += velocity_y
#     bird.y = max(bird.y, 0)

#     if bird.y > GAME_HEIGHT:
#         game_over = True
#         return


#     for pipe in pipes:
#         pipe.x += velocity_x
#         if not pipe.passed and bird.x > pipe.width + pipe.x:
#             score += 0.5
#             pipe.passed = True
#         if bird.colliderect(pipe):
#             game_over = True
#             return 
#     while len(pipes)>0 and pipes[0].x  < -pipe_width:
#         pipes.pop(0)



# def create_pipe():

#     random_y = pipe_y - pipe_height/4 - random.random()*(pipe_height/2)

#     opening_space = GAME_HEIGHT/4
#     top_pipe = Pipe(top_pipe_image)
#     top_pipe.y = random_y 
#     pipes.append(top_pipe)

#     bottom_pipe = Pipe(bottom_pipe_image)
#     bottom_pipe.y = top_pipe.y+ top_pipe.height + opening_space
#     pipes.append(bottom_pipe)
#     # print(len(pipes))


# pygame.init()
# window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
# pygame.display.set_caption("Neta Bhagau")
# clock = pygame.time.Clock()

# create_pipe_timer = pygame.USEREVENT +0
# pygame.time.set_timer(create_pipe_timer, 2500) #for 2.5 sse

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#         if event.type == create_pipe_timer and not game_over: 
#             create_pipe()
        
#         if event.type == pygame.KEYDOWN:
#             if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_x):
#                 velocity_y = -6

#                 if game_over:
#                     bird.y = bird_y
#                     pipes.clear()
#                     score= 0
#                     game_over = False
#     if not game_over:
#         move()
#         draw()
#         pygame.display.update()
#         clock.tick(60) #fps is 60


import pygame
from sys import exit
import random

GAME_WIDTH = 630
GAME_HEIGHT = 830

bird_X = GAME_WIDTH/8
bird_y = GAME_HEIGHT/3
bird_width = 110
bird_height = 70


class Bird(pygame.Rect):
    def __init__(self, img):
        super().__init__(bird_X, bird_y, bird_width, bird_height)
        self.img = img


pipe_x = GAME_WIDTH
pipe_y = 0
pipe_width = 64
pipe_height = 512


class Pipe(pygame.Rect):
    def __init__(self, img):
        super().__init__(pipe_x, pipe_y, pipe_width, pipe_height)
        self.img = img
        self.passed = False


 
# INIT & LOAD IMAGES


pygame.init()

pygame.mixer.init()

# Background Music (will loop forever)
pygame.mixer.music.load("flappyneta_game/modisong.mp3")
pygame.mixer.music.set_volume(0.4)

# Game Over Sound
game_over_sound = pygame.mixer.Sound("flappyneta_game/chancepayoki.mp3")
game_over_sound.set_volume(0.7)

window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Udyo Neta haha huhu ")
clock = pygame.time.Clock()
pygame.mixer.music.play(-1)   # -1 = loop forever

# Load + convert images
background_image = pygame.image.load("flappyneta_game/nepal_background.png").convert()

bird_image = pygame.image.load("flappyneta_game/flyNeta.png").convert_alpha()
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height)).convert_alpha()

top_pipe_image = pygame.image.load("flappyneta_game/toppipe.png").convert_alpha()
top_pipe_image = pygame.transform.scale(top_pipe_image, (pipe_width, pipe_height)).convert_alpha()

bottom_pipe_image = pygame.image.load("flappyneta_game/bottompipe.png").convert_alpha()
bottom_pipe_image = pygame.transform.scale(bottom_pipe_image, (pipe_width, pipe_height)).convert_alpha()

# Font (load once)
font_big = pygame.font.SysFont("Comic Sans MS", 50)


# ===================
# GAME LOGIC
# ===================

bird = Bird(bird_image)
pipes = []
velocity_x = -2
velocity_y = 0
gravity = 0.4
score = 0
game_over = False


def draw():
    window.blit(background_image, (0, 0))
    window.blit(bird.img, bird)

    for pipe in pipes:
        window.blit(pipe.img, pipe)

    # Score
    text_str = str(int(score))
    text_render = font_big.render(text_str, True, "white")
    window.blit(text_render, (5, 0))

    # Game Over
    if game_over:
        go_text = "Game Over! Score: " + text_str
        go_render = font_big.render(go_text, True, "white")
        window.blit(go_render, (GAME_WIDTH/6, GAME_HEIGHT/2))


def move():
    global velocity_y, score, game_over

    velocity_y += gravity
    bird.y += velocity_y
    bird.y = max(bird.y, 0)

    if bird.y > GAME_HEIGHT:
        if not game_over:
            game_over_sound.play()
            pygame.mixer.music.stop()
        game_over = True
        return

    for pipe in pipes:
        pipe.x += velocity_x

        if not pipe.passed and bird.x > pipe.x + pipe.width:
            score += 0.5
            pipe.passed = True

        if bird.colliderect(pipe):
            if not game_over:
                game_over_sound.play()
                pygame.mixer.music.stop()   # stop background music
            game_over = True
            return


    while pipes and pipes[0].x < -pipe_width:
        pipes.pop(0)


def create_pipe():
    random_y = pipe_y - pipe_height/4 - random.random() * (pipe_height/2)

    opening_space = GAME_HEIGHT / 4

    top_pipe = Pipe(top_pipe_image)
    top_pipe.y = random_y
    pipes.append(top_pipe)

    bottom_pipe = Pipe(bottom_pipe_image)
    bottom_pipe.y = top_pipe.y + top_pipe.height + opening_space
    pipes.append(bottom_pipe)


# Timer for pipes
create_pipe_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_pipe_timer, 2500)

# ===================
# GAME LOOP
# ===================

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == create_pipe_timer and not game_over:
            create_pipe()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_x):
                velocity_y = -6

                if game_over:
                    game_over_sound.stop()      # 🔥 stop game over sound immediately

                    bird.y = bird_y
                    pipes.clear()
                    score = 0
                    game_over = False
                    pygame.mixer.music.play(-1)   # restart background music


    # Move only when not game over
    if not game_over:
        move()

    # But draw ALWAYS
    draw()
    pygame.display.update()
    clock.tick(60)

