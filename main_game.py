import menu
import transitions
import small_menu
from texture_tools import StaticImage, DinamicImage, MessageAcionLayer
from scenes import lvl1_scene, lvl1_locker, lvl1_empty_locker, lvl2_scene, lvl3_scene, final_scene
from scenes import box_scene, set_scene
import cocos
from cocos.director import director
from pyglet.window import mouse
import pyglet
from inventory import ItemInv, Naruto, MessageBox

if __name__ == '__main__':
    director.init(width=1920, height=1080, caption="Cocos test", autoscale=True, resizable=True)

    """Создание переходов и инициализация сцен"""
    lvl1 = lvl1_scene()
    lvl_locker = lvl1_locker()
    lvl_empty = lvl1_empty_locker()
    lvl3 = lvl3_scene()
    lvl2 = lvl2_scene()
    final = final_scene()

    """Инициализация меню основной сценой"""
    Menu = cocos.scene.Scene()
    background_layer = StaticImage("Resources/main_menu_bg.png", 1920/2, 1080/2, 1)
    set_m = set_scene(Menu)
    Menu.add(background_layer)
    Menu.add(menu.Settings(set_m))
    Menu.add(menu.MainMenu(lvl1))

    """Иницилизация сцен инвентаря и настроек"""
    set1 = set_scene(lvl1)
    box1 = box_scene(lvl1)
    small_menu_1 = small_menu.SmallMenu(set1,box1,Menu)

    set1 = set_scene(lvl_locker)
    box1 = box_scene(lvl_locker)
    small_menu_locker = small_menu.SmallMenu(set1,box1,Menu)

    set2 = set_scene(lvl2)
    box2 = box_scene(lvl2)
    small_menu_2 = small_menu.SmallMenu(set2,box2,Menu)

    set3 = set_scene(lvl3)
    box3 = box_scene(lvl3)
    small_menu_3 = small_menu.SmallMenu(set3,box3,Menu)

    #Переходы для 1 уровня
    lvl1_to_lvl2 = transitions.ArrowDown(787, 30, lvl2)
    lvl1_to_locker = transitions.BtnLocker(1432, 530, lvl_locker)
    lvl1_to_empty = transitions.BtnLocker(1600, 150, lvl_empty)

    #Переходы для уровня со шкафом
    locker_to_lvl1 = transitions.BtnLockerBack(880, 30, lvl1)
    locker_to_lvl11 = transitions.BtnLockerBack(830, 30, lvl1)
    empty_to_lvl1 = transitions.BtnLockerBack(880, 65, lvl1)
    empty_to_lvl11 = transitions.BtnLockerBack(830, 65, lvl1)

    #Переходы для 2 уровня
    lvl2_to_lvl1 = transitions.ArrowDown(695, 25, lvl1)
    lvl2_to_lvl3 = transitions.ArrowLeft(107, 257, lvl3)

    #Переходы для 3 уровня
    lvl3_to_lvl2 = transitions.ArrowDown(830, 57, lvl2)
    lvl3_to_final = transitions.ArrowRight(1111, 777, final)

    """Инициализация объектов"""
    # Взаимодействие с объектами 1 уровня
    bench = MessageAcionLayer(700, 280, "Resources/bench_action.png", "bench")
    ward = MessageAcionLayer(840, 782, "Resources/ward_action.png", "ward")
    locked = MessageAcionLayer(1460, 150, "Resources/locked_action.png", "locked")
    locked2 = MessageAcionLayer(1600, 420, "Resources/locked2_action.png", "locked2")
    mirror = MessageAcionLayer(0, 325, "Resources/mirror_action.png", "mirror")

    # Взаимодействие с объектами 2 уровня
    spider = MessageAcionLayer(415, 65, "Resources/spider_action.png", "spider")
    otvertka = MessageAcionLayer(1148, 764, "Resources/otvertka_action.png", "otvertka")
    boots = MessageAcionLayer(1130, 247, "Resources/boots_action.png", "boots")
    boots2 = MessageAcionLayer(1455, 595, "Resources/boots2_action.png", "boots2")
    garbage_box = MessageAcionLayer(1355, 33, "Resources/garbage_box_action.png", "garbage_box")
    plakat = MessageAcionLayer(700, 433, "Resources/plakat_action.png", "plakat")
    resh = MessageAcionLayer(315, 240, "Resources/resh_action.png", "resh")

    # Взаимодействие с объектами 3 уровня
    safe = MessageAcionLayer(1483, 163, "Resources/safe_action.png", "safe")
    acid_ac = MessageAcionLayer(300, 123, "Resources/acid_action.png", "acid_ac")
    

    scarf = ItemInv(560, 515, "Resources/scarf.png", "scarf")
    acid = DinamicImage(250, 95, "Resources/acid.png",
    410, 782, "Resources/Scarf_on_pipe.png", "acid")
    n = Naruto()
    message1 = MessageBox("lvl1", 40)

    """Заполнение сцен"""
    # Объекты для сцены (уровня) №1
    lvl1.add(scarf)
    lvl1.add(message1)
    lvl1.add(lvl1_to_locker)
    lvl1.add(lvl1_to_empty)
    lvl1.add(lvl1_to_lvl2)
    lvl1.add(small_menu_1)
    lvl1.add(bench) 
    lvl1.add(ward) 
    lvl1.add(locked)
    lvl1.add(locked2)
    lvl1.add(mirror)

    #Объекты для сцены (уровня) со шкафом
    lvl_locker.add(locker_to_lvl1)
    lvl_empty.add(n)
    lvl_empty.add(empty_to_lvl1)

    # Объекты для сцены (уровня) №2
    lvl2.add(lvl2_to_lvl1)
    lvl2.add(lvl2_to_lvl3)
    lvl2.add(small_menu_2)
    lvl2.add(spider)
    lvl2.add(otvertka)
    lvl2.add(boots) 
    lvl2.add(boots2)
    lvl2.add(garbage_box)
    lvl2.add(plakat)
    lvl2.add(resh) 

    # Объекты для сцены (уровня) №3
    lvl3.add(acid)
    lvl3.add(lvl3_to_lvl2)
    lvl3.add(lvl3_to_final)
    lvl3.add(small_menu_3)
    lvl3.add(safe)
    lvl3.add(acid_ac)
    
    """Запуск игры с главного меню"""
    director.run(Menu)
