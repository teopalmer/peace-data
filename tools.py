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

        menus.append(cocos.menu.ToggleMenuItem("Показ FPS: ", self.on_show_fps, director.show_FPS)) # Пример переключателя
        menus[0].y = 80
        
        menus.append(cocos.menu.MenuItem("Выход из игры", self.on_quit))
        menus[1].y = 40

        menus.append(cocos.menu.MenuItem("Назад", self.on_back))
        menus[2].y = 20

        menus.append(cocos.menu.MenuItem("Sound on", self.sound_on))
        menus[3].y = 15

        menus.append(cocos.menu.MenuItem("Sound off", self.sound_off))
        menus[4].y = 10
        
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
        
        
if __name__ == '__main__':
    director.init(width=1920, height=1080, caption="Cocos test", autoscale=True, resizable=True) # Инициализация директора (тест)
    director.window.pop_handlers() 
    
   
    test_scene = cocos.scene.Scene() 
    scene_box = cocos.scene.Scene()
    scene_set = cocos.scene.Scene()
    small_menu = menu.SmallMenu(scene_set,scene_box)
    test_scene.add(small_menu)
    scene_set.add(SetMenu(test_scene))

    director.run(test_scene) 


