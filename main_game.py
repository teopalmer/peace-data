import menu
import transitions
import small_menu
from scenes import lvl1_scene, lvl2_scene, lvl3_scene, final_scene, box_scene,set_scene
import cocos
from cocos.director import director
from pyglet.window import key, mouse
import pyglet


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
    
    def mouse_on_sprite(self, x, y):
        """Проверка на попадание в хитбокс"""
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        """Нажатие мышкой"""
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x, y):
                print("Hi!")

if __name__ == '__main__':
    director.init(width=1920, height=1080, caption="Cocos test", autoscale=True, resizable=True)
    
    keyboard = key.KeyStateHandler() # Инициализация клавиатуры
    director.window.push_handlers(keyboard)
    
    """Инициализация объектов"""
    ufo = UFOLayer()

    """Создание переходов и инициализация сцен"""
    lvl1 = lvl1_scene()
    lvl3 = lvl3_scene()
    lvl2 = lvl2_scene()
    final = final_scene()
    
    
    """Инициализация меню основной сценой"""
    Menu = cocos.scene.Scene(menu.MainMenu(lvl1))
    set_m = set_scene(Menu)
    Menu.add(menu.Settings(set_m))

    """Иницилизация сцен инвентаря и настроек"""
    set1 = set_scene(lvl1)
    box1 = box_scene(lvl1)
    small_menu_1 = small_menu.SmallMenu(set1,box1,Menu)
    
    set2 = set_scene(lvl2)
    box2 = box_scene(lvl2)
    small_menu_2 = small_menu.SmallMenu(set2,box2,Menu)
    
    set3 = set_scene(lvl3)
    box3 = box_scene(lvl3)
    small_menu_3 = small_menu.SmallMenu(set3,box3,Menu)

    #Переходы для 1 уровня
    lvl1_to_lvl2 = transitions.ArrowDown(787, 30, lvl2)

    #Переходы для 2 уровня
    lvl2_to_lvl1 = transitions.ArrowDown(695, 25, lvl1)
    lvl2_to_lvl3 = transitions.ArrowLeft(107, 257, lvl3)

    #Переходы для 3 уровня
    lvl3_to_lvl2 = transitions.ArrowDown(830, 57, lvl2)
    lvl3_to_final = transitions.ArrowRight(1111, 777, final)

    
    """Заполнение сцен"""
    # Объекты для сцены (уровня) №1
    lvl1.add(ufo) 
    lvl1.add(lvl1_to_lvl2)
    lvl1.add(small_menu_1)
    
    # Объекты для сцены (уровня) №2
    lvl2.add(lvl2_to_lvl1)
    lvl2.add(lvl2_to_lvl3)
    lvl2.add(small_menu_2)
    

    # Объекты для сцены (уровня) №3
    lvl3.add(lvl3_to_lvl2)
    lvl3.add(lvl3_to_final)
    lvl3.add(small_menu_3)
    
    """Запуск игры с главного меню"""
    director.run(Menu)
