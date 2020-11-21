import pygame
import random 

# initialize pygame
pygame.init()

# create display and run update
display = pygame.display.set_mode((500, 500))

pygame.display.update()
pygame.display.set_caption("Jumper Game by Temirlan")

walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png')]
walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png')]
char = pygame.image.load('stand.png')
bg = pygame.image.load('back.jpg')
right_jump = pygame.image.load('Rjump2.png')
left_jump = pygame.image.load('Ljump2.jpg')
jump = pygame.image.load('jumping.png')
clock = pygame.time.Clock()
pygame.mixer.music.load('soundtrack_main.mp3')
pygame.mixer.music.set_volume(0.3)

x = 50
y = 425
width = 64
height = 64
vel = 9
left = False
right = False
walk_count = 0

def sound():
    sound.play()

def redrawGameWindow():
        global walk_count
        display.blit(bg, (0,0))
    
        if walk_count + 1 >= 27:
                walk_count = 0

        if left:
         display.blit(walk_left[walk_count // 10], (x, y))
         walk_count += 1
        elif right:
         display.blit(walk_right[walk_count // 10], (x, y))
         walk_count += 1
        else:
         display.blit(char, (x, y))
    
        pygame.display.update()

is_jump = False
jump_count = 10
pygame.mixer.music.play(loops = 1)
# start loop
game_end = False

while not game_end:
        clock.tick(27)
        #game loop
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
                game_end = True
        display.blit(bg, (0,0))

        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_LEFT] and x > vel:
         x -= vel
         left = True
         right = False 
        elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
         x += vel
         right = True
         left = False
        else:
         right = False
         left = False
         walk_count = 0
        if not (is_jump):
         if keys[pygame.K_SPACE]:
            is_jump = True
        else:
         if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg 
            jump_count -= 1
         else:
            is_jump = False
            jump_count = 10
        redrawGameWindow()

# close app, if required
pygame.quit()
quit()