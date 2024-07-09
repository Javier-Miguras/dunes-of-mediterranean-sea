import pyxel
from lib import Sprite

class Protagonist:
    def __init__(self):
        self.x = 35
        self.y = 54

        self.ground_y = self.y  # La posición y del suelo donde el protagonista aterriza
        self.vy = 0  # Velocidad vertical
        self.gravity = 0.5  # Gravedad que afecta al protagonista
        self.jump_strength = -6  # Fuerza del salto (negativo para subir)
        self.on_ground = True  # Indicador si está en el suelo
        
        # Cargar sprites
        self.sprite_1 = Sprite(1, 0, 0, 16, 16, 1)
        self.sprite_2 = Sprite(1, 16, 0, 16, 16, 1)
        self.sprite_3 = Sprite(1, 32, 0, 16, 16, 1)
        self.sprite = self.sprite_1
        
        # Velocidad del movimiento (pixeles por movimiento)
        self.speed = 4
        # Volteo del personaje
        self.flip_x = False
        
        # Variables para la animación de caminar
        self.walk_timer = 0
        self.walk_frame_duration = 3  # Duración de cada frame de la animación
        self.current_frame = 0  # Frame actual de la animación

    def update(self):
        # Caminar hacia adelante
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x + self.speed < pyxel.width - self.sprite.w:
                self.x += self.speed
            self.flip_x = False
            # Actualizar frame de caminar
            self.update_walk_animation()

        # Caminar hacia atrás
        elif pyxel.btn(pyxel.KEY_LEFT):
            if self.x - 2 >= 0:
                self.x -= self.speed
            self.flip_x = True
            # Actualizar frame de caminar
            self.update_walk_animation()

        # Personaje en reposo
        else:
            self.sprite = self.sprite_2
        # Saltar
        self.update_jump()

    def update_walk_animation(self):
        # Actualizar el temporizador
        self.walk_timer += 1

        # Cambiar de sprite cada cierto número de frames excepto cuando el personaje salta
        if self.y < 54:
            self.sprite = self.sprite_1
        else:
            if self.walk_timer >= self.walk_frame_duration:
                self.walk_timer = 0
                if self.current_frame == 0:
                    self.sprite = self.sprite_2
                    self.current_frame = 1
                elif self.current_frame == 1:
                    self.sprite = self.sprite_3
                    self.current_frame = 2
                else:
                    self.sprite = self.sprite_1
                    self.current_frame = 0

    def update_jump(self):
        # Iniciar el salto
        if pyxel.btnp(pyxel.KEY_UP) and self.on_ground:
            self.vy = self.jump_strength
            self.on_ground = False
            # Sprite para el salto
            #self.sprite = self.sprite_1

        # Aplicar la gravedad
        self.y += self.vy
        self.vy += self.gravity

        # Aterrizar en el suelo
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.vy = 0
            self.on_ground = True

    def draw(self):
        self.sprite.draw(self.x, self.y, self.flip_x)
