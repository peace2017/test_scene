#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
from PyQt5 import QtWidgets, QtCore
from test_scene import vehicle_scene

LOG = logging.getLogger(__name__)


class TestScene(QtWidgets.QGraphicsView):
    def __init__(self, *args, **kwargs):
        super(TestScene, self).__init__(*args, **kwargs)
        self.setSceneRect(
            -0, -0, 1000, 1000)
        self.kadabra = vehicle_scene.VehicleScene()
        self.setScene(self.kadabra)
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(
            QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(
            QtWidgets.QGraphicsView.AnchorViewCenter)

        self.kadabra.get_center_scene(self.sceneRect())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left:
            self.kadabra.move_left()
        elif event.key() == QtCore.Qt.Key_Right:
            self.kadabra.move_right()
        elif event.key() == QtCore.Qt.Key_Up:
            self.kadabra.move_up()
            # vel++
        elif event.key() == QtCore.Qt.Key_Down:
            self.kadabra.move_down()
            # vel--
        elif event.key() == QtCore.Qt.Key_Space:
            pass


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = TestScene()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
