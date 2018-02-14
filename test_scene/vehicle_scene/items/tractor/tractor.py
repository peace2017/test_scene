from PyQt5 import QtGui, QtWidgets
import logging
import os
from test_scene.vehicle_scene.items.tractor import bicycle_model
from test_scene.vehicle_scene.items.tractor.wheel import wheel

LOG = logging.getLogger(__name__)


class Tractor(QtWidgets.QGraphicsPixmapItem):

    def __init__(self, scene, path, params):
        super(Tractor, self).__init__(QtGui.QPixmap(path))
        scene.add_to_update(self)

        self.setPos(scene.sceneRect().width() / 2,
                    scene.sceneRect().height() / 2)

        self.setOffset(-self.boundingRect().width() / 2,
                       -self.boundingRect().height())

        self.setScale(0.15)

        self.model = bicycle_model.Bicycle(
            frame_rate=params['rate'],
            angle_the=params['the'],
            angle_fi=params['fi'],
            angel_fi_limit=params['fi_limit'],
            velocity=params['vel'],
            pos_x=self.x(),
            pos_y=self.y(),
            R_curve=params['R'],
            H_base=self.boundingRect().height() * self.scale())

        self.path_wheel_left = os.path.join(
            os.path.split(wheel.__file__)[0], "wheel_left.jpg")
        self.path_wheel_right = os.path.join(
            os.path.split(wheel.__file__)[0], "wheel_right.jpg")

        self.wheel_left = wheel.Wheel(self.path_wheel_left, self)
        self.wheel_right = wheel.Wheel(self.path_wheel_right, self)

        self.wheel_left.setPos(
            -195, -self.boundingRect().height() / 2 - 180)
        self.wheel_right.setPos(
            200, -self.boundingRect().height() / 2 - 180)

    def increase_speed(self):
        self.model.increase_speed()

    def reduce_speed(self):
        self.model.reduce_speed()

    def increase_angle(self):
        self.model.increase_angle()

    def reduce_angle(self):
        self.model.reduce_angle()

    def update(self):
        self.model.update()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    scene = QtWidgets.QGraphicsScene()
    scene.setSceneRect(0, 0, 200, 200)
    Tractor(scene)
    view = QtWidgets.QGraphicsView()
    view.setScene(scene)
    view.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
