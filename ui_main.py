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
        self.resize(820, 650)
        self.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)

        speedSlider = QSlider(QtCore.Qt.Horizontal)
        speedSlider.valueChanged.connect(self._model.setTimeCorrection)
        self.verticalLayout.addWidget(speedSlider)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.chkHearSound = QtGui.QCheckBox(self.centralwidget)
        self.horizontalLayout.addWidget(self.chkHearSound)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.grPlot = PlotWidget(self.centralwidget)
        self.grPlot.hideAxis('bottom')
        self.verticalLayout.addWidget(self.grPlot)
        self.setCentralWidget(self.centralwidget)

        self._sinConfigWidget = SinConfigWidget(self)
        self._sinConfigWidget.freqSlider.valueChanged.connect(self._model.setFrequencyOfFirstSignal)
        self.verticalLayout.addWidget(self._sinConfigWidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Interference")
        self.chkHearSound.setText("Hear")
