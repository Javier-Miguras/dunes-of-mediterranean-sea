import pyxel

class Tilemap:
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0
        self.speed = 2  # Velocidad de desplazamiento del tilemap
        self.tilemap = pyxel.tilemap(0)
        self.steps_counter = 0

    def is_tile_solid(self, x, y):
        tile_x = (x + self.offset_x) // 8
        tile_y = (y + self.offset_y) // 8  # Ajustamos aquí para dividir y por 8

        if 0 <= tile_x < self.tilemap.width and 0 <= tile_y < self.tilemap.height:
            tile = self.tilemap.pget(tile_x, tile_y)
            #print(tile)
            #print(f'Checking tile at ({tile_x}, {tile_y}): {tile}')  # Debug
            # Suponemos que el valor 2 indica que el tile es sólido, ajusta según tu diseño
            #return tile == 1
            if tile == (2,0):
                return True
            else:
                return False
        return False
    
    def level_end(self):
        if self.steps_counter >= 976:
            return True
        else:
            return False
    
    def update(self, moving_right):
        if moving_right:
            self.offset_x = (self.offset_x + self.speed) % (self.tilemap.width * 8)  # Ajusta según el tamaño de tu tilemap
            self.steps_counter += 1

    def draw(self):
        pyxel.bltm(0, 0, 0, self.offset_x, self.offset_y, pyxel.width, pyxel.height, colkey=3)
