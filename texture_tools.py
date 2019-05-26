import cocos

class StaticImage(cocos.sprite.Sprite):
    """Установка статического изображения по координатам"""
    def __init__(self, texture, w, h):

        self.texture = texture
        self.w = w
        self.h = h

        super().__init__(self.texture)
        self.position = self.w, self.h
