# -*- utf-8 -*-
"""蜘蛛侠来了"""
from ddcmaker import __version__
from ddcmaker.linux.armv7l import get_equipment_type as ge
from ddcmaker.spider import Serial_Servo_Running as SSR

if ge.get_eq_type() == 3:
    class spider(object):
        def __init__(self):
            self.version = __version__
#----------------------------------------------------------------
        def creeping(self,step):
            SSR.run_ActionGroup('0', 1)
            print("蜘蛛匍匐")

        def creeping_forward(self, step):
            for i in range(step):
                SSR.run_ActionGroup('1', 1)
                print("蜘蛛匍匐前进")

        def creeping_backward(self, step):
            for i in range(step):
                SSR.run_ActionGroup('2', 1)
                print("蜘蛛匍匐后退")

        def creeping_left(self, step):
            for i in range(step):
                SSR.run_ActionGroup('3', 1)
                print("蜘蛛匍匐左转")

        def creeping_right(self, step):
            for i in range(step):
                SSR.run_ActionGroup('4', 1)
                print("蜘蛛匍匐右转")
#-----------------------------------------------------------------
        def stand(self,step):
            SSR.run_ActionGroup('25', 1)
            print("蜘蛛站立")

        def forward(self, step):
            for i in range(step):
                SSR.run_ActionGroup('26', 1)
                print("蜘蛛前进")

        def backward(self, step):
            for i in range(step):
                SSR.run_ActionGroup('27', 1)
                print("蜘蛛后退")

        def left(self, step):
            for i in range(step):
                SSR.run_ActionGroup('28', 1)
                print("蜘蛛左转")

        def right(self, step):
            for i in range(step):
                SSR.run_ActionGroup('29', 1)
                print("蜘蛛右转")
# -----------------------------------------------------------------

        def towering(self,step):
            SSR.run_ActionGroup('34', 1)
            print("蜘蛛耸立")

        def towering_forward(self, step):
            for i in range(step):
                SSR.run_ActionGroup('35', 1)
                print("蜘蛛耸立前进")

        def towering_backward(self, step):
            for i in range(step):
                SSR.run_ActionGroup('36', 1)
                print("蜘蛛耸立后退")

        def towering_left(self, step):
            for i in range(step):
                SSR.run_ActionGroup('37', 1)
                print("蜘蛛耸立左转")

        def towering_right(self,step):
            for i in range(step):
                SSR.run_ActionGroup('38', 1)
                print("蜘蛛耸立右转")

# -----------------------------------------------------------------

        def forward_flutter(self, step):
            for i in range(step):
                SSR.run_ActionGroup('5', 1)
                print("蜘蛛前扑")

        def backward_flutter(self, step):
            for i in range(step):
                SSR.run_ActionGroup('6', 1)
                print("蜘蛛后扑")

        def left_shift(self, step):
            for i in range(step):
                SSR.run_ActionGroup('7', 1)
                print("蜘蛛左移")

        def right_shift(self, step):
            for i in range(step):
                SSR.run_ActionGroup('8', 1)
                print("蜘蛛右移")

        def twisting(self,step):
            SSR.run_ActionGroup('9', 1)
            print("蜘蛛扭身")

        def fighting(self,step):
            SSR.run_ActionGroup('10', 1)
            print("蜘蛛战斗")

        def break_forward(self, step):
            for i in range(step):
                SSR.run_ActionGroup('41', 1)
                print("蜘蛛碎步前进")

        def minor_steering(self, step):
            for i in range(step):
                SSR.run_ActionGroup('40', 1)
                print("蜘蛛小转向(右)")



