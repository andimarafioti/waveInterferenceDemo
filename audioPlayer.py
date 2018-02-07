# coding: utf-8

import threading
import numpy as np
import pyaudio
import time

__author__ = 'Andres'


class AudioPlayer(object):
	def __init__(self, signal, sampling_rate, frames_per_buffer, channels):
		self._signal = signal
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format=pyaudio.paFloat32, channels=channels, rate=sampling_rate, output=True,
								frames_per_buffer=frames_per_buffer, stream_callback=self.callback, start=False)

	def callback(self, in_data, frame_count, time_info, status):
		data = self._signal.getBufferedSignal()
		return data.tostring(), pyaudio.paContinue

	def start(self):
		thread = threading.Thread(target=self._start)
		thread.daemon = True
		thread.start()

	def _start(self):
		self.stream.start_stream()
		while self.stream.is_active():
			time.sleep(0.1)

	def stop(self):
		self.stream.stop_stream()

	def exit(self):
		self.stream.close()
		self.p.terminate()
