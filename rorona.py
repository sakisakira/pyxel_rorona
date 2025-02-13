import pyxel
import color_palette

Screen = [240, 180]
Sprite = [32, 48]

FR0 = [1, 0]
FR1 = [1, 1]
FR2 = [2, 0]
FRW0 = [0, 0]
FRW1 = [0, 1]
RT0 = [3, 0]
RTW0 = [2, 1]
RTW1 = [3, 1]

class App:
    def __init__(self):
        pyxel.init(Screen[0], Screen[1], title="Rorona Test")
        self.init_color_palette()
        pyxel.images[0].load(0, 0, "sprites/rorona_study.png")
        self.x = (Screen[0] - Sprite[0]) / 2
        self.y = (Screen[1] - Sprite[1]) / 2
        self.tic = 0
        self.lx = self.x
        self.ly = self.y
        self.front = True
        self.back_start = 0
        self.tx = False
        self.ty = False
        pyxel.run(self.update, self.draw)

    def init_color_palette(self):
        colors = pyxel.colors.to_list()
        sprite_colors = color_palette.load()
        colors.extend(sprite_colors)
        pyxel.colors.from_list(colors)

    def update(self):
        self.movement()
        self.tic += 1
    
    def draw(self):
        pyxel.cls(1)
        self.disp_walking()

    def disp_walking(self):
        flip = 0
        if (self.tic % 30) < 15:
            sp_id = FR0
        else:
            sp_id = FR1
        pyxel.blt(self.x, self.y, 0, sp_id[0] * Sprite[0], sp_id[1] * Sprite[1], Sprite[0], Sprite[1], 0)

    def movement(self):
        if pyxel.btn(pyxel.KEY_LEFT): self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT): self.x += 1
        
App()
