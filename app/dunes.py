import pyxel
from characters.protagonist import Protagonist
from backgrounds.level1.background import Background
from backgrounds.level1.sun import Sun
from tilemaps.tilemap import Tilemap

class App:
    def __init__(self):
        #extensión horizontal por nivel/tilemap 2048px, (0,63)
        pyxel.init(160, 144, title='Dunes Of Mediterranean Sea')
        pyxel.load('my_resource.pyxres')

        self.protagonist = Protagonist()
        self.background = Background()
        self.sun = Sun()
        self.tilemap = Tilemap()
        self.level_end = False
        self.level_width = 976
        self.walk_to_end = False

        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if(self.tilemap.steps_counter >= self.level_width):
            self.level_end = True

        if(self.tilemap.steps_counter >= self.level_width - (pyxel.width / 2)):
            self.walk_to_end = True

        self.protagonist.update(self.tilemap, self.walk_to_end)

        self.sun.update()

        # Actualizar el fondo si el protagonista está en el centro y moviendose a la derecha
        if self.protagonist.x >= pyxel.width / 2 - self.protagonist.sprite.w / 2 and pyxel.btn(pyxel.KEY_RIGHT):
            self.background.update(True, self.walk_to_end)
            self.tilemap.update(True, self.walk_to_end)
        else:
            self.background.update(False)
            self.tilemap.update(False)

    def draw(self):

        #Acá se acaba el nivel, por lo cual se debe cortar la ejecución y mostrar una pantalla que diga "Level Finished" o algo así
        if self.level_end:
            pyxel.cls(0)
            text = "Level Completed!"
            text_width = pyxel.FONT_WIDTH * len(text)
            text_height = pyxel.FONT_HEIGHT
            x = (pyxel.width - text_width) // 2
            y = (pyxel.height - text_height) // 2
            pyxel.text(x, y, text, 7)
        else:
            pyxel.cls(2)
            self.sun.draw()
            self.background.draw()
            self.protagonist.draw()
            self.tilemap.draw()

App()
