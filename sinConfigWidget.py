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

        freqSliderView = QWidget(self)
        freqSliderView.setLayout(QGridLayout())

        freqNameView = QLabel('frec')
        self.freqSlider = QSlider(QtCore.Qt.Horizontal)
        self.freqSlider.setRange(10, 19)
        self.freqSlider.setPageStep(2)
        self.freqSlider.setTickInterval(1)
        self.freqSlider.setTickPosition(QSlider.TicksBelow)

        freqSliderView.layout().addWidget(freqNameView, 0, 0, 1, 1)
        freqSliderView.layout().addWidget(self.freqSlider, 0, 1, 1, 1)

        phaseSliderView = QWidget(self)
        phaseSliderView.setLayout(QGridLayout())

        phaseNameView = QLabel('phase')
        self.phaseSlider = QSlider(QtCore.Qt.Horizontal)

        phaseSliderView.layout().addWidget(phaseNameView, 0, 0, 1, 1)
        phaseSliderView.layout().addWidget(self.phaseSlider, 0, 1, 1, 1)

        self.layout().addWidget(freqSliderView, 1, 0, 1, 1)
        self.layout().addWidget(phaseSliderView, 2, 0, 1, 1)
