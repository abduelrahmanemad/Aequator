import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Mixer import Channel
from SignalHandler import SignalHandler
from signal_utils import Signal
import pyqtgraph as pg


class EqualizerScreen:
    def __init__(self):
        self.channel1 = SignalHandler("Original Signal", [])
        self.channel2 = SignalHandler("Mutated Signal", [])
        self.channel3 = Channel("Original Signal")
        self.channel4 = Channel("Mutated Signal")
        self.channel5 = Channel("Frequency")
        self.figure3 = Figure()
        self.figure4 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.canvas4 = FigureCanvas(self.figure4)
        self.signal = None
        self.add_spectrogram = True
        self.mutated_signal = None
        self.current_mode = "Uniform"
        self.original_magnitude = None

    def initialize_graphs(self):
        self.channel1.initialize_graph()
        self.channel2.initialize_graph()
        self.channel3.initialize_graph()
        self.channel4.initialize_graph()
        self.channel5.initialize_graph()


    def add_signal(self, sig: Signal):
        self.signal = sig
        self.signal.signal_fft()
        self.original_magnitude = self.signal.original_magnitude
        self.draw_signal()
        self.handle_spectrogram_drawing()
        self.handle_frequency_window()

    def draw_signal(self, mode="uniform"):
        self.delete_signal()
        self.signal.get_mode(self.current_mode)
        self.channel1.add_signal(self.signal)
        self.mutated_signal = Signal("Mutated")
        self.mutated_signal.x = self.signal.x
        self.mutated_signal.y = self.signal.inverse_fft()
        self.channel2.add_signal(self.mutated_signal)
        self.handle_frequency_window()
        self.handle_spectrogram_drawing()
        self.original_magnitude = self.signal.original_magnitude.copy()

        self.channel1.update_plot_data()
        self.channel2.update_plot_data()
        self.save_audio(self.signal.inverse_fft())

    def draw_spectrogram(self, channel, canvas, sig):
        plt.rcParams['font.size'] = '6'
        figure, ax = plt.subplots(figsize=(2.9, 2.6))

        # Create a spectrogram
        if self.current_mode == "ECG":
            self.signal.sample_rate = 500
        _, _, Sxx, im = ax.specgram(
            sig.flatten(), Fs=self.signal.sample_rate, cmap="plasma"
        )

        # Set axis labels
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Frequency (Hz)")
        ax.set_title(f"{channel.name} Spectrogram")
        plt.xticks(rotation=45)
        plt.yticks(rotation=45)

        figure.colorbar(im, ax=ax, label="Intensity (dB)")
        canvas.figure.clf()
        canvas.figure = figure
        canvas.draw()

    # selected_band -> Slider index
    # new_gain -> value
    # window -> rectangular

    def change_gain(self, selected_band, new_gain, window):
        self.signal.get_mode(self.current_mode)
        self.signal.set_selected_band(selected_band)
        self.signal.windowing(window)
        self.signal.set_gains(new_gain)
        inverse_fft = self.signal.inverse_fft()
        self.mutated_signal.y = inverse_fft
        print(f"bands {self.signal.num_bands}")
        self.handle_spectrogram_drawing()
        self.handle_frequency_window()

    def save_audio(self, audio, output_file="out1.wav"):
        self.signal.numpy_array_to_audio(audio, self.signal.sample_rate, output_file)

    def toggle_spectrogram(self, flag):
        self.add_spectrogram = flag

    def change_window(self, window="rectangular"):
        self.signal.windowing(window)
        self.handle_frequency_window()
        self.handle_spectrogram_drawing()

    def change_mode(self, mode):
        self.current_mode = mode

    def handle_spectrogram_drawing(self):
        if self.add_spectrogram and self.signal:
            self.draw_spectrogram(
                self.channel3, self.canvas3, self.signal.magnitude_specturm
            )
            self.draw_spectrogram(
                self.channel4,
                self.canvas4,
                self.signal.modified_data.flatten(),
            )

    def handle_frequency_window(self):
        self.signal.get_mode(self.current_mode)
        mags = abs(self.signal.modified_data.flatten())
        self.channel5.graphWidget.clear()
        self.channel5.graphWidget.plot(self.signal.frequency_components[:len(mags)], mags)
        window_y = self.signal.window
        #if type(self.signal.window) == np.ndarray:
            #window_y *= self.signal.slider_ranges[self.signal.selected_band][100]
            #window_x = list(self.signal.slider_frequencies[self.signal.selected_band])
            #self.channel5.graphWidget.plot(window_x, list(window_y), pen="r")

    def delete_signal(self):
        if self.signal:
            self.signal.popped_x_vals, self.signal.popped_y_vals = [], []
            self.channel1.delete_signal(self.signal)    
            self.channel2.delete_signal(self.mutated_signal)