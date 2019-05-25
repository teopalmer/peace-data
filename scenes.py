import cocos
from texture_tools import StaticImage
import tools
import inventory

def lvl1_scene():
    """Создание игрового уровня №1"""

    Scene = cocos.scene.Scene()
    
    background_layer = StaticImage("Resources/IMG_0102.PNG", 1920/2, 1080/2)
    Scene.add(background_layer)
    
    return Scene

def lvl2_scene():
    """Создание игрового уровня №2"""

    Scene = cocos.scene.Scene()
    
    background_layer = StaticImage("Resources/IMG_0106.PNG", 1920/2, 1080/2)
    Scene.add(background_layer)
    
    return Scene

def lvl3_scene():
    """Создание игрового уровня №3"""

    Scene = cocos.scene.Scene()

    background_layer = StaticImage("Resources/IMG_0107.PNG", 1920/2, 1080/2)
    Scene.add(background_layer)
    
    return Scene

def final_scene():
    """Создание финального игрового уровня"""

    Scene = cocos.scene.Scene()

    label = cocos.text.Label("The end.", font_size=32, anchor_x="center", anchor_y="center")
    label.position = 1920/2, 1080/2
    Scene.add(label)
    
    return Scene
def box_scene(main):
    """Создание инвентаря"""
    Scene = cocos.scene.Scene()
    Scene.add(inventory.Inventory(main))
    return Scene
def set_scene(main):
    """Создание настроек"""
    Scene = cocos.scene.Scene()
    Scene.add(tools.SetMenu(main))
    return Scene
    
