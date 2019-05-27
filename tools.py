import cocos
import menu
import pygame
from cocos.director import director
from cocos.scenes import FadeTransition as animation

class SetMenu(cocos.menu.Menu):
    is_event_handler = True
    def __init__(self,main_game_scene):
        self.main_game_scene = main_game_scene
        super().__init__()
        menus = []

        menus.append(cocos.menu.MenuItem("Sound on", self.sound_on))
        menus[0].y = 70

        menus.append(cocos.menu.MenuItem("Sound off", self.sound_off))
        menus[1].y = 30

        menus.append(cocos.menu.ToggleMenuItem("Показ FPS: ", self.on_show_fps, director.show_FPS)) # Пример переключателя
        menus[2].y = 10

        menus.append(cocos.menu.MenuItem("Выход из игры", self.on_quit))
        menus[3].y = 0

        menus.append(cocos.menu.MenuItem("Назад", self.on_back))
        menus[4].y = -15


        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back()) # Эффект встряхивания

    """Классы для взаимодействия с пунктами меню"""


    def on_quit(self):
        director.window.close()

    def on_show_fps(self, show_fps):
        director.show_FPS = show_fps

    def sound_on(self):
        pygame.mixer.init(44100, -16,2,2048)
        pygame.mixer.music.load("Resources/s.mp3")
        pygame.mixer.music.play()
    def sound_off(self):
        pygame.mixer.music.stop()

    def on_back(self):
        director.replace(animation(self.main_game_scene, duration = 2))
