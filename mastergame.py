import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Mastergame")

# Starthastighet
x_speed = 0
y_speed = 0

# Startposition
x = 250
y = 250

move_left = False
move_right = False
move_up = False
move_down = False

a_or_d = False
w_or_s = False
q_or_e = False

any_movement = x_speed or y_speed

# Add visual elements to the game

antal_studs = 0
studs = "Studs: " + str(antal_studs)

font = pygame.font.Font(None, 36)
text = font.render(studs, True, BLACK, WHITE)
textRect = text.get_rect()
print(textRect)
textRect.center = ((1000 - int(textRect[2])) // 2, (0 + int(textRect[3])) // 2)
 
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
            if event.key == pygame.K_q or event.key == pygame.K_e:
                q_or_e = True

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
            if event.key == pygame.K_q or event.key == pygame.K_e:
                q_or_e = False


   
    if move_left:
        x_speed = x_speed - 0.2
        if x_speed < -4:
            x_speed = -4
    if move_right:
        x_speed = x_speed + 0.2
        if x_speed > 4:
            x_speed = 4

    if move_up:
        y_speed = y_speed - 0.2
        if y_speed < -4:
            y_speed = -4
    if move_down:
        y_speed = y_speed + 0.2
        if y_speed > 4:
            y_speed = 4
        
            


    if a_or_d:
        x_speed = 0
    if w_or_s:
        y_speed = 0
    if q_or_e:
        x = 250
        y = 250

    # --- Game logic should go here
    
    y_speed = y_speed + 0.1

    if x <= 10 or x >= 490:
        x_speed = x_speed * -1
    if y <= 10:
        y_speed = y_speed * -1
    if y >= 490:
        y_speed = y_speed * 0.8
        y_speed = y_speed * -1

    

    x += x_speed
    y += y_speed
    antal_studs = antal_studs + 1
    studs = "Studs:" + str(antal_studs)
   
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    pygame.draw.circle(screen, BLUE, (x, y), 10)
    screen.blit(text, textRect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60 )
 
# Close the window and quit.
print("quitting...")
pygame.quit()