import cocos
from cocos.director import director
from cocos.scenes import FlipX3DTransition as animation # Анимация перехода
class MainMenu(cocos.menu.Menu):
    
    def __init__(self, main_game_scene):
        self.main_game_scene = main_game_scene
        super().__init__("Peace Data quest") # Название 

        menus = []

        menus.append(cocos.menu.MenuItem("Новая игра", self.on_new_game)) # Пункт меню
        menus[0].y = 120 # Координата расположения

        menus.append(cocos.menu.ToggleMenuItem("Показ FPS: ", self.on_show_fps, director.show_FPS)) # Пример переключателя
        menus[1].y = 80
        
        menus.append(cocos.menu.MenuItem("Выход", self.on_quit))
        menus[2].y = 40
        
        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back()) # Эффект встряхивания

    """Классы для взаимодействия с пунктами меню"""

    def on_new_game(self): 
        """Здесь будет выполняться загрузка новой игры"""
        director.replace(animation(self.main_game_scene, duration = 2))

    def on_quit(self):
        """Выход"""
        director.window.close()

    def on_show_fps(self, show_fps):
        """Показать FPS"""
        director.show_FPS = show_fps
class SmallMenu(cocos.menu.Menu):
    is_event_handler = True
    def __init__(self, set_game_scene, box_game_scene):
        self.box_game_scene = box_game_scene
        self.set_game_scene = set_game_scene
        
        super().__init__() 

        menus = []

        menus.append(cocos.menu.ImageMenuItem("Resources/box.png", self.on_box)) # Пункт меню
        menus[0].x = 900
        menus[0].y = 470 # Координата расположения

        menus.append(cocos.menu.ImageMenuItem("Resources/set.png", self.on_settings)) # Пункт меню
        menus[1].x = 900
        menus[1].y = 420 # Координата расположения
        
        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back()) # Эффект встряхивания

    def on_box(self): 
        director.replace(animation(self.box_game_scene, duration = 2))

    def on_settings(self): 
        director.replace(animation(self.set_game_scene, duration = 2))
        
if __name__ == '__main__':
    director.init(width=1920, height=1080, caption="Cocos test", autoscale=True, resizable=True) # Инициализация директора (тест)
    director.window.pop_handlers() # Отключение дебаг функций
    
   
    test_scene = cocos.scene.Scene() # Тестовая сцена
    scene1 = cocos.scene.Scene()
    menu = MainMenu(scene1) # Создание объекта "Меню"
    small_menu = SmallMenu(scene1,scene1)
    test_scene.add(small_menu, z=0) 
    scene1.add(menu,z=0)

    director.run(test_scene) # Запуск сцены

