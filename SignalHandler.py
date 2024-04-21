import typing
from PyQt6 import QtGui, QtWidgets, QtCore
from numpy import sign
import pyqtgraph as pg
from PyQt6.QtCore import Qt
import os
import time
import numpy as np
from itertools import chain
import pyqtgraph.exporters


class SignalHandler(QtWidgets.QWidget):
    id = 0

    def __init__(self, name, signals: list, *args, **kwargs):
        """
        Initialize a SignalHandler object.

        Args:
            signals (list): A list of Signal objects to associate with this handler.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        SignalHandler.id += 1
        self.id = SignalHandler.id
        self.name = name
        super(SignalHandler, self).__init__(*args, **kwargs)
        self.signals = {}
        self.signal_x_vals, self.signal_y_vals = {}, {}
        self.signal_popped_x_vals, self.signal_popped_y_vals = {}, {}
        self.data_lines = {}
        self.linked = False
        # self.default_y_limits = (-1.5, 5)
        self.setWindowTitle("PyQtGraph Test")
        self.setGeometry(0, 0, 1000, 600)
        self.layout = QtWidgets.QVBoxLayout()
        self.graphWidget = None
        self.initialize_graph()
        self.plot_current_x, self.plot_current_y = (
            {},
            {},
        )  # intermediate variables to plot the data points point by point.
        self.initialTimerInterval = 10
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.initialTimerInterval)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        # self.graphWidget.scene().sigMouseClicked.connect(self.moveDown)
        for signal in signals:
            self.add_signal(signal)

        self.pause = True
        self.selected = []
        self.zoom_factor = 1.0

    def initialize_graph(self):
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground("w")
        self.graphWidget.setLabel("left", "Amplitude", fontsize=60)
        self.graphWidget.setLabel("bottom", "Time", fontsize=60)
        self.graphWidget.setTitle(self.name, fontsize=200)
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setMouseEnabled(x=False, y=False)
        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)
        self.graphWidget.setAutoVisible(x=True, y=True)
        # self.graphWidget.setYRange(-1.5, 5)
        self.legend = self.graphWidget.addLegend()
        self.legend.setParentItem(self.graphWidget.getPlotItem())
        self.legend.getViewBox().setGeometry(1, 1, 2, 2)
        self.graphWidget.wheelEvent = self.custom_wheel_event

    def add_signal(self, signal):
        """
        Add a Signal object to this SignalHandler.

        Args:
            signal (Signal): The Signal object to add.
        """
        self.signals["0"] = signal
        signal.change_handler(self.id)
        self.signal_popped_x_vals["0"] = []
        self.signal_popped_y_vals["0"] = []
        self.plot_current_x["0"] = signal.popped_x_vals
        self.plot_current_y["0"] = signal.popped_y_vals
        self.signal_x_vals["0"] = list(signal.x)
        self.signal_y_vals["0"] = list(signal.y)
        self.data_lines["0"] = self.graphWidget.plot(
            self.plot_current_x["0"],
            self.plot_current_y["0"],
            pen=signal.pen,
            name=f"{signal.name}",
        )

    def handle_empty_channel(self):
        if len(self.data_lines) < 1:
            self.timer.start()
            self.data_lines.clear()
            self.graphWidget.clear()
            self.timer.stop()

    def toggle_link(self):
        self.linked = not self.linked

    def delete_signal(self, signal):
        if len(self.signals) == 1:
            del self.plot_current_x["0"]
            del self.plot_current_y["0"]
            del self.signal_x_vals["0"]
            del self.signal_y_vals["0"]
            self.graphWidget.removeItem(self.data_lines["0"])
            del self.data_lines["0"]
            removed_signal = self.signals.pop("0")
            # check if the channel is empty clear the graph
            self.handle_empty_channel()
            return removed_signal
        return "0"

    def change_speed(self, speed):
        interval = self.initialTimerInterval
        newInterval = int(interval // speed)
        self.timer.setInterval(newInterval)

    def reset(self):
        self.layout.removeWidget(self.graphWidget)
        self.graphWidget.deleteLater()
        self.initialize_graph()
        for _, signal in self.signals.items():
            signal.x = signal.popped_x_vals + self.signal_x_vals["0"]
            signal.popped_x_vals = []
            signal.y = signal.popped_y_vals + self.signal_y_vals["0"]
            signal.popped_y_vals = []
            self.plot_current_x["0"] = []
            self.plot_current_y["0"] = []
            self.add_signal(signal)

    def rescale(self, zoom_factor):
        """Rescales the plot based on the provided zoom factor."""
        self.zoom_factor = zoom_factor
        for id, _ in self.plot_current_x.items():
            self.graphWidget.setXRange(
                self.plot_current_x[id]["0"] * self.zoom_factor,
                self.plot_current_x[id][-1] * self.zoom_factor,
            )
            self.graphWidget.setYRange(
                min(self.plot_current_y[id]) * self.zoom_factor,
                max(self.plot_current_y[id]) * self.zoom_factor,
            )
            self.update_plot_data()

    def zoom_in(self):
        if self.pause and self.zoom_factor > 1 / (1.1**3):
            self.zoom_factor /= 1.1
            self.rescale(self.zoom_factor)

    def zoom_out(self):
        if self.pause:
            if self.zoom_factor == 1:
                self.graphWidget.setYRange(*self.default_y_limits)
                return
            self.zoom_factor *= 1.1
            self.rescale(self.zoom_factor)

    def toggle_pause(self):
        self.pause = not self.pause
        if self.pause:
            self.timer.stop()
            self.graphWidget.setMouseEnabled(x=True, y=True)

        else:
            self.real_time_update_enabled = True
            self.graphWidget.setMouseEnabled(x=False, y=False)
            self.timer.start()

        return self.pause

    def play(self):
        if self.pause:
            self.real_time_update_enabled = True
            self.graphWidget.setMouseEnabled(x=False, y=False)
            self.timer.start()
        self.pause = False

    def update_plot_data(self):
        for _, signal in self.signals.items():
            if (
                    self.signal_x_vals["0"]
                    and self.signal_y_vals["0"]
                    and signal.is_visible
            ):
                signal.update_state(
                    (self.signal_x_vals["0"][0], self.signal_y_vals["0"][0])
                )
                # Pop the oldest data point and append the newest one
                popped_x_value, popped_y_value = self.signal_x_vals["0"].pop(0), self.signal_y_vals["0"].pop(0)
                signal.popped_x_vals.append(popped_x_value)
                signal.popped_y_vals.append(popped_y_value)

                # Adjust the window size to the last 'N' data points
                window_size = 1000  # Set the desired window size
                if len(signal.popped_x_vals) > window_size:
                    signal.popped_x_vals = signal.popped_x_vals[-window_size:]
                    signal.popped_y_vals = signal.popped_y_vals[-window_size:]

                # Update the plot with the current data within the window
                self.data_lines["0"].setData(signal.popped_x_vals, signal.popped_y_vals)

                # Set appropriate x-axis range for the sliding window effect
                self.graphWidget.setXRange(min(signal.popped_x_vals), max(signal.popped_x_vals))

                # self.graphWidget.setLimits(
                # xMin=0,
                # xMax=self.plot_current_x[signal.id][-1] + 0.007,
                # yMin=-1 + yMin,
                # yMax=3 + yMax,
                # )

    def statistics_report(self):
        reports = {}
        for _, signal in self.signals.items():
            x_limit, y_limit = signal.state
            amplitudes = np.array(signal.y[: int(y_limit) + 1])
            mean = np.mean(amplitudes)
            std = np.std(amplitudes)
            amplitude_range = (min(amplitudes), max(amplitudes))
            peak_to_peak = amplitude_range[1] - amplitude_range[0]
            signal_duration = x_limit
            signal_report = {
                "mean": mean,
                "std": std,
                "amplitude_range": amplitude_range,
                "peak_to_peak": peak_to_peak,
                "signal_duration": signal_duration,
            }
            reports[signal.name] = signal_report

        graphPath = self.export_plot()
        return {"reports": reports, "graphPath": graphPath}

    def export_plot(self):
        if not os.path.exists("results"):
            os.mkdir("results")

        fileName = f"Channel_{self.id}_{time.time() * 1000}.png"
        outputPath = os.path.join("results", fileName)
        exporter = pg.exporters.ImageExporter(self.graphWidget.plotItem)
        exporter.export(outputPath)
        return outputPath

    def getLimits(self):
        positions_of_bounds_x_y = self.graphWidget.viewRange()
        x_bounds, y_bounds = positions_of_bounds_x_y[0], positions_of_bounds_x_y[1]
        return x_bounds[0], x_bounds[1], y_bounds[0], y_bounds[1]

    def getBoundaries(self):
        xMax = max(list(chain.from_iterable(self.plot_current_x.values())))
        xMin = min(list(chain.from_iterable(self.plot_current_x.values())))
        yMax = max(list(chain.from_iterable(self.plot_current_y.values())))
        yMin = min(list(chain.from_iterable(self.plot_current_y.values())))
        return {"x": {"max": xMax, "min": xMin}, "y": {"max": yMax, "min": yMin}}

    def moveRight(self, step=5):
        if self.pause:
            x_min, x_max, _, _ = self.getLimits()
            last_time_step = max(
                list(chain.from_iterable(self.plot_current_x.values()))
            )
            if last_time_step > x_max:
                self.graphWidget.setXRange(x_min + step, x_max + step)

    def moveLeft(self, step=5):
        if self.pause:
            x_min, x_max, _, _ = self.getLimits()
            x_range = x_max - x_min  # Calculate the current x-axis range
            new_x_min = x_min - step  # Calculate the new minimum x-value for the view
            new_x_max = (
                new_x_min + x_range
            )  # Calculate the new maximum x-value for the view
            if new_x_min > 0:
                self.graphWidget.setXRange(new_x_min, new_x_max)

    def moveUp(self):
        step = 0.5
        if self.pause:
            _, _, y_min, y_max = self.getLimits()
            max_plotted_y_val = max(
                list(chain.from_iterable(self.plot_current_y.values()))
            )
            if y_max <= max_plotted_y_val:
                self.graphWidget.setYRange(y_min + step, y_max + step)

    def moveDown(self):
        step = 0.5
        if self.pause:
            _, _, y_min, y_max = self.getLimits()
            min_plotted_y_val = min(
                list(chain.from_iterable(self.plot_current_y.values()))
            )
            if y_min > min_plotted_y_val:
                self.graphWidget.setYRange(y_min - step, y_max - step)

    # Add these methods to your SignalHandler class
    def scroll_to_x(self, x_position):
        # x_min,- x_max, y_min, y_max = self.getLimits()
        x_range = self.graphWidget.getViewBox().state["viewRange"][0]
        rx = 0.1 * (x_range[1] - x_range[0])
        self.current_widget.setXRange((x_range[0] + rx), (x_range[1] + rx), padding=0)

    def scroll_to_y(self, y_position):
        x_min, x_max, y_min, y_max = self.getLimits()
        delta_y = y_position - y_min
        new_y_min = y_min + delta_y
        new_y_max = y_max + delta_y
        self.graphWidget.setYRange(new_y_min, new_y_max)

    def get_current_limits(self):
        return (
            min(chain.from_iterable(self.plot_current_x.values())),
            max(chain.from_iterable(self.plot_current_x.values())),
            min(chain.from_iterable(self.plot_current_y.values())),
            max(chain.from_iterable(self.plot_current_y.values())),
        )

    def update_legend(self, signal):
        self.legend.removeItem(self.data_lines["0"])
        self.legend.addItem(self.data_lines["0"], signal.name)

    def custom_wheel_event(self, event):
        if self.pause:
            pass
        else:
            super(pg.PlotWidget, self.graphWidget).wheelEvent(event)
