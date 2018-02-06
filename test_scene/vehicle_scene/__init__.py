from PyQt5 import QtCore, QtWidgets
from math import sin, cos, tan, pi
from test_scene.vehicle_scene.items.tractor import tractor
from test_scene.vehicle_scene.items.wheel_right import wheel_right
from test_scene.vehicle_scene.items.wheel_left import wheel_left
from test_scene.vehicle_scene.items.implement import implement


class VehicleScene(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kkargs):
        QtWidgets.QGraphicsScene.__init__(self, *args, **kkargs)
        self.update_list = []

        self.rate = 30
        self.the = 90
        self.fi = 0
        self.vel = 0
        self.x = 0
        self.y = 0
        self.R = 1000000

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_scene)
        self.timer.start(self.rate)

        self.tractor = tractor.Tractor(self)
        self.wheel_left = wheel_left.Wheel_left(self, self.tractor)
        self.wheel_right = wheel_right.Wheel_right(self, self.tractor)
        # self.implement = implement.Implement(self.tractor)
        # self.add_to_update(self.implement)

        self.H = self.tractor.boundingRect().height() * 0.15
        self.W = self.tractor.boundingRect().width() * 0.15

    def update_scene(self):
        for item in self.update_list:
            item.update()

        print('self.H = ', self.H)
        print('self.W = ', self.W)
        print('self.fi = ', self.fi)
        print('self.the = ', self.the)
        print('self.R = ', self.R)
        print("self.vel = ", self.vel)
        print('self.x = ', self.x)
        print('self.y = ', self.y)

        try:
            self.R = self.H / tan(self.fi * pi / 180)
        except ZeroDivisionError:
            self.R = None

        if self.R:
            self.the += (self.vel / self.rate / self.R) * 180 / pi

        self.x = self.tractor.pos().x() + \
                 self.vel / self.rate * cos(self.the * pi / 180)

        self.y = self.tractor.pos().y() + \
                      self.vel / self.rate * sin(self.the * pi / 180)

        self.tractor.setPos(self.x, self.y)
        self.tractor.setRotation(self.the - 90)
        # print('Trans1 = ', self.tractor.transformOriginPoint())

        # # self.tractor.setTransformOriginPoint(
        # #     -self.tractor.boundingRect().width() / 2 + self.R,
        # #     -self.tractor.boundingRect().height())

        # print('Trans2 = ', self.tractor.transformOriginPoint())
        # self.tractor.setOffset(
        #     -self.tractor.boundingRect().width() / 2 + self.R,
        #     -self.tractor.boundingRect().height())

    def add_to_update(self, item):
        print("item = ", item)
        self.addItem(item)
        self.update_list.append(item)

    def move_right(self):
        if self.fi > -35:
            self.fi -= 1
            self.wheel_left.setRotation(self.wheel_left.rotation() + 1)
            self.wheel_right.setRotation(self.wheel_right.rotation() + 1)
            # self.tractor.setRotation(self.tractor.rotation() + 1)
        else:
            pass

    def move_left(self):
        if self.fi < 35:
            self.fi += 1
            self.wheel_left.setRotation(self.wheel_left.rotation() - 1)
            self.wheel_right.setRotation(self.wheel_right.rotation() - 1)
            print('self.tractor.offset() = ', self.tractor.offset())
            # self.tractor.setRotation(self.tractor.rotation() - 1)
        else:
            pass

        # self.fi *= 3.14 / 180
        # self.the += self.fi
        # # self.the += self.vel * tan(self.fi) / self.H

        # print('left self.the = ', self.the)
        # print('left self.vel = ', self.vel)

        # # self.tractor.setOffset(0, 0)

        # self.tractor.setRotation(self.tractor.rotation() + self.fi * 180 / 3.14)

    def move_down(self):
        self.vel += 1

    def move_up(self):
        self.vel -= 1

    def get_center_scene(self, points):
        self.tractor.setPos(points.width() / 2, points.height() / 2)
        # self.implement.body.setPos(
        #     self.tractor.pos().x() / 2, self.tractor.pos().y() / 2)

        self.wheel_left.setPos(
            self.tractor.pos().x() - 695, self.tractor.pos().y() - 1150)

        self.wheel_right.setPos(
            self.tractor.pos().x() - 300, self.tractor.pos().y() - 1150)

        self.tractor.setScale(0.15)
