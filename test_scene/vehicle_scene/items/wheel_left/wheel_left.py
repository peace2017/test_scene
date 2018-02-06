#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtWidgets
import logging
import os
from test_scene.vehicle_scene.items import wheel_left


LOG = logging.getLogger(__name__)


class Wheel_left(QtWidgets.QGraphicsPixmapItem):
    path = os.path.join(
        os.path.split(wheel_left.__file__)[0], "wheel_left.jpg")

    def __init__(self, scene, parent):
        super(Wheel_left, self).__init__(QtGui.QPixmap(self.path), parent)
        scene.add_to_update(self)

        self.setOffset(-self.boundingRect().width() / 2,
                       -self.boundingRect().height() / 2)
