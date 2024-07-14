import pyxel
from lib import Sprite

class Protagonist:
    def __init__(self):
        self.x = 10
        self.y = 112
        self.ground_y = self.y
        self.vy = 0
        self.gravity = 0.5
        self.jump_strength = -6
        self.on_ground = True
        self.over_tile = False

        # Cargar sprites
        self.sprite_1 = Sprite(1, 0, 0, 16, 16, 1)
        self.sprite_2 = Sprite(1, 16, 0, 16, 16, 1)
        self.sprite_3 = Sprite(1, 32, 0, 16, 16, 1)
        self.sprite = self.sprite_2

        self.speed = 2
        self.flip_x = False

        self.walk_timer = 0
        self.walk_frame_duration = 3
        self.current_frame = 0

    def update(self, tilemap, walk_to_end = False):
        if pyxel.btnp(pyxel.KEY_UP) and (self.on_ground or self.over_tile):
            self.vy = self.jump_strength
            self.on_ground = False
            self.over_tile = False
            self.sprite = self.sprite_1

        self.y += self.vy
        self.vy += self.gravity

        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.vy = 0
            self.on_ground = True

        if pyxel.btn(pyxel.KEY_RIGHT):
            if(not walk_to_end):
                if self.x < pyxel.width / 2 - self.sprite.w / 2:
                    self.x += self.speed
            else:
                self.x += self.speed
            self.flip_x = False
            if self.on_ground or self.over_tile:
                self.update_walk_animation()

        elif pyxel.btn(pyxel.KEY_LEFT):
            if self.x > 0:
                self.x -= self.speed
            self.flip_x = True
            if self.on_ground or self.over_tile:
                self.update_walk_animation()

        if not pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_LEFT) and (self.on_ground or self.over_tile):
            self.sprite = self.sprite_2
            self.walk_timer = 0
            self.current_frame = 0

        self.check_collisions(tilemap)
        #print(self.over_tile)

    def update_walk_sprite(self):
        if self.sprite == self.sprite_1:
            self.sprite = self.sprite_2
        elif self.sprite == self.sprite_2:
            self.sprite = self.sprite_3
        else:
            self.sprite = self.sprite_1

    def update_walk_animation(self):
        self.walk_timer += 1
        if self.walk_timer >= self.walk_frame_duration:
            self.walk_timer = 0
            if self.current_frame == 0:
                self.update_walk_sprite()
            elif self.current_frame == 1:
                self.update_walk_sprite()
            else:
                self.update_walk_sprite()

    def check_collisions(self, tilemap):
        tile_width, tile_height = 8, 8
        # Check below the protagonist
        #print(self.on_ground)
        if not self.on_ground:
            # Calcula las coordenadas de los tiles debajo del protagonista
            tile_x = (self.x + self.sprite.w // 2) // tile_width
            tile_y = (self.y + self.sprite.h) // tile_height
            if tilemap.is_tile_solid(self.x + self.sprite.w // 2, self.y + self.sprite.h):
                self.y = (tile_y * tile_height) - self.sprite.h
                #self.ground_y = self.y
                self.vy = 0
                self.on_ground = False
                self.over_tile = True
            else:
                self.on_ground = False
                self.over_tile = False
                

        # Check above the protagonist
        if self.vy < 0:
            # Calcula las coordenadas de los tiles arriba del protagonista
            tile_x = (self.x + self.sprite.w // 2) // tile_width
            tile_y = self.y // tile_height
            if tilemap.is_tile_solid(self.x + self.sprite.w // 2, self.y):
                self.vy = 0
                self.y = (tile_y + 1) * tile_height

        # Check horizontal collisions
        self.check_horizontal_collisions(tilemap)

    def check_horizontal_collisions(self, tilemap):
        tile_width, tile_height = 8, 8
        # Check right side of the protagonist
        if self.flip_x == False and tilemap.is_tile_solid(self.x + self.sprite.w, self.y + self.sprite.h // 2):
            self.x = (self.x // tile_width) * tile_width
        # Check left side of the protagonist
        elif self.flip_x == True and tilemap.is_tile_solid(self.x, self.y + self.sprite.h // 2):
            self.x = (self.x // tile_width + 1) * tile_width

    def draw(self):
        self.sprite.draw(self.x, self.y, self.flip_x)
