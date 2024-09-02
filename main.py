import pygame 
import random

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

BIRD = pygame.image.load('bird.png')
PIPE = pygame.image.load('pipe.png')
BG = pygame.image.load('background.png')

bird_x, bird_y = 50, HEIGHT // 2
gravity = 0.5
bird_velocity = 0
pipe_gap = 150
pipe_velocity = 5

pipes = []
pipe_width = PIPE.get_width()
pipe_height = PIPE.get_height()

def draw_bird(x, y):
    win.blit(BIRD,(x,y))

def draw_pipes(pipes):
    for pipe in pipes:
        win.blit(PIPE, (pipe['x'], pipe['y']))    
        win.blit(pygame.transform.flip(PIPE, False, True), (pipe['x'], pipe['y']-pipe_gap-pipe_height))

def main():
    global bird_y, bird_velocity
    clock = pygame.time.Clock()
    run = True
    score = 0

    pipes.append({'x':WIDTH, 'y':random.randint(pipe_gap, HEIGHT - pipe_gap)})
    while run:
        clock.tick(30)
        win.blit(BG, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_velocity= -8

                        bird_velocity+= gravity
                        bird_y+=bird_velocity

                        for pipe in pipes:
                            pipe['x'] -= pipe_velocity

                        pipes = [pipe for pipe in pipes if pipe['x'] > -pipe_width]
                    if len(pipes) == 0 or pipes[-1]['x'] < WIDTH - 200:
                        pipes.append({'x': WIDTH, 'y': random.randint(pipe_gap, HEIGHT - pipe_gap)})

                    for pipe in pipes:
                        if bird_x + BIRD.get_width() > pipe['x'] and bird_x < pipe['x'] + pipe_width:
                            if bird_y < pipe['y'] - pipe_gap or bird_y + BIRD.get_height() > pipe['y']: run = False

                    draw_bird(bird_x,bird_y)
                    draw_pipes(pipes)
                    pygame.display.update()

                    if bird_y > HEIGHT or bird_y < 0:
                        run = False
                    pygame.quit()

                if __name__ == "__main__":
                    main()