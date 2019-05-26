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
class DinamicImage():
    """Установка препятствий, для котрых нужен предмет"""
    def __init__(self, name, pickurl, x, y):

        self.texture = texture
        self.x = x
        self.y = y
        self.obj = cocos.sprite.Sprite(self.texture, self.x, self.y)
'''
