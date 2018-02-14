#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtWidgets
import logging
# from test_scene.vehicle_scene.items.tractor import wheel

LOG = logging.getLogger(__name__)


class Wheel(QtWidgets.QGraphicsPixmapItem):

    def __init__(self, path, parent):
        super(Wheel, self).__init__(QtGui.QPixmap(path), parent)
        # scene.add_to_update(self)

        self.setOffset(-self.boundingRect().width() / 2,
                       -self.boundingRect().height() / 2)
