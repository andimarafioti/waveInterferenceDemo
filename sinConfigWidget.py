from PyQt4 import QtCore

from PyQt4.QtGui import QWidget, QGridLayout, QCheckBox, QLabel, QSlider

__author__ = 'Andres'


class SinConfigWidget(QWidget):
    def __init__(self, model, parent=None):
        super(SinConfigWidget, self).__init__(parent)
        self._model = model
        self.setupUi()

    def setupUi(self):
        self.setLayout(QGridLayout())

        self.activateButton = QCheckBox(self)
        self.activateButton.setEnabled(True)

        self.layout().addWidget(self.activateButton, 0, 0, 1, 1)

        sliderView = QWidget(self)
        sliderView.setLayout(QGridLayout())

        nameView = QLabel('frec')
        self.freqSlider = QSlider(QtCore.Qt.Horizontal)

        sliderView.layout().addWidget(nameView, 0, 0, 1, 1)
        sliderView.layout().addWidget(self.freqSlider, 0, 1, 1, 1)

        self.layout().addWidget(sliderView, 1, 0, 1, 1)
        self.phaseSlider = self._slider('phase')
        self.layout().addWidget(self.phaseSlider, 2, 0, 1, 1)

    def _slider(self, name):
        slider = QWidget(self)
        slider.setLayout(QGridLayout())

        nameView = QLabel(name)
        actualSlider = QSlider(QtCore.Qt.Horizontal)
        actualSlider.sliderMoved.connect(print)

        slider.layout().addWidget(nameView, 0, 0, 1, 1)
        slider.layout().addWidget(actualSlider, 0, 1, 1, 1)

        return slider

