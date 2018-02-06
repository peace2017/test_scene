from PyQt5 import QtGui, QtWidgets
import logging
import os
from test_scene.vehicle_scene.items import tractor


LOG = logging.getLogger(__name__)


class Tractor(QtWidgets.QGraphicsPixmapItem):
    path = os.path.join(os.path.split(tractor.__file__)[0], "tractor_2.jpg")

    def __init__(self, scene):
        super(Tractor, self).__init__(QtGui.QPixmap(self.path))
        scene.add_to_update(self)

        self.setOffset(-self.boundingRect().width() / 2,
                       -self.boundingRect().height())


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
