import pyqtgraph
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QSlider
from pyqtgraph import PlotWidget

from sinConfigWidget import SinConfigWidget

__author__ = 'Andres'


class InterferenceView(QtGui.QMainWindow):
    def __init__(self, model, parent=None):
        pyqtgraph.setConfigOption('background', 'w')  # before loading widget
        super(InterferenceView, self).__init__(parent)
        self._model = model
        self.setupUi()
        self.chkHearSound.clicked.connect(self._model.hearSound, self.chkHearSound.isChecked())
        self.grPlot.plotItem.showGrid(True, True, 0.7)

    def setupUi(self):
        self.showFullScreen()
        self.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(self)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)

        self.hearSoundLabel = QtGui.QLabel("Hear Sound")
        self.chkHearSound = QtGui.QCheckBox(self.centralwidget)

        self.speedSliderLabel = QtGui.QLabel("Sound Speed")
        speedSlider = QSlider(QtCore.Qt.Horizontal)
        speedSlider.setRange(-1, 6)
        # speedSlider.setTickInterval(0.00001)

        speedSlider.valueChanged.connect(self._model.setTimeCorrection)
        self.gridLayout.addWidget(self.hearSoundLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.chkHearSound, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.speedSliderLabel, 0, 2, 1, 1)
        self.gridLayout.addWidget(speedSlider, 0, 3, 1, 1)

        self.grPlot = PlotWidget(self.centralwidget)
        self.grPlot.hideAxis('bottom')
        self.gridLayout.addWidget(self.grPlot, 1, 0, 1, 4)
        self.setCentralWidget(self.centralwidget)

        self._firstSignalConfigWidget = SinConfigWidget(self)
        self._firstSignalConfigWidget.activateButton.stateChanged.connect(self._model.activateFirstSignal)
        self._firstSignalConfigWidget.freqSlider.onValueChangedCall(self._model.setFrequencyOfFirstSignal)
        self._firstSignalConfigWidget.phaseSlider.valueChanged.connect(self._model.setPhaseOfFirstSignal)

        self._secondSignalConfigWidget = SinConfigWidget(self)
        self._secondSignalConfigWidget.activateButton.stateChanged.connect(self._model.activateSecondSignal)
        self._secondSignalConfigWidget.freqSlider.onValueChangedCall(self._model.setFrequencyOfSecondSignal)
        self._secondSignalConfigWidget.phaseSlider.valueChanged.connect(self._model.setPhaseOfSecondSignal)

        self.gridLayout.addWidget(self._firstSignalConfigWidget, 2, 0, 1, 2)
        self.gridLayout.addWidget(self._secondSignalConfigWidget, 2, 2, 1, 2)

        self.updateGeometry()

        # self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(self)

    def setFirstSignalFreq(self, frequencyIndex):
        self._firstSignalConfigWidget.freqSlider.setValue(frequencyIndex+10)

    def setSecondSignalFreq(self, frequencyIndex):
        self._secondSignalConfigWidget.freqSlider.setValue(frequencyIndex+10)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Interference")
        self.chkHearSound.setText("Hear")
