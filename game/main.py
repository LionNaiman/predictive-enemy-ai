import pygame


# Window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (40, 40, 40)

# Player settings
PLAYER_SIZE = 30
PLAYER_COLOR = (0, 0, 255)
PLAYER_SPEED = 200  # Pixels per second

#enemy settings
ENEMY_SIZE = 40
ENEMY_COLOR = (255, 0, 0)


# Initialize Pygame and game state
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
player_x = (SCREEN_WIDTH - PLAYER_SIZE) / 2
player_y = (SCREEN_HEIGHT - PLAYER_SIZE) / 2
enemy_y= 100
enemy_x= (SCREEN_WIDTH - ENEMY_SIZE) / 2
direction = pygame.math.Vector2(0, 0)

while running: # a loop that continues until the user closes the window
    dt = clock.tick(FPS) / 1000.0 #a variable to keep track of the time between frames, which can be used for smooth movement and animations
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed() # Get the state of all keyboard buttons
    if keys[pygame.K_LEFT]: # If the left arrow key is pressed
        direction.x = -1 # Move left
    elif keys[pygame.K_RIGHT]: # If the right arrow key is pressed
        direction.x = 1 # Move right
    else:
        direction.x = 0 # Stop horizontal movement
    if keys[pygame.K_UP]: # If the up arrow key is pressed
        direction.y = -1 # Move up
    elif keys[pygame.K_DOWN]: # If the down arrow key is pressed
        direction.y = 1 # Move down
    else:
        direction.y = 0 # Stop vertical movement
    if direction.length() > 0: # If there is any movement
        direction = direction.normalize() # Normalize the direction vector to have a length of 1
    player_x += direction.x * PLAYER_SPEED * dt # Update the x position of the square based on the direction and speed
    player_y += direction.y * PLAYER_SPEED * dt # Update the y position of the square based on the direction and speed
    player_x = max(0, min(player_x, SCREEN_WIDTH - PLAYER_SIZE))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - PLAYER_SIZE))
    screen.fill(BACKGROUND_COLOR) # Fill the screen with a dark gray color
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)) # Draw the player on the screen
    pygame.draw.rect(screen, ENEMY_COLOR, (enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)) # Draw the enemy on the screen
    pygame.display.flip() # Update the display
    

pygame.quit()
