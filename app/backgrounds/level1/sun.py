import pyxel
from lib import Sprite

class Sun:
    def __init__(self):
        self.x = 64
        self.y = -6

        # Cargar sprites
        self.sprite_1 = Sprite(2, 0, 72, 89, 89, 3)  # Sprite para el salto
        self.sprite_2 = Sprite(2, 0, 168, 89, 89, 3)  # Sprite para el salto
        self.sprite = self.sprite_1

        #Temporizador para update
        self.t = 1
        #Veocidad update
        self.v = 4

    def update(self):

        if self.t % self.v == 0:

            if self.sprite == self.sprite_1:
                self.sprite = self.sprite_2
            else:
                self.sprite = self.sprite_1

        self.t += 1

    def draw(self):
        self.sprite.draw(self.x, self.y, False)