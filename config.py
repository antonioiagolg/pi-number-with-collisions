class Config:
    def __init__(self):
        self.number_of_digits = 6
        self.timesteps = 30000
        self.mass_block1 = 1
        self.mass_block2 = self.mass_block1 * pow(100, self.number_of_digits - 1)
        self.framerate = 60

        # Colors
        self.blue_color = (0, 128, 255)
        self.orange_color = (255, 100, 0)
        self.white_color = (255,255,255)
