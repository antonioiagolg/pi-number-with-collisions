import pygame
from config import Config
from block import Block

class Main:
    def __init__(self, config):

        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MF', 30)
        self.screen = pygame.display.set_mode((800,600))
        self.bounce_count = 0
        self.config = config
        

        self.block1 = Block(self.screen, 100, 20, 0, self.config.mass_block1, config.blue_color)
        self.block2 = Block(self.screen, 200, 150, -0.00005, self.config.mass_block2, config.orange_color)
        self.done = False
        
    
    def draw(self):

        for i in range(self.config.timesteps):
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
    
    def show_GUI(self):
        pi_text = self.font.render(f"PI equals: {self.bounce_count}", False, self.config.white_color)
        digits_text = self.font.render(f"Number of Digits: {self.config.number_of_digits}", False, self.config.white_color)
        self.screen.blit(pi_text, (10,10))
        self.screen.blit(digits_text, (10,40))

    def start(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self.screen.fill((0, 0, 0))
            self.draw()
            self.show_GUI()
            pygame.display.flip()
            self.clock.tick(self.config.framerate)


if __name__ == '__main__':
    Main(Config()).start()