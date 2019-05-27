import cocos
from cocos.director import director
from cocos.scenes import FadeTransition as animation
import texture_tools
from texture_tools import *

global inv
inv = {"scarf" : 0, "paper" : 0}

class Inventory(cocos.menu.Menu):

    def __init__(self,main_game_scene):

        self.main_game_scene = main_game_scene
        super().__init__()

        menus = []

        menus.append(cocos.menu.MenuItem("Назад", self.on_back))
        menus[0].x = 100
        menus[0].y = -450

        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back()) # Эффект встряхивания

    def on_back(self):
        director.replace(animation(self.main_game_scene, duration = 2))


class ItemInv(cocos.layer.Layer):
    """Предмет инвентаря"""
    is_event_handler = True
    def __init__(self, xxx, yyy, pickurl, name):
        self.name = name
        self.xxx = xxx
        self.yyy = yyy
        self.pickurl = pickurl
        super().__init__()

        self.obj = cocos.sprite.Sprite(pickurl, anchor = (0, 0))
        self.obj.position = self.xxx, self.yyy
        self.add(self.obj)

    def mouse_on_sprite(self, x, y):
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if self.mouse_on_sprite(x, y):
            inv[self.name] = 1
            self.delete_from_screen()
            self.add(MessageBox("scarf", 25))
            """Оконо сообщения о предмете"""

    def delete_from_screen(self):
        hide = cocos.actions.FadeOut(1)
        self.obj.do(hide)


class Naruto(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        self.x = 0
        self.y = 0
        self.count = 0
        self.pickurl = "Resources/Kakashi.png"

        super().__init__()

        white = cocos.sprite.Sprite("Resources/button_locker.png", anchor = (-1500, -600), opacity = 255)
        white.position = 300, 200
        self.obj = cocos.sprite.Sprite(self.pickurl, anchor = (-800, -150))
        self.obj.opacity = 0
        self.obj.scale = 0.8
        self.obj.position = self.x, self.y
        self.add(self.obj)

    def mouse_on_sprite(self, x, y):
        if (x < (self.obj.x + self.obj.width) and x > self.obj.x and y < (self.obj.y + self.obj.height) and y > self.obj.y):
            return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if self.mouse_on_sprite(x, y):
            #if self.count == 0:
            self.new_sprite_pipe()
            #self.count = 1

    def new_sprite_pipe(self):
        show = cocos.actions.FadeIn(0.3)
        self.obj.do(show)
