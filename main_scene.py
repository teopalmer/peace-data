import menu
import cocos
from cocos.director import director
from pyglet.window import key, mouse
from cocos.scenes import FlipX3DTransition as animation # Анимация перехода
import pyglet

global storage
storage = int(1)

class Mover(cocos.actions.Move): 
    """Реализация движения объекта клавиатурой"""
    def step(self, dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 500
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 500
        self.target.velocity = (vel_x, vel_y)

class UFOLayer(cocos.layer.Layer): 
    """Анимированный объект"""
    is_event_handler = True
    def __init__(self):
        
        super().__init__()
        
        img = pyglet.image.load("Resources/animated_ufo.png")
        img_grid = pyglet.image.ImageGrid(img, 1, 12, item_width=260, item_height=67)

        animation = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1, loop=True)
        self.obj = cocos.sprite.Sprite(animation, anchor = (0, 0))
        self.obj.position = 960, 540
        self.obj.velocity = (0, 0)

        self.obj.do(Mover())
        self.add(self.obj)
    global storage
    storage = int(1)
    
    def mouse_on_sprite(self, x, y):
        """Проверка на попадание в хитбокс"""
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False
    def on_mouse_press(self, x, y, button, modifiers):
        """Нажание мышкой"""
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x, y):
                print("6opucoB JIox")

class Static_Image(cocos.sprite.Sprite):
    """Установка статичного изображения"""

    def __init__(self, texture, w, h):
        
        self.texture = texture
        self.w = w
        self.h = h
        
        super().__init__(self.texture)
        self.position = self.w, self.h

class CatLayer(cocos.layer.Layer):
    """Объект кот (тест)"""
    is_event_handler = True
    def __init__(self, xxx, yyy):
        self.xxx = xxx
        self.yyy = yyy
        super().__init__()
        
        self.obj = cocos.sprite.Sprite("Resources/barsik_r.png", anchor = (0, 0))
        self.obj.position = self.xxx, self.yyy

        self.add(self.obj, 0, 'cat0')
    
    def mouse_on_sprite(self, x, y):
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def move_left(self):
        global storage
        if storage == 1:
            move = cocos.actions.MoveTo((100, 1000), 7)
            storage += 1
        elif storage == 2:
            move = cocos.actions.MoveTo((250, 1000), 7)
            storage += 1
        else:
            move = cocos.actions.MoveBy((0, 0), 0)
        self.obj.do(move)
    
    def on_mouse_motion(self, x, y, dx, dy):
        if self.mouse_on_sprite(x, y):
            cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_DEFAULT)
            director.window.set_mouse_cursor(cursor)
    
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.mouse_on_sprite(x, y):
            self.obj.position = (x-self.obj.width//2, y-self.obj.height//2)
    
    def on_mouse_press(self, x, y, button, modifiers):
        if self.mouse_on_sprite(x, y):
            self.move_left()

class TransitionLayer(cocos.layer.Layer):
    """Объект перехода"""
    is_event_handler = True
    def __init__(self, xxx, yyy, level_2_scene):
        self.xxx = xxx
        self.yyy = yyy
        self.level_2_scene = level_2_scene
        super().__init__()
        
        self.obj = cocos.sprite.Sprite("Resources/to_level_2.png", anchor = (0, 0))
        self.obj.position = self.xxx, self.yyy
        self.add(self.obj)
    
    def mouse_on_sprite(self, x, y):
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False
    
    def on_mouse_motion(self, x, y, dx, dy):
        """При наведение курсора на объект"""

        if self.mouse_on_sprite(x, y):
            image = pyglet.image.load('Resources/tim_cursor.png')
            cursor = pyglet.window.ImageMouseCursor(image, 60, 89)
            director.window.set_mouse_cursor(cursor)
        else:
            cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_DEFAULT)
            director.window.set_mouse_cursor(cursor)
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button & mouse.LEFT:    
            if self.mouse_on_sprite(x,y):
                director.replace(animation(self.level_2_scene, duration = 2))
def lvl2(scene):
    transition = TransitionLayer(0, 1080/2, scene)
    background_layer = Static_Image("Resources/IMG_6205.PNG", 1920/2, 1080/2)
    test = cocos.scene.Scene()
    test.add(background_layer)
    test.add(transition)
    return test

if __name__ == '__main__':
    director.init(width=1920, height=1080, caption="Cocos test", autoscale=True, resizable=True)
    
    keyboard = key.KeyStateHandler() # Инициализация клавиатуры
    director.window.push_handlers(keyboard)
    
    
    """Инициализация объектов"""
    ufo = UFOLayer()
    cat = CatLayer(760, 330)
    cat2 = CatLayer(100, 330)
   
    background_layer = Static_Image("Resources/IMG_6219.PNG", 1920/2, 1080/2)

    """Инициализация сцен"""
    MAIN = cocos.scene.Scene()
    
    MAIN.add(background_layer, z=0)
    MAIN.add(cat, z=1)
    MAIN.add(cat2, z=2)
    MAIN.add(ufo, z=2)
    lvl_2_scene = lvl2(MAIN)
    transition = TransitionLayer(1920-150, 1080/2, lvl_2_scene)
    MAIN.add(transition)
    
    """Инициализация меню и основной сцены"""
    MENU = cocos.scene.Scene(menu.MainMenu(MAIN))
    director.run(MENU)
