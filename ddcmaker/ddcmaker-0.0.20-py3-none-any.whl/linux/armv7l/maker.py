import subprocess
# from ddcmaker.car import __init__
# from ddcmaker.dog import __init__
# from ddcmaker.arm import __init__

from ddcmaker.linux.armv7l import get_equipment_type as ge
# from ddcmaker.human import __init__
# from ddcmaker.spider.__init__ import *
from ddcmaker.decorator.safety import parameter_checking, args_check


class author(object):
    def __init__(self):
        self.name = 'Bob He'
        self.age = 20
        self.projects = "Django_linux、Django-504、selenium_linux、Amazon-crawler、AIserver、Automated-cartography" \
                        "、ddcmaker、JIT、ddcmakerVirtual"
        self.github = "https://github.com/NocoldBob/robot"
        self.email = "fastbiubiu@163.com"

    def info(self):
        print("------------****author's information****-------------\n\nname:", self.name, "\nage:", self.age,
              "\nprojects:", self.projects, "\ngithub:", self.github,
              "\nemail:", self.email, "\n\n------------****author's information****-------------")


if ge.get_eq_type() == 0:
    from ddcmaker.human import robot
    from ddcmaker.pubulic import showlib

    Rb = robot.robot()
    Sh = showlib.showlib()


    class Robot(object):

        @staticmethod
        @args_check()
        def left(step=1):
            Rb.left(step)

        @staticmethod
        @args_check()
        def right(step=1):
            Rb.right(step)

        @staticmethod
        @args_check()
        def left_slide(step=1):
            Rb.left_slide(step)

        @staticmethod
        @args_check()
        def right_slide(step=1):
            Rb.right_slide(step)

        @staticmethod
        @args_check()
        def forward(step=1):
            Rb.forward(step)

        @staticmethod
        @args_check()
        def backward(step=1):
            Rb.backward(step)

        @staticmethod
        @args_check(attr_max=1)
        def up(step=1):
            Rb.up(step)

        @staticmethod
        @args_check(attr_max=1)
        def down(step=1):
            Rb.down(step)

        @staticmethod
        @args_check(attr_max=1)
        def check(step=1):
            Rb.check(step)

        @staticmethod
        @args_check()
        def nod(step=1):
            Rb.nod(step)

        @staticmethod
        @args_check()
        def shaking_head(step=1):
            Rb.shaking_head(step)

        '''虚不实真，苦切一除能，咒等等无是，咒上无是，咒明大是'''

        @staticmethod
        def hiphop():
            Sh.hiphop()

        @staticmethod
        def smallapple():
            Sh.smallapple()

        @staticmethod
        def jiangnanstyle():
            Sh.jiangnanstyle()

        @staticmethod
        def lasong():
            Sh.lasong()

        @staticmethod
        def feelgood():
            Sh.feelgood()

        '''无法兼容白色机器人，在调用时进行机器人判断'''

        @staticmethod
        def push_up():
            Rb.push_up()

        @staticmethod
        def abdominal_curl():
            Rb.abdominal_curl()

        @staticmethod
        def wave():
            Rb.wave()

        @staticmethod
        def bow():
            Rb.bow()

        @staticmethod
        def spread_wings():
            Rb.spread_wings()

        @staticmethod
        def haha():
            Rb.haha()

if ge.get_eq_type() == 1:
    from ddcmaker.car import car

    Ca = car.car()


    class Car(object):

        @staticmethod
        @args_check()
        def left(step=1, speed=50):
            Ca.left(step, speed)

        @staticmethod
        @args_check()
        def right(step=1, speed=50):
            Ca.right(step, speed)

        @staticmethod
        @args_check()
        def forward(step=1, speed=50):
            Ca.forward(step, speed)

        @staticmethod
        @args_check()
        def backward(step=1, speed=50):
            Ca.backward(step, speed)

        @staticmethod
        def stop():
            Ca.stop(0)
if ge.get_eq_type() == 2:

    from ddcmaker.human_code import whiterobot
    from ddcmaker.pubulic import showlib

    Rb = whiterobot.robot()
    Sh = showlib.showlib()


    class Robot(object):

        @staticmethod
        @args_check()
        def left(step=1):
            Rb.left(step)

        @staticmethod
        @args_check()
        def right(step=1):
            Rb.right(step)

        @staticmethod
        @args_check()
        def left_slide(step=1):
            Rb.left_slide(step)

        @staticmethod
        @args_check()
        def right_slide(step=1):
            Rb.right_slide(step)

        @staticmethod
        @args_check()
        def forward(step=1):
            Rb.forward(step)

        @staticmethod
        @args_check()
        def backward(step=1):
            Rb.backward(step)

        @staticmethod
        @args_check(attr_max=1)
        def up(step=1):
            Rb.up(step)

        @staticmethod
        @args_check(attr_max=1)
        def down(step=1):
            Rb.down(step)

        @staticmethod
        @args_check(attr_max=1)
        def check(step=1):
            Rb.check(step)

        @staticmethod
        @args_check()
        def nod(step=1):
            Rb.nod(step)

        @staticmethod
        @args_check()
        def shaking_head(step=1):
            Rb.shaking_head(step)

        '''虚不实真，苦切一除能，咒等等无是，咒上无是，咒明大是'''

        @staticmethod
        def jiangnanstyle():
            Sh.jiangnanstyle()

        @staticmethod
        def smallapple():
            Sh.smallapple()

        @staticmethod
        def lasong():
            Sh.lasong()

        @staticmethod
        def feelgood():
            Sh.feelgood()

        @staticmethod
        def fantastic_baby():
            Sh.fantastic_baby()

        @staticmethod
        def super_champion():
            Sh.super_champion()

        @staticmethod
        def youth_cultivation():
            Sh.youth_cultivation()

        @staticmethod
        def love_starts():
            Sh.Love_starts()

        @staticmethod
        def push_up():
            Rb.push_up()

        @staticmethod
        def abdominal_curl():
            Rb.abdominal_curl()

        @staticmethod
        def wave():
            Rb.wave()

        @staticmethod
        def bow():
            Rb.bow()

        @staticmethod
        def spread_wings():
            Rb.spread_wings()

        @staticmethod
        def straight_boxing():
            Rb.straight_boxing()

        @staticmethod
        def lower_hook_combo():
            Rb.lower_hook_combo()

        @staticmethod
        def left_hook():
            Rb.left_hook()

        @staticmethod
        def right_hook():
            Rb.right_hook()

        @staticmethod
        def punching():
            Rb.punching()

        @staticmethod
        def crouching():
            Rb.crouching()

        @staticmethod
        def yongchun():
            Rb.yongchun()

        @staticmethod
        def beat_chest():
            Rb.beat_chest()

        @staticmethod
        def left_side_kick():
            Rb.left_side_kick()

        @staticmethod
        def right_side_kick():
            Rb.right_side_kick()

        @staticmethod
        def left_foot_shot():
            Rb.left_foot_shot()

        @staticmethod
        def right_foot_shot():
            Rb.right_foot_shot()

        @staticmethod
        def show_poss():
            Rb.show_poss()

        @staticmethod
        def inverted_standing():
            Rb.inverted_standing()

        @staticmethod
        def rear_stand_up():
            Rb.rear_stand_up()
