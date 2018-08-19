from PyQt5.QtWidgets import *  # (QWidget, QMainWindow, QAction, QLabel, QFileDialog, QApplication)
from PyQt5.QtGui import *  # QIcon, QPixmap, QImage, QColor
from PyQt5.QtCore import *
import sys
import pickle
import numpy as np
from sklearn.externals import joblib


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('GUI pH')
        self.statusBar()

        self.label = QLabel(self.widget)
        self.img = QImage('ph_datasets/test_ph.jpg')
        pixmap = QPixmap(QPixmap.fromImage(self.img))
        self.resize(pixmap.width(), pixmap.height())
        self.label.setPixmap(pixmap)

        self.label.mousePressEvent = self.getPixel

        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        # self.setSizeConstraint()

        self.load_model('name')
        self.show()

    def showDialog(self):
        image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.jpg)")
        # update image -- to impove
        ##
        ##
        self.img = QImage(image[0])
        pix = QPixmap(QPixmap.fromImage(self.img))
        self.resize(pix.width(), pix.height())
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)

    def getPixel(self, event):
        x = event.x()
        y = event.y()
        c = self.img.pixel(x, y)
        c_rgb = QColor(c).getRgb()
        predict = self.predict(c_rgb[0], c_rgb[1], c_rgb[2])
        rgb = 'red: {}  green: {}  blue: {} --- prediction: {}'.format(
            c_rgb[0], c_rgb[1], c_rgb[2], predict)
        self.statusBar().showMessage(rgb)

    def load_model(self, name):
        name = "saved_models\\rnd_search_cv_82%.pkl"
        # name2 = "saved_models\\voting_clf-85.pkl"
        # name1 = "saved_models\\37_datasets.pickle"
        with open(name, 'rb') as f:
            self.clf = joblib.load(f)
            # self.clf = pickle.load(f)

    def predict(self, r, g, b):
        predict_rgb = np.vstack([b, g, r]).T
        ph_predict = self.clf.predict(predict_rgb)
        return str(ph_predict).strip('[]')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    qui = Gui()
    sys.exit(app.exec_())
