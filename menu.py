import cocos
from cocos.director import director
from cocos.scenes import FadeTransition as animation

class MainMenu(cocos.menu.Menu):
    
    """Главное меню"""
    def __init__(self, main_game_scene):
        self.main_game_scene = main_game_scene

        super().__init__()

        menus = []

        menus.append(cocos.menu.MenuItem("                                                            ", self.on_new_game, ))
        menus[0].y = -50

        menus.append(cocos.menu.MenuItem("                                                            ", self.on_quit))
        menus[1].y = -450
        
        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back()) 

    """Методы для взаимодействия с пунктами меню"""

    def on_new_game(self): 
        """Загрузка новой игры"""
        director.replace(animation(self.main_game_scene, duration = 2.5))

    def on_quit(self):
        """Выход"""
        director.window.close()

class Settings(cocos.menu.Menu):
    def __init__(self, set_scene):
        self.set_scene = set_scene
        super().__init__()

        menus = []
        
        menus.append(cocos.menu.MenuItem("                                                           ", self.on_settings))
        menus[0].y = -320
        
        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back()) 

    """Методы для взаимодействия с пунктами меню"""

    def on_settings(self):
        director.replace(animation(self.set_scene, duration = 2.5))


