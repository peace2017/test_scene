
from PyQt5 import QtGui, QtWidgets, QtCore
import logging

LOG = logging.getLogger(__name__)


class Implement(QtWidgets.QGraphicsItemGroup):
    body_length = 500.0
    body_width = 50.0

    pen = QtGui.QPen()
    pen.setWidth(1)
    pen.setCosmetic(True)

    def __init__(self, parent):
        super(Implement, self).__init__()
        self.body = QtWidgets.QGraphicsRectItem(
            QtCore.QRectF(
                0,
                0,
                self.body_length,
                self.body_width),
            parent)

        self.body.setBrush(
            QtGui.QBrush(
                QtGui.QColor(QtCore.Qt.red)))
        self.body.setPen(self.pen)
