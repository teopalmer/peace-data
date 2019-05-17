import cocos
from cocos.director import director
from cocos.scenes import FlipX3DTransition # Анимация перехода
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
        director.replace(FlipX3DTransition(self.main_game_scene, duration = 2))

    def on_quit(self):
        """Выход"""
        director.window.close()

    def on_show_fps(self, show_fps):
        """Показать FPS"""
        director.show_FPS = show_fps