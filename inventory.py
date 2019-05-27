import cocos
from cocos.director import director
from cocos.scenes import FadeTransition as animation
from pyglet.window import mouse

global inv
inv = {"scarf" : 0, "paper" : 0, "key" : 0}
global sms
sms = {
        "key_warning": "              Дверь, однако заперта!",
        "paper":"          Хммм, похоже на цифровой код...",
        "key" : "      Опять облом! Ну, хотя бы выберусь от сюда",
        "scarf" : "О, этот шарф может мне пригодиться, пожалуй заберу его",
        "scarf_warning" : "Ну и как я её починю? Может замотать её чем?",
        "lvl1" : 'Черт! *Звук закрытия двери*' + 'Этого еще не хватало',
        "mirror": 'Не время себя разглядывать!',
        "ward": ' Дёрну за крючок — стена отвалится',
        "locked": 'Походу закрыто...',
        "locked2": 'Заперто!',
        "bench": 'Сколько же ты повидала на своём веку...',
        "spider": 'Похоже мы тут одни, дружище',
        "boots": 'Не мой размерчик',
        "boots2": 'Да не, фигня какая-то',
        "otvertka": 'Ну и нафиг она мне сдалась?',
        "garbage_box": 'Не, ну это я точно руками трогать не буду',
        "plakat": 'Такс, шо тут у нас...',
        "resh": 'Кондиционер, трехкомнатный лофт — все как в сказке!',
        "acid_ac": 'Ну ёмаё! К лестнице не теперь подойти...',
        "safe": 'Опа, что же там такое? Может быть экзамен по проге?'}

class MessageBox(cocos.layer.Layer):
    """Всплывающие сообщения"""
    is_event_handler = True
    def __init__(self, name, size, w, h):
        self.w = w
        self.h = h
        self.flag = True
        self.name = name
        self.text = sms[self.name]
        self.size = size
        super().__init__()

        self.obj_c = cocos.sprite.Sprite("Resources/message_action.png", anchor=(0,0))
        self.obj_c.position = 170, 30
        self.obj = cocos.sprite.Sprite("Resources/message.png", anchor = (0, 0))
        self.obj.position = 170, 30
        self.add(self.obj)
        self.obj_label = cocos.text.Label(self.text, font_name = "Calibri", font_size = self.size)
        self.obj_label.position = self.w, self.h
        self.add(self.obj_label)

    def mouse_on_sprite(self, x, y):
        """Метод проверки курсора на попадание по объекту"""
        if (x < (self.obj_c.x + self.obj_c.width) and x > self.obj_c.x and y < (self.obj_c.y + self.obj_c.height) and y > self.obj_c.y):
            return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x, y) and self.flag:
                self.flag = False
                self.delete_from_screen()

    def delete_from_screen(self):
        hide = cocos.actions.FadeOut(1)
        self.obj.do(hide)
        self.obj_label.do(hide)
        self.obj_c.do(hide)
        self.kill(obj)

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
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x, y):
                inv[self.name] = 1
                self.delete_from_screen()
                self.add(MessageBox(self.name, 40, 300, 120))

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
