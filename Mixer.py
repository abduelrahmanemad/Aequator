import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PyQt6 import QtGui, QtWidgets, QtCore
import pyqtgraph as pg

# from scipy.interpolate import CubicSpline
from Signal import Signal


class Channel(QtWidgets.QWidget):
    id = 0

    def __init__(self, name, *args, **kwargs):
        Channel.id += 1
        self.id = Channel.id
        self.name = name
        super(Channel, self).__init__(*args, **kwargs)
        self.layout = QtWidgets.QVBoxLayout()
        self.initialize_graph()

    def initialize_graph(self):
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground("w")
        self.graphWidget.setLabel("left", "Magnitude", fontsize=60)
        self.graphWidget.setLabel("bottom", "Frequency", fontsize=60)
        self.graphWidget.setTitle(self.name, fontsize=200)
        self.graphWidget.showGrid(x=True, y=True)
        # self.graphWidget.setMouseEnabled(x=False, y=False)
        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)
        self.graphWidget.setAutoVisible(x=True, y=True)
        # self.graphWidget.setXRange(0, 1)
        # self.graphWidget.setLimits(xMin=-.2, xMax=8.2)



class SamplingHandler:
    def __init__(self) -> None:
        self.signals = []
        self.channels = [
            Channel("Original signal and Sampled Points"),
            Channel("Recovered Signal"),
            Channel("Reconstruction Error"),
        ]

    def add_signal(self, sig) -> None:
        """
        Adds a signal to the mixer
        """
        self.signals.append(sig)

    def delete_signal(self, sig) -> None:
        self.signals.remove(sig)

    def get_signal_components(self, index: int) -> list:
        """
        Returns a list of components for a given signal
        """
        return self.signals[index].get_components()

    def get_signal(self, index: int) -> Signal:
        """
        Returns a signal at a given index
        """
        return self.signals[index]

    def get_signals(self) -> list:
        """
        Returns a list of signals
        """
        return self.signals

    def change_nq_rate(self, nq_rate, sig):
        sig.new_sampling_freq = nq_rate * sig.fmax

    def change_sampling_freq(self, freq, sig):
        sig.new_sampling_freq = freq

    def draw_signal(self, sig) -> None:
        if sig in self.signals:
            for channel in self.channels:
                channel.graphWidget.clear()

            index = self.signals.index(sig)

            if self.signals[index].SNR:
                self.signals[index].create_noise()
                self.signals[index].apply_noise()

            self.signals[index].sample_signal()
            print("Done First")
            sampled_points = self.signals[index].sampled_points
            print("Sampled")
            x_values, y_values_sampled = zip(*sampled_points)
            # recovered_points = self.signals[index].interpolate_signal_sinusoidal(self.signals[index].x, x_values, y_values_sampled)
            # recovered_points = sig.recovered_points
            # x, y_values_recovered = zip(*recovered_points)
            interpolate = sig.whittaker_shannon_interpolation(
                x_values, y_values_sampled, sig.x, 1 / sig.new_sampling_freq
            )
            print("Generated")
            self.channels[0].graphWidget.plot(
                self.signals[index].x,
                self.signals[index].y,
                pen="r",
            )
            sample_markers = pg.ScatterPlotItem(
                x=x_values,
                y=y_values_sampled,
                pen=None,
                symbol="x",
                symbolPen="b",
                name="sample_markers",
            )
            self.channels[0].graphWidget.addItem(sample_markers)
            self.channels[1].graphWidget.plot(sig.x, interpolate)
            error = np.array(self.signals[index].y) - interpolate
            self.channels[2].graphWidget.plot(sig.x, error, pen="r")
            self.channels[2].graphWidget.setYRange(-2, 2)
