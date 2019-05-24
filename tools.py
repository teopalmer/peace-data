import cocos
import menu
from cocos.director import director
from cocos.scenes import FlipX3DTransition as animation # Анимация перехода
class SetMenu(cocos.menu.Menu):
    is_event_handler = True
    def __init__(self,main_game_scene):
        self.main_game_scene = main_game_scene
        super().__init__("Peace Data quest") # Название 

        menus = []

        menus.append(cocos.menu.ToggleMenuItem("Показ FPS: ", self.on_show_fps, director.show_FPS)) # Пример переключателя
        menus[0].y = 80
        
        menus.append(cocos.menu.MenuItem("Выход из игры", self.on_quit))
        menus[1].y = 40

        menus.append(cocos.menu.MenuItem("Назад", self.on_back))
        menus[2].y = 20
        
        self.create_menu(menus, cocos.menu.shake(), cocos.menu.shake_back()) # Эффект встряхивания

    """Классы для взаимодействия с пунктами меню"""


    def on_quit(self):
        director.window.close()

    def on_show_fps(self, show_fps):
        director.show_FPS = show_fps
        
    def on_back(self):
        director.replace(animation(self.main_game_scene, duration = 2))
        
        
if __name__ == '__main__':
    director.init(width=1920, height=1080, caption="Cocos test", autoscale=True, resizable=True) # Инициализация директора (тест)
    director.window.pop_handlers() # Отключение дебаг функций
    
   
    test_scene = cocos.scene.Scene() # Тестовая сцена
    scene_box = cocos.scene.Scene()
    scene_set = cocos.scene.Scene()
    small_menu = menu.SmallMenu(scene_set,scene_box)
    test_scene.add(small_menu)
    scene_set.add(SetMenu(test_scene))

    director.run(test_scene) # Запуск сцены


