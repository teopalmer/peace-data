import cocos
from cocos.director import director
from pyglet.window import mouse
from cocos.scenes import FadeBLTransition as animation # Анимация переход
from cocos.scenes import FadeTransition as ending
from texture_tools import barr, MessageBox

class BtnLocker(cocos.layer.Layer):
    """
    Объект перехода на следующий уровень
    Направление: шкаф
    """
    is_event_handler = True
    def __init__(self, x, y, scene):
        self.w = x
        self.h = y
        self.scene = scene
        super().__init__()

        # Загрузка и установка изображения
        self.obj = cocos.sprite.Sprite("Resources/button_locker.png", anchor = (0,0), scale = 0.72)
        self.obj.position = self.w, self.h
        self.add(self.obj)

    def mouse_on_sprite(self, x, y):
        """Метод проверки курсора на попадание по объекту"""
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def on_mouse_motion(self, x, y, dx, dy):
        """Метод изменения курсора при наводке на объект"""
        if self.mouse_on_sprite(x, y):
            cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_DEFAULT)
            director.window.set_mouse_cursor(cursor)

    def on_mouse_press(self, x, y, button, modifiers):
        """Метод осуществления перехода к выбранной сцене"""
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x,y):
                director.replace(animation(self.scene, duration = 0.78))

class BtnLockerBack(cocos.layer.Layer):
    """
    Объект перехода на следующий уровень
    Направление: из шкафа
    """
    is_event_handler = True
    def __init__(self, x, y, scene):
        self.w = x
        self.h = y
        self.scene = scene
        super().__init__()

        # Загрузка и установка изображения
        self.obj = cocos.sprite.Sprite("Resources/arrow_down_from_locker3.png", anchor = (0,0), scale = 0.7)
        self.obj.position = self.w, self.h
        self.add(self.obj)

    def mouse_on_sprite(self, x, y):
        """Метод проверки курсора на попадание по объекту"""
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def on_mouse_motion(self, x, y, dx, dy):
        """Метод изменения курсора при наводке на объект"""
        if self.mouse_on_sprite(x, y):
            cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_DEFAULT)
            director.window.set_mouse_cursor(cursor)

    def on_mouse_press(self, x, y, button, modifiers):
        """Метод осуществления перехода к выбранной сцене"""
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x,y):
                director.replace(animation(self.scene, duration = 0.5))

class ArrowDown(cocos.layer.Layer):
    """
    Объект перехода на следующий уровень
    Направление: вниз
    """
    is_event_handler = True
    def __init__(self, x, y, scene):
        self.w = x
        self.h = y
        self.scene = scene
        super().__init__()

        # Загрузка и установка изображения
        self.obj = cocos.sprite.Sprite("Resources/arrow_down.png", anchor = (0,0))
        self.obj.position = self.w, self.h
        self.add(self.obj)

    def mouse_on_sprite(self, x, y):
        """Метод проверки курсора на попадание по объекту"""
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def on_mouse_motion(self, x, y, dx, dy):
        """Метод изменения курсора при наводке на объект"""
        if self.mouse_on_sprite(x, y):
            cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_DEFAULT)
            director.window.set_mouse_cursor(cursor)

    def on_mouse_press(self, x, y, button, modifiers):
        """Метод осуществления перехода к выбранной сцене"""
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x,y):
                director.replace(animation(self.scene, duration = 0.5))

class ArrowRight(cocos.layer.Layer):
    """
    Объект перехода на следующий уровень
    Направление: напрво
    """
    is_event_handler = True
    def __init__(self, x, y, scene):
        self.w = x
        self.h = y
        self.scene = scene
        super().__init__()

        # Загрузка и установка изображения
        self.obj = cocos.sprite.Sprite("Resources/arrow_right.png", anchor = (0,0))
        self.obj.position = self.w, self.h
        self.add(self.obj)

    def mouse_on_sprite(self, x, y):
        """Метод проверки курсора на попадание по объекту"""
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def on_mouse_motion(self, x, y, dx, dy):
        """Метод изменения курсора при наводке на объект"""
        if self.mouse_on_sprite(x, y):
            cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_DEFAULT)
            director.window.set_mouse_cursor(cursor)

    def on_mouse_press(self, x, y, button, modifiers):
        """Метод осуществления перехода к выбранной сцене"""
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x,y):
                if barr['acid'] == 0:
                    if barr['key'] == 0:
                        director.replace(ending(self.scene, duration = 2.5))
                    else:
                        self.add(MessageBox("key_warning", 40, 400, 120))
                else:
                    self.add(MessageBox("scarf_warning", 40, 400, 120))
class ArrowLeft(cocos.layer.Layer):
    """
    Объект перехода на следующий уровень
    Направление: влево
    """
    is_event_handler = True
    def __init__(self, x, y, scene):
        self.w = x
        self.h = y
        self.scene = scene
        super().__init__()

        # Загрузка и установка изображения
        self.obj = cocos.sprite.Sprite("Resources/arrow_left.png", anchor = (0,0))
        self.obj.position = self.w, self.h
        self.add(self.obj)

    def mouse_on_sprite(self, x, y):
        """Метод проверки курсора на попадание по объекту"""
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def on_mouse_motion(self, x, y, dx, dy):
        """Метод изменения курсора при наводке на объект"""
        if self.mouse_on_sprite(x, y):
            cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_DEFAULT)
            director.window.set_mouse_cursor(cursor)

    def on_mouse_press(self, x, y, button, modifiers):
        """Метод осуществления перехода к выбранной сцене"""
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x,y):
                director.replace(animation(self.scene, duration = 0.5))
