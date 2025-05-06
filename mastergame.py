import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 1500
screen_height = 750

size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Mastergame")

# Starthastighet
x_speed = 0
y_speed = 0

speed_max = 100
acceleration = 0.2  # +
retardation = 0.05   # -

# Startposition
x = 250
y = 250

move_left = False
move_right = False
move_up = False
move_down = False

a_or_d = False
w_or_s = False
key_e = False
key_q = False

# Add visual elements to the game

ball = pygame.sprite.Sprite()
ball.radius = 10

enemy_balls = pygame.sprite.Group()
enemy_ball_radius = 3
timer_enemy_ball = 0

antal_studs = 0
cornertext = "x: xxxx   y: yyy"

font = pygame.font.Font(pygame.font.match_font("courier"), 36)
text = font.render(cornertext, True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (screen_width - int(textRect[2]), (0 + int(textRect[3])))
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
is_running = True

# Functions
 
# -------- Main Program Loop -----------
while is_running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_a or event.key == pygame.K_d:
                a_or_d = True
            if event.key == pygame.K_w or event.key == pygame.K_s:
                w_or_s = True
            if event.key == pygame.K_q:
                key_q = True
            if event.key == pygame.K_e:
                key_e = True

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_a or event.key == pygame.K_d:
                a_or_d = False
            if event.key == pygame.K_w or event.key == pygame.K_s:
                w_or_s = False
            if event.key == pygame.K_q:
                key_q = False
            if event.key == pygame.K_e:
                key_e = False


   
    if move_left:
        x_speed = x_speed - acceleration
        if x_speed < -1 * speed_max:
            x_speed = -1 * speed_max 
    if move_right:
        x_speed = x_speed + acceleration
        if x_speed > speed_max:
            x_speed = speed_max

    if move_up:
        y_speed = y_speed - acceleration
        if y_speed < -1 * speed_max:
            y_speed = -1 * speed_max
    if move_down:
        y_speed = y_speed + acceleration
        if y_speed > speed_max:
            y_speed = speed_max
        

    if a_or_d:
        x_speed = 0
    if w_or_s:
        y_speed = 0
    if key_e:
        x = 250
        y = 250
        ball.radius = ball.radius + 1
    if key_q:
        ball.radius = ball.radius - 1

    # --- Game logic should go here
    

    if x + x_speed > screen_width - ball.radius:
        x = screen_width - ball.radius
        x_speed *= -1
        print("studs höger")

    if  x + x_speed < 0 + ball.radius:
        x = 0 + ball.radius
        x_speed *= -1
        print("studs vänster")


    if y + y_speed > screen_height - ball.radius:
        y = screen_height - ball.radius
        y_speed *= -1
        print("studs nere")

    if  y + y_speed < 0 + ball.radius:
        y = 0 + ball.radius
        y_speed *= -1
        print("studs uppe")


    x += x_speed
    if x_speed > 0 and move_right == False:
        if x_speed + retardation <= 0:
            x_speed = 0
        else:
            x_speed -= retardation
    if x_speed < 0 and move_left == False:
        if x_speed + retardation >= 0:
            x_speed = 0
        else:
            x_speed += retardation
            
    y += y_speed
    if y_speed > 0 and move_down == False:
        if y_speed + retardation <= 0:
            y_speed = 0
        else:
            y_speed -= retardation
    if y_speed < 0 and move_up == False:
        if y_speed + retardation >= 0:
            y_speed = 0
        else:
            y_speed += retardation

    '''

    timer_enemy_ball += 1

    if timer_enemy_ball == 100:
        timer_enemy_ball = 0
        
        enemy_ball_side = random.randint(1, 4)
        if enemy_ball_side == 1:
            enemy_ball = pygame.sprite.Sprite()
            enemy_ball_radius

    '''

    # Textwindows
    cornertext_x = str(int(x))
    cornertext_y = str(int(y))
    for i in range (4 - len(str(int(x)))):
        cornertext_x += " "
    for i in range (3 - len(str(int(y)))):
        cornertext_y += " "
    cornertext = "x: " + cornertext_x + "   y: " + cornertext_y
      
    text = font.render(cornertext, True, BLACK, WHITE)
   
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    pygame.draw.circle(screen, BLUE, (x, y), ball.radius)
    
    screen.blit(text, textRect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
print("quitting...")
pygame.quit()