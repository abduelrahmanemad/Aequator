import wave
import numpy as np
import pandas as pd
from scipy.io import wavfile
from Signal import Signal
import matplotlib.pyplot as plt

files_data = {
    "Music": {"0": [20, 70], "1": [60, 80], "2": [270, 400], "3": [200, 290]},
    "Animals": {"0": [0, 1470], "1": [1470, 2940], "2": [2940, 4410], "3": [4410, 5880]},
    "Uniform": {
        "0": [0, 2000],
        "1": [2001, 4000],
        "2": [4001, 6000],
        "3": [6001, 8000],
        "4": [8001, 10000],
        "5": [10001, 12000],
        "6": [12001, 14000],
        "7": [14001, 16000],
        "8": [16001, 18000],
        "9": [18001, 20000],
    },
    "ECG": {"0": [0, 20], "1": [0, 4], "2": [0, 5]},
}

num_bands = {"Uniform": 10, "ECG": 3, "Music": 4, "Animals": 4}


class Signal(Signal):
    def __init__(self, name):
        super(Signal, self).__init__(name)
        self.fft = None
        self.magnitude_specturm = None
        self.phase_spectrum = None
        self.frequency_components = None
        self.slider_ranges = {}
        self.modified_data = None
        self.num_bands = None
        self.gains = None
        self.selected_band = None
        self.sample_rate = None
        self.num_of_channels = None
        self.window = None
        self.original_magnitude = None
        self.mode = None
        self.window_type = None
        self.ranges = {}

    def signal_fft(self):
        """
        Computes the fft of a signal and stores the fft, magnitude spectrum, phase spectrum and frequency spectrum
        :param signal: signal to compute fft
        :return: None
        """
        self.fft = np.fft.rfft(self.y)
        self.magnitude_specturm = np.abs(self.fft)
        self.phase_spectrum = np.angle(self.fft)
        self.modified_data = self.magnitude_specturm.copy()

    def initialze_gains(self):
        if not self.gains:
            self.gains = [1] * self.num_bands
        elif len(self.gains) != self.num_bands:
            self.gains = [1] * self.num_bands
        else:
            self.gains = [val for i, val in enumerate(self.gains)]

    def get_mode(self, mode="Uniform"):
        """
        sets the mode of the signal and calls the appropriate function to make the partionning
        """
        self.num_bands = num_bands[mode]
        self.ranges = files_data[mode]
        self.mode = mode
        if mode == "ECG":
            self.sample_rate = 500

        self.initialze_gains()
        self.make_bands()

    def make_bands(self):
        """
        Makes bands of equal lengths
        :return: None
        """
        self.frequency_components = np.fft.rfftfreq(
            2 * self.magnitude_specturm.size, 1 / self.sample_rate
        )
        slider_index = 0
        for index, freqs in self.ranges.items():
            start_freq, end_freq = self.ranges[index][0], self.ranges[index][1]
            indices_range = np.where(
                (self.frequency_components >= start_freq)
                & (self.frequency_components <= end_freq)
            )
            self.slider_ranges[slider_index] = self.magnitude_specturm[indices_range]
            slider_index += 1
        self.original_magnitude = self.slider_ranges.copy()

    def set_selected_band(self, selected_band: int):
        self.selected_band = selected_band

    def set_gains(self, val=None):
        # aka the gain is the value on my slider multiplies each slider value in a linear gain space by its amplitude
        # and flattens the array, so we have a 1d array of amplitudes that is ready to be multiplied
        # by the window function and then inverse fft
        if val is not None:
            # for index in range(self.num_bands):
            #     self.gains[index] = 0
            self.gains[self.selected_band] = val

        # linear_gains = np.int16(10 ** (np.array(self.gains) / 20))
        for index in range(self.num_bands):
            self.slider_ranges[index] = (
                self.original_magnitude[index]
                * self.gains[index]
            )
            start_freq, end_freq = (
                self.ranges[str(index)][0],
                self.ranges[str(index)][1],
            )
            indices_range = np.where(
                (self.frequency_components >= start_freq)
                & (self.frequency_components <= end_freq)
            )
            self.modified_data[indices_range] = self.slider_ranges[index]

    def windowing(self, window_type):
        band_width = len(self.slider_ranges[self.selected_band])
        if window_type == "hann":
            self.window = np.hanning(band_width)
            print(f"min {min(self.window)}, max{max(self.window)}")
        elif window_type == "hamming":
            self.window = np.hamming(band_width)
        elif window_type == "gaussian":
            # Create a Gaussian window with a specified sigma (standard deviation)
            sigma = 0.1  # Adjust the sigma value as needed
            self.window = np.exp(
                -0.5
                * ((np.arange(band_width) - band_width / 2) / (sigma * band_width / 2))
                ** 2
            )
        elif window_type == "rectangular":
            # Rectangular window (no windowing)
            self.window = np.ones(band_width)
        else:
            raise ValueError("Window type not supported")

        return self.window

    def inverse_fft(self):
        """
        Computes the inverse fft of the signal
        :return: None
        """
        fft = np.multiply(
            self.modified_data,
            np.exp(1j * self.phase_spectrum).flatten(),
        )

        inverse_fft = np.fft.irfft(fft)
        print(f"shape of inverse fft is {inverse_fft.shape}")
        return inverse_fft
        # TODO: implement inverse fft

    def convert_wav_csv(self, path: str):
        self.sample_rate, data = wavfile.read(path)
        df = pd.DataFrame(data)
        print(df)
        self.num_of_channels = len(df.columns)
        data_array = np.array(data, dtype=np.float32)
        self.x = np.arange(0, data_array.size / self.sample_rate, 1 / self.sample_rate)
        self.y = data_array.flatten()

    def numpy_array_to_audio(self, array, sample_rate=44100, output_file="out1.wav"):
        # Normalize the array to the range [-32768, 32767] for 16-bit PCM audio
        normalized_array = np.interp(
            array, (np.min(array), np.max(array)), (-32768, 32767)
        ).astype(np.int16)
        # Open a WAV file for writing
        with wave.open(output_file, "w") as wf:
            wf.setnchannels(self.num_of_channels)  # Mono audio
            wf.setsampwidth(2)  # 16-bit PCM
            wf.setframerate(sample_rate)  # Sample rate
            wf.writeframes(normalized_array.tobytes())

        print(f"Conversion complete. Audio saved to {output_file}")
