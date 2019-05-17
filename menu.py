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


if __name__ == '__main__':
    director.init(width=1280, height=720, caption="Peace Data menu test") # Инициализация директора (тест)
    director.window.pop_handlers() # Отключение дебаг функций
    
    menu = MainMenu() # Создание объекта "Меню"
    test_scene = cocos.scene.Scene() # Тестовая сцена
    test_scene.add(menu, z=0) # Добавление Меню на 0 слой

    director.run(test_scene) # Запуск сцены
