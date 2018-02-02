import pyqtgraph
from PyQt4 import QtCore, QtGui
from pyqtgraph import PlotWidget

__author__ = 'Andres'


class InterferenceView(QtGui.QMainWindow):
    def __init__(self, model, parent=None):
        pyqtgraph.setConfigOption('background', 'w')  # before loading widget
        super(InterferenceView, self).__init__(parent)
        self._model = model
        self.setupUi(self)
        self.chkHearSound.clicked.connect(self._model.hearSound, self.chkHearSound.isChecked())
        self.grPlot.plotItem.showGrid(True, True, 0.7)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 650)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkHearSound = QtGui.QCheckBox(self.centralwidget)
        self.chkHearSound.setObjectName("chkMore")
        self.horizontalLayout.addWidget(self.chkHearSound)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.grPlot = PlotWidget(self.centralwidget)
        self.grPlot.hideAxis('bottom')
        self.grPlot.setObjectName("grPlot")
        self.verticalLayout.addWidget(self.grPlot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Interference")
        self.chkHearSound.setText("Hear")

