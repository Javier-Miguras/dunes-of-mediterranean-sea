import pyxel
from lib import Sprite

class Tree:
    def __init__(self):
        self.x = 64
        self.y = 98

        # Cargar sprites
        self.sprite = Sprite(2, 0, 0, 32, 32, 0)  # Sprite para el salto

    def update(self):
        pass

    def draw(self):
        self.sprite.draw(self.x, self.y, False)