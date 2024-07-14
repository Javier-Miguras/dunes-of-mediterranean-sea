import pyxel
from lib import Sprite

class Background:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 2  # Velocidad de desplazamiento del fondo
        self.sprite_width = 248  # Ancho del sprite del fondo
        
        # Cargar sprite del fondo
        self.sprite = Sprite(0, 0, 0, self.sprite_width, 144, 3)

    def update(self, moving_right, near_level_end = False):
        if moving_right and not near_level_end:
            self.x = (self.x + self.speed) % self.sprite_width  # Desplazamiento del fondo

    def draw(self):
        # Dibujar el fondo con repetición
        part1_width = min(pyxel.width, self.sprite_width - self.x)
        part2_width = pyxel.width - part1_width
        
        pyxel.blt(0, 0, 0, self.x, 0, part1_width, pyxel.height, 3)
        if part2_width > 0:
            pyxel.blt(part1_width, 0, 0, 0, 0, part2_width, pyxel.height, 3)
