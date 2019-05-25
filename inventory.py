import cocos
from cocos.director import director
from cocos.scenes import FadeTransition as animation 
class Inventory(cocos.menu.Menu):

    def __init__(self,main_game_scene):

        self.main_game_scene = main_game_scene
        super().__init__("Peace Data quest") 

        menus = []

        menus.append(cocos.menu.MenuItem("Назад", self.on_back))
        menus[0].y = 40
        
        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back()) # Эффект встряхивания

    def on_back(self):
        director.replace(animation(self.main_game_scene, duration = 2))



