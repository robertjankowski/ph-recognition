import sys

from PyQt5 import Qt
from PyQt5 import uic
import pickle
import numpy as np

from untitled import Ui_Form


class override_graphicsScene (Qt.QGraphicsScene):
    def __init__(self, parent=None):
        super(override_graphicsScene, self).__init__(parent)
        self.load_model('saved_models\\29_datasets.pickle')

    def mousePressEvent(self, event):
        super(override_graphicsScene, self).mousePressEvent(event)
        p = event.pos()
        x = p.x
        y = p.y
        predict = self.predict(c_rgb[0], c_rgb[1], c_rgb[2])
        rgb = 'red: {}  green: {}  blue: {} --- prediction: {}'.format(
            c_rgb[0], c_rgb[1], c_rgb[2], predict)
        print(rgb)

    def load_model(self, name):
        with open(name, 'rb') as f:
            self.clf = pickle.load(f)

    def predict(self, r, g, b):
        predict_rgb = np.vstack([b, g, r]).T
        ph_predict = self.clf.predict(predict_rgb)
        return str(ph_predict).strip('[]')


class Image_Process(Qt.QWidget):
    def __init__(self):
        super(Image_Process, self).__init__()
        self.path = 'ph_datasets/test_ph.jpg'  # image path

        self.new = Ui_Form()
        self.new.setupUi(self)

        self.pixmap = Qt.QPixmap()
        self.pixmap.load(self.path)
        self.pixmap = self.pixmap.scaled(self.size(), Qt.Qt.KeepAspectRatio)

        self.graphicsPixmapItem = Qt.QGraphicsPixmapItem(self.pixmap)

        self.graphicsScene = override_graphicsScene(self)
        self.graphicsScene.addItem(self.graphicsPixmapItem)

        self.new.graphicsView.setScene(self.graphicsScene)


def main():
    a = Qt.QApplication(sys.argv)
    my_Qt_Program = Image_Process()
    my_Qt_Program.show()
    sys.exit(a.exec_())


if __name__ == '__main__':
    main()
