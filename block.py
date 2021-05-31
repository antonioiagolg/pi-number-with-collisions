import pygame
class Block:
    def __init__(self, screen, x, width, speed, mass, color):
        w, h = pygame.display.get_surface().get_size()
        ground_offset = 50

        self.screen = screen
        self.x = x
        self.y = h - ground_offset - width
        self.color = color
        self.width = width
        self.speed = speed
        self.mass = mass
    
    def update(self):
        self.x = self.x + self.speed
    
    def hit_wall(self):
        return self.x <= 0

    def reverse(self):
        self.speed = self.speed * -1
        
    def collide(self, other):
        return not ((self.x + self.width) < other.x) or ( self.x > (other.x + other.width))
    
    def bounce(self, other):
        sum_mass = self.mass + other.mass
        new_speed = self.speed * ((self.mass - other.mass)/sum_mass) + other.speed * ((2 * other.mass)/sum_mass)
        return new_speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.width))
