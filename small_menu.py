import cocos
import inventory
import tools
import menu
from cocos.director import director
from cocos.scenes import FadeTransition as animation

class SmallMenu(cocos.menu.Menu):
    is_event_handler = True
    def __init__(self, set_game_scene, box_game_scene, main_menu_scene):
        self.box_game_scene = box_game_scene
        self.set_game_scene = set_game_scene
        self.main_menu_scene = main_menu_scene

        super().__init__()

        menus = []

        menus.append(cocos.menu.ImageMenuItem("Resources/box.png", self.on_box))
        menus[0].x = 780
        menus[0].y = 450

        menus.append(cocos.menu.ImageMenuItem("Resources/set.png", self.on_settings))
        menus[1].x = 900
        menus[1].y = 490

        menus.append(cocos.menu.ImageMenuItem("Resources/main_menu.png", self.on_main_menu))
        menus[2].x = 840
        menus[2].y = 530

        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back())

    def on_box(self):
        director.replace(animation(self.box_game_scene, duration = 2))

    def on_settings(self):
        director.replace(animation(self.set_game_scene, duration = 2))
    def on_main_menu(self):
        director.replace(animation(self.main_menu_scene, duration = 2))