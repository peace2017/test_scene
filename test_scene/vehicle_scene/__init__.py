import os
from PyQt5 import QtCore, QtWidgets
from test_scene.vehicle_scene.items.tractor import tractor


class VehicleScene(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kkargs):
        QtWidgets.QGraphicsScene.__init__(self, *args, **kkargs)

        self.rate = 30
        self.the = 90
        self.fi = 0
        self.fi_limit = 35
        self.vel = 0
        self.x = 0
        self.y = 0
        self.R = None

        self.params = {'rate': self.rate,
                       'the': self.the,
                       'fi': self.fi,
                       'fi_limit': self.fi_limit,
                       'vel': self.vel,
                       'x': self.x,
                       'y': self.y,
                       'R': self.R}

        self.path_tractor = os.path.join(
            os.path.split(tractor.__file__)[0], "tractor_no_wheels.jpg")

        self.tractor = tractor.Tractor(self, self.path_tractor, self.params)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_scene)
        self.timer.start(self.rate)

    def update_scene(self):
        for item in self.items():
            item.update()
        self.update_tractor_pos()

    def add_to_update(self, item):
        self.addItem(item)

    def update_tractor_pos(self):
        pos = self.tractor.model.get()

        self.tractor.setPos(pos['pos_x'], pos['pos_y'])
        self.tractor.setRotation(pos['the'] - 90)
        self.tractor.wheel_left.setRotation(-self.fi)
        self.tractor.wheel_right.setRotation(-self.fi)

    def move_right(self):
        if self.fi > -self.fi_limit:
            self.fi -= 1
            self.tractor.model.reduce_angle()

    def move_left(self):
        if self.fi < self.fi_limit:
            self.fi += 1
            self.tractor.model.increase_angle()

    def move_down(self):
        self.tractor.model.increase_speed()

    def move_up(self):
        self.tractor.model.reduce_speed()
