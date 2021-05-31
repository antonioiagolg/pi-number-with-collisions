import pygame
from block import Block

class Main:
    def __init__(self):

        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MF', 30)
        self.screen = pygame.display.set_mode((800,600))
        self.bounce_count = 0
        self.pow_mass = 6
        self.time_steps = 30000

        mass_block1 = 1
        mass_block2 = mass_block1 * pow(100, self.pow_mass)

        self.block1 = Block(self.screen, 100, 20, 0, mass_block1, (0, 128, 255))
        self.block2 = Block(self.screen, 200, 150, -0.00005, mass_block2, (255, 100, 0))
        self.done = False
        
    
    def draw(self):

        for i in range(self.time_steps):
            if self.block1.hit_wall():
                self.block1.reverse()
                self.bounce_count = self.bounce_count + 1

            if self.block1.collide(self.block2):
                speed_block1 = self.block1.bounce(self.block2)
                speed_block2 = self.block2.bounce(self.block1)
                self.block1.speed = speed_block1
                self.block2.speed = speed_block2
                self.bounce_count = self.bounce_count + 1

            self.block1.update()
            self.block2.update()

        self.block1.draw()
        self.block2.draw()

    def start(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self.screen.fill((0, 0, 0))
            self.draw()
            pi_text = self.font.render(f"PI equals: {self.bounce_count}", False, (255,255,255))
            digits_text = self.font.render(f"Number of Digits after dot: {self.pow_mass}", False, (255,255,255))
            self.screen.blit(pi_text, (10,10))
            self.screen.blit(digits_text, (10,40))
            pygame.display.flip()
            self.clock.tick(144)

if __name__ == '__main__':
    Main().start()