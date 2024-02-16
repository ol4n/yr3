import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

move_left = False
move_right = False
jump = False

# y_gravity = 1
# jump_height = 20
# y_speed = jump_height

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.load()
        self.image = pygame.transform.scale()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.y_gravity = 1
        self.jump_height = 20
        self.y_speed = self.jump_height

    def movement(self, move_left, move_right, jump):
        change_x = 0
        change_y = 0

        if move_left:
            change_x = -self.speed
        if move_right:
            change_y = self.speed
        # if jump:


        self.rect.x += change_x
        self.rect.y += change_y

    def draw(self):
        screen.blit(self.image, self.rect)

run = True

while run:
    clock.tick(FPS)

    screen.fill((0, 0, 0))

    player = Character(400, 0, 2, 1)

    player.draw()

    player.movement(move_left, move_right)
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
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False

    pygame.display.update()

pygame.quit()
