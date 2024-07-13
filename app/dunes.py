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

        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        self.protagonist.update(self.tilemap)

        self.sun.update()

        level_end = self.tilemap.level_end()

        #Acá se acaba el nivel, por lo cual se debe cortar la ejecución y mostrar una pantalla que diga "Level Finished" o algo así
        if level_end:
            print('Level End')

        # Actualizar el fondo si el protagonista está en el centro y moviendose a la derecha
        if self.protagonist.x >= pyxel.width / 2 - self.protagonist.sprite.w / 2 and pyxel.btn(pyxel.KEY_RIGHT):
            self.background.update(True)
            self.tilemap.update(True)
        else:
            self.background.update(False)
            self.tilemap.update(False)

    def draw(self):
        pyxel.cls(2)
        self.sun.draw()
        self.background.draw()
        self.protagonist.draw()
        self.tilemap.draw()

App()
