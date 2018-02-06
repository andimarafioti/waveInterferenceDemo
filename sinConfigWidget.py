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

        self.activateLabel = QLabel("Activate Signal")
        self.layout().addWidget(self.activateLabel, 0, 0, 1, 1)

        self.activateButton = QCheckBox(self)
        self.activateButton.setChecked(True)

        self.layout().addWidget(self.activateButton, 0, 1, 1, 1)

        freqNameView = QLabel('frec')
        self.freqSlider = QSlider(QtCore.Qt.Horizontal)
        self.freqSlider.setRange(10, 19)
        self.freqSlider.setPageStep(2)
        self.freqSlider.setTickInterval(1)
        self.freqSlider.setTickPosition(QSlider.TicksBelow)

        phaseNameView = QLabel('phase')
        self.phaseSlider = QSlider(QtCore.Qt.Horizontal)
        self.phaseSlider.setRange(0, 8)
        self.phaseSlider.setPageStep(2)
        self.phaseSlider.setTickInterval(1)
        self.phaseSlider.setTickPosition(QSlider.TicksBelow)

        self.layout().addWidget(freqNameView, 1, 0, 1, 1)
        self.layout().addWidget(self.freqSlider, 1, 1, 1, 1)
        self.layout().addWidget(phaseNameView, 2, 0, 1, 1)
        self.layout().addWidget(self.phaseSlider, 2, 1, 1, 1)
