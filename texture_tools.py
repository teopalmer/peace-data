import cocos
from inventory import inv, MessageBox, ItemInv
from pyglet.window import mouse

# Объяевление кисоты как глобальной переменной
global acid

# Объявление словаря барьеров
barr = {"acid" : 1, "door" : 1, "key":1, "safe":1}

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
    def __init__(self,  xb, yb, pickurlb, xg, yg, pickurlg, name, scene):
        self.name = name
        self.xb = xb
        self.yb = yb
        self.pickurlb = pickurlb
        self.scene = scene
        self.xg = xg
        self.yg = yg
        self.pickurlg = pickurlg
        super().__init__()

        # Начальный объект
        self.obj_b = cocos.sprite.Sprite(pickurlb, anchor = (0, 0))
        self.obj_b.position = self.xb, self.yb
        self.add(self.obj_b)

        # Конечный объект
        self.obj_g = cocos.sprite.Sprite(pickurlg, anchor = (0, 0))
        self.obj_g.opacity = 0
        self.obj_g.position = self.xg, self.yg

        # Установка иерархии
        if self.name == 'safe':
            self.add(self.obj_g, z = -1)
        else:
            self.add(self.obj_g)

    def mouse_on_sprite(self, x, y):
        """Метод проверки курсора на попадание по объекту"""
        if (x < (self.obj_b.x + self.obj_b.width) and x > self.obj_b.x and y < (self.obj_b.y + self.obj_b.height) and y > self.obj_b.y):
            return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if self.mouse_on_sprite(x, y):
            if self.name == 'acid' and barr[self.name] == 1:
                if inv['scarf'] == 1:
                    self.delete_from_screen()
                    self.new_sprite()
                    barr[self.name] = 0
                    self.add(MessageBox("acid_scrf", 40, 400, 120))
                else:
                    self.add(MessageBox("no_scarf_warning", 40, 200, 120))
            if self.name == 'safe' and barr[self.name] == 1:
                if inv['paper'] == 1:
                    self.delete_from_screen()
                    self.new_sprite()
                    barr[self.name] = 0
                    barr['key'] = 0
                    self.add(MessageBox("safe_open", 40, 400, 120))
                    self.scene.add(ItemInv(1490, 200, "Resources/key.png", "key", 0.15))
                else:
                    self.add(MessageBox("safe", 40, 400, 120))

    def delete_from_screen(self):
        """Удаление картинки"""
        hide = cocos.actions.FadeOut(3)
        self.obj_b.do(hide)

    def new_sprite(self):
        """Проявление картинки"""
        show = cocos.actions.FadeIn(1)
        self.obj_g.do(show)

class MessageAcionLayer(cocos.layer.Layer):
    """
    Объект перехода на следующий уровень
    Направление: напрво
    """

    is_event_handler = True
    def __init__(self, x, y, texture, message, pos_x, pos_y, font_size):
        self.w = x
        self.h = y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.texture = texture
        self.message = message
        self.font_size = font_size
        self.flag = True
        super().__init__()

        # Загрузка и установка изображения
        self.obj = cocos.sprite.Sprite(self.texture, anchor = (0,0))
        self.obj.position = self.w, self.h
        self.add(self.obj)

    def mouse_on_sprite(self, x, y):
        """Метод проверки курсора на попадание по объекту"""
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        """Метод осуществления перехода к выбранной сцене"""
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x,y):
                self.add(MessageBox(self.message, self.font_size, self.pos_x, self.pos_y))
