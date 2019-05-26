import cocos
from inventory import inv

class StaticImage(cocos.sprite.Sprite):
    """Установка статического изображения по координатам"""
    def __init__(self, texture, w, h):

        self.texture = texture
        self.w = w
        self.h = h

        super().__init__(self.texture)
        self.position = self.w, self.h
'''
class DinamicImage(cocos.layer.Layer):
    """Установка препятствий, для котрых нужен предмет"""
    is_event_handler = True
    def __init__(self, name, texture_bad, texture_good, xxx, yyy):

        self.name = name
        self.texture_bad = texture_bad
        self.texture_good = texture_good
        self.xxx = xxx
        self.yyy = yyy
        super().__init__()

        self.obj_bad = cocos.sprite.Sprite(self.texture_bad)
        self.obj_good = cocos.sprite.Sprite(self.texture_good)
        self.obj_bad.position = self.xxx, self.yyy
        self.obj_good.position = self.xxx, self.yyy
        self.obj_good.opacity = 255
        self.add(self.obj_bad)
        self.add(self.obj_good)

        def mouse_on_sprite(self, x, y):
            if (x < (self.obj_bad.x + self.obj_bad.width) and x > self.obj_bad.x and y < (self.obj_bad.y + self.obj_bad.height) and y > self.obj_bad.y):
                return True
            return False

        def on_mouse_press(self,name, x, y, button, modifiers):
            print('hui')
            if self.mouse_on_sprite(x, y):
                if self.name == 'acid':
                    print(inv, 'hui')
                    if inv['scarf'] == 1:
                        self.delete_from_screen()
                        self.new_sprite_pipe()
                    else:
                        """
                        Здесь должен быть код для окна сообщения
                        """
                print(inv)

        def delete_from_screen(self):
            hide = cocos.actions.FadeOut(3)
            self.obj_bad.do(hide)

        def new_sprite_pipe(self):
            show = cocos.actions.FadeIn(1)
            self.obj_good.do(show)
'''
class DinamicImage(cocos.layer.Layer):
    """Установка препятствий, для котрых нужен предмет"""
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
            if self.name == 'acid':
                if inv['scarf'] == 1:
                    self.delete_from_screen()
                    self.new_sprite_pipe()
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
