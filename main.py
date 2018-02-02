from PyQt4 import QtGui, QtCore
import sys
import numpy as np
import time
import pyqtgraph

from audioPlayer import AudioPlayer
from ui_main import InterferenceView

__author__ = 'Andres'


class InterferenceModel(object):
    def __init__(self):
        self._view = InterferenceView(self)

        self._sampling_rate = 44100
        self._frequencyOfFirstSignal = 440
        self._frequencyOfSecondSignal = 220
        self._lastTime = time.clock()
        self._timeCorrection = 1/1000

        self._countOfCycles = 2
        self._time = np.arange(0, self._countOfCycles
                               / np.math.gcd(self._frequencyOfFirstSignal, self._frequencyOfSecondSignal),
                               1 / self._sampling_rate)
        self._window_size = int(len(self._time)/self._countOfCycles)
        print(self._window_size)

        self._phaseOfFirstSignal = 0
        self._firstSignal = np.sin(2*np.pi*self._frequencyOfFirstSignal*self._time + self._phaseOfFirstSignal,
                                   dtype=np.float32)

        self._phaseOfSecondSignal = 0
        self._secondSignal = np.sin(2*np.pi*self._frequencyOfSecondSignal*self._time + self._phaseOfSecondSignal,
                                    dtype=np.float32)

        self._totalSignal = 0.05 * (self._firstSignal + self._secondSignal)

        self._audioPlayer = AudioPlayer(self._totalSignal, self._sampling_rate, self._window_size, 2)

    def hearSound(self, bool):
        if bool:
            self._audioPlayer.start()
        else:
            self._audioPlayer.stop()

    def show(self):
        self._view.show()

    def update(self):
        interval_shift = int(self._sampling_rate * self._lastTime * self._timeCorrection
                             % (len(self._totalSignal)-self._window_size))

        C = pyqtgraph.hsvColor(0.66, alpha=.5)
        pen = pyqtgraph.mkPen(width=10, color=C)
        self._view.grPlot.plot(self._time[interval_shift:interval_shift+self._window_size],
                               self._totalSignal[interval_shift:interval_shift+self._window_size], pen=pen, clear=True)
        self._lastTime = time.clock()

        QtCore.QTimer.singleShot(10, self.update)  # QUICKLY repeat


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = InterferenceModel()
    form.show()
    form.update()  # start with something
    app.exec_()


