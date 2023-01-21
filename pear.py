import random
import arcade

class Pear(arcade.Sprite):
    def __init__(self, game):
        super().__init__("pear.png")
        self.width = 50
        self.height = 50
        self.center_x = random.randint(10, game.width-10)
        self.center_y = random.randint(10, game.height-10)
        self.change_x = 0
        self.change_y = 0

