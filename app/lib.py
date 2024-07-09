import pyxel

class Sprite:
    def __init__(self, img_bank, u, v, w, h, transparent_color):
        self.img_bank = img_bank
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.transparent_color = transparent_color

    def draw(self, x, y, flip_x=False):
        if flip_x:
            pyxel.blt(x, y, self.img_bank, self.u, self.v, -self.w, self.h, self.transparent_color)
        else:
            pyxel.blt(x, y, self.img_bank, self.u, self.v, self.w, self.h, self.transparent_color)
