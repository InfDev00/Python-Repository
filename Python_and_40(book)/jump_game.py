import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))


class Unit:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.isJump = False
        self.jumpCnt = 10

    def draw(self):
        return pygame.draw.rect(screen, self.color, (self.x, self.y, 40, 40))

    def move(self, speed):
        self.x = self.x - speed
        if self.x <= 0:
            self.x = MAX_WIDTH
        elif self.x >= MAX_WIDTH:
            self.x = 0


class Player(Unit):

    def jump(self):
        if self.isJump:
            if self.jumpCnt >= -10:
                neg = 1
                if self.jumpCnt < 0:
                    neg = -1
                self.y -= self.jumpCnt ** 2 * 0.7 * neg
                self.jumpCnt -= 1
            else:
                self.isJump = False
                self.jumpCnt = 10


class Enemy(Unit):
    pass


player = Player(50, MAX_HEIGHT - 40, (0, 0, 225))
enemy = Enemy(MAX_WIDTH, MAX_HEIGHT - 40, (0, 225, 0))


def main():
    enemy_speed = 5
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_speed = 7
        elif keys[pygame.K_RIGHT]:
            player_speed = -7
        else:
            player_speed = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.isJump = True

        clock.tick(FPS)
        screen.fill((255, 255, 255))

        player_rect = player.draw()
        player.jump()
        player.move(player_speed)

        enemy_rect = enemy.draw()
        enemy.move(enemy_speed)
        enemy_speed = enemy_speed + 0.01

        if player_rect.colliderect(enemy_rect):
            print("collide")
            pygame.quit()
            sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
