import cocos
from inventory import inv

global acid
barr = {"acid" : 1}

class StaticImage(cocos.sprite.Sprite):
    """Установка статического изображения по координатам"""
    def __init__(self, texture, w, h, scale):

        self.texture = texture
        self.w = w
        self.h = h

        super().__init__(self.texture)
        self.position = self.w, self.h
        self.scale = scale


class DinamicImage(cocos.layer.Layer):
    """Установка препятствий, для которых нужен предмет"""
    is_event_handler = True
    def __init__(self,  xb, yb, pickurlb, xg, yg, pickurlg, name):
        self.name = name
        self.xb = xb
        self.yb = yb
        self.pickurlb = pickurlb

        self.xg = xg
        self.yg = yg
        self.pickurlg = pickurlg
        super().__init__()

        self.obj_b = cocos.sprite.Sprite(pickurlb, anchor = (0, 0))
        self.obj_b.position = self.xb, self.yb
        self.add(self.obj_b)

        self.obj_g = cocos.sprite.Sprite(pickurlg, anchor = (0, 0))
        self.obj_g.opacity = 0
        self.obj_g.position = self.xg, self.yg
        self.add(self.obj_g)

    def mouse_on_sprite(self, x, y):
        if (x < (self.obj_b.x + self.obj_b.width) and x > self.obj_b.x and y < (self.obj_b.y + self.obj_b.height) and y > self.obj_b.y):
            return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if self.mouse_on_sprite(x, y):
            if self.name == 'acid' and barr[self.name] == 1:
                if inv['scarf'] == 1:
                    self.delete_from_screen()
                    self.new_sprite_pipe()
                    barr[self.name] = 0
                else:
                    """
                    Здесь должен быть код для окна сообщения
                    """

    def delete_from_screen(self):
        hide = cocos.actions.FadeOut(3)
        self.obj_b.do(hide)

    def new_sprite_pipe(self):
        show = cocos.actions.FadeIn(1)
        self.obj_g.do(show)
