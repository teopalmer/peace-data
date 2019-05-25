import cocos
from cocos.director import director
from cocos.scenes import FadeTransition as animation

class MainMenu(cocos.menu.Menu):
    """Главное меню"""
    def __init__(self, main_game_scene):
        self.main_game_scene = main_game_scene
        super().__init__("Peace Data quest")

        menus = []

        menus.append(cocos.menu.MenuItem("Новая игра", self.on_new_game)) 
        menus[0].y = 120 

        menus.append(cocos.menu.ToggleMenuItem("Показ FPS: ", self.on_show_fps, director.show_FPS)) 
        menus[1].y = 80
        
        menus.append(cocos.menu.MenuItem("Выход", self.on_quit))
        menus[2].y = 40
        
        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back()) 

    """Методы для взаимодействия с пунктами меню"""

    def on_new_game(self): 
        """Загрузка новой игры"""
        director.replace(animation(self.main_game_scene, duration = 2.5))

    def on_show_fps(self, show_fps):
        """Показать FPS"""
        director.show_FPS = show_fps

    def on_quit(self):
        """Выход"""
        director.window.close()