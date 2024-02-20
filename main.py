import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CHAR_SIZE = 32
BLOCK_SIZE = 16  # Size of each block
# BLOCK_COLOR = (255, 255, 255)  # Color of the blocks

# Load the block image
block_image = pygame.image.load('Sunny-land-files/Sunny-land-files/Graphical Assets/environment/Props/block.png')
block_image = pygame.transform.scale(block_image, (BLOCK_SIZE, BLOCK_SIZE))
# Calculate the number of blocks that can fit horizontally on the screen
num_blocks_horizontal = SCREEN_WIDTH // BLOCK_SIZE

box_jump = pygame.image.load('Sunny-land-files/Sunny-land-files/Graphical Assets/environment/Props/crate.png')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

move_left = False
move_right = False
jump = False

y_gravity = 1
jump_height = 10
# y_speed = jump_height

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load('Sunny-land-files/Sunny-land-files/Graphical Assets/sprites/player/idle/player-idle-1.png')
        scaled_width = int(img.get_width() * scale)
        scaled_height = int(img.get_height() * scale)
        self.image = pygame.transform.scale(img, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.jump = False
        self.y_gravity = 1
        self.jump_height = 10
        self.y_speed = self.jump_height

    def movement(self, move_left, move_right, jump):
        change_x = 0
        change_y = 0

        if move_left:
            change_x = -self.speed
        if move_right:
            change_x = self.speed

        if jump and not self.jump:  # Check if not already jumping
            # print("Jumping")
            self.jump = True
            self.y_speed = self.jump_height

        if self.jump:  # If currently jumping
            # print("Jump Speed:", self.y_speed)
            change_y -= self.y_speed
            self.y_speed -= y_gravity
            self.rect.y += change_y
            if self.y_speed < -jump_height:  # Check if reached peak of jump
                self.jump = False
                self.y_speed = self.jump_height

        # if jump:
        #     change_y -= self.y_speed
        #     self.y_speed -= y_gravity
        #     self.rect.y += change_y
        #     if self.y_speed < -jump_height:
        #         self.jump = False
        #         self.y_speed = jump_height

        self.rect.x += change_x
        self.rect.y += change_y

    def draw(self):
        screen.blit(self.image, self.rect)

run = True

player = Character(400, SCREEN_HEIGHT-(BLOCK_SIZE+CHAR_SIZE), 2, 2)

box_x = 500
box_y = 530

while run:
    clock.tick(FPS)

    screen.fill((0, 0, 0))

    player.draw()

    player.movement(move_left, move_right, jump)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                jump = False

    screen.blit(box_jump, (box_x, box_y))

    if player.rect.colliderect(pygame.Rect(box_x, box_y, BLOCK_SIZE, BLOCK_SIZE)):
        # If collision detected and character is moving downwards (jumping)
        if player.y_speed >= 0:
            # Set character position to be on top of the box
            player.rect.bottom = box_y
            player.jump = False  # Stop the character from falling further

    for i in range(num_blocks_horizontal):
        screen.blit(block_image, (i * BLOCK_SIZE, SCREEN_HEIGHT - BLOCK_SIZE))

    pygame.display.update()

pygame.quit()
