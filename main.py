from functools import partial
import os
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QMenu,
    QSlider,
    QLabel,
    QSizePolicy,
)
from PyQt6 import QtGui
from PyQt6.QtCore import QPoint
import matplotlib.pyplot as plt
from Equalizer import EqualizerScreen
from signal_utils import Signal
from mainwindow import Ui_MainWindow
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

modes = [
    {
        "name": "Uniform",
        "slidersCount": 10,
        "labels": [
            "0-2k",
            "2k-4k",
            "4k-6k",
            "6k-8k",
            "8k-10k",
            "10k-12k",
            "12k-14k",
            "14k-16k",
            "16k-18k",
            "18k-20k",
        ],
    },
    {
        "name": "Animals",
        "slidersCount": 4,
        "labels": ["Wolf", "Dolfen", "Cat", "Birds"],
    },
    {
        "name": "Music",
        "slidersCount": 4,
        "labels": ["Drums", "Rest", "Piano", "Guitar"],
    },
    {"name": "ECG", "slidersCount": 3, "labels": ["VF", "AFL", "VT"]},
]

speeds = [
    "0.25x",
    "0.5x",
    "0.75x",
    "1x",
    "1.25x",
    "1.5x",
    "1.75x",
    "2",
    "3x",
    "4x",
]

windows = ["rectangular", "hann", "hamming", "gaussian"]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.selectModeComBox.clear()
        for mode in modes:
            self.selectModeComBox.addItem(mode["name"])

        for i in range(10):
            self.addSlider(modes[0]["labels"][i])

        self.selectWindowComBox.clear()
        for window in windows:
            self.selectWindowComBox.addItem(window)
        self.selectWindowComBox.currentIndexChanged.connect(self.handleChangeWindow)
        self.currentWindow = "rectangular"

        self.equalizer = EqualizerScreen()
        self.originalSignalGraph.setLayout(QVBoxLayout())
        self.mutatedSignalGraph.setLayout(QVBoxLayout())
        self.originalSignalSpectrogram.setLayout(QVBoxLayout())
        self.mutatedSignalSpectrogram.setLayout(QVBoxLayout())
        self.freqGraph.setLayout(QVBoxLayout())
        self.selectModeComBox.currentIndexChanged.connect(
            self.selectModeComboBoxChanged
        )
        # self.selectModeComboBoxChanged()
        self.originalSignalGraph.layout().addWidget(self.equalizer.channel1.graphWidget)
        self.originalSignalSpectrogram.layout().addWidget(self.equalizer.canvas3)
        # self.originalSignalSpectrogram.layout().setAlignment(
        # self.equalizer.canvas3, QtCore.Qt.AlignmentFlag.AlignVCenter
        # )
        self.mutatedSignalGraph.layout().addWidget(self.equalizer.channel2.graphWidget)
        self.mutatedSignalSpectrogram.layout().addWidget(self.equalizer.canvas4)
        self.equalizer.canvas4.draw()
        # self.mutatedSignalSpectrogram.layout().setAlignment(
        # QtCore.Qt.AlignmentFlag.AlignVCenter
        # )
        self.freqGraph.layout().addWidget(self.equalizer.channel5.graphWidget)

        self.browseBtn.clicked.connect(self.handleUploadFile)
        self.originalPlayBtn.clicked.connect(self.playOriginalSignal)
        self.updatedPlayBtn.clicked.connect(self.stopOriginalSignal)
        self.originalSignal = None
        self.mediaPlayer = QMediaPlayer()
        self.originaAudio = QAudioOutput()
        self.mutatedMediaPlayer = QMediaPlayer()
        self.mutatedAudio = QAudioOutput()
        self.playPauseBtn.clicked.connect(self.handleTogglePlayPause)
        self.resetBtn.clicked.connect(self.handleReset)
        self.speedBtn.clicked.connect(self.handleToggleSpeedMenu)
        self.zoomInBtn.clicked.connect(self.handleZoomIn)
        self.zoomOutBtn.clicked.connect(self.handleZoomOut)
        self.speedBtn.setText("1x")
        self.applyChangesBtn.clicked.connect(self.handleApplyChanges)
        self.updatedPlayBtn.clicked.connect(self.playMutatedSignal)

    def handleApplyChanges(self):
        self.equalizer.draw_signal()
        self.handleTogglePlayPause()

    def handleTogglePlayPause(self):
        paused = self.equalizer.channel1.toggle_pause()
        self.equalizer.channel2.toggle_pause()
        newIcon = QtGui.QIcon()
        if not paused:
            newIcon.addPixmap(
                QtGui.QPixmap("icons/pause.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )
            self.equalizer.channel1.graphWidget.setXLink(
                self.equalizer.channel1.graphWidget
            )
            self.equalizer.channel1.graphWidget.setYLink(
                self.equalizer.channel1.graphWidget
            )
            self.equalizer.channel2.graphWidget.setXLink(
                self.equalizer.channel2.graphWidget
            )
            self.equalizer.channel2.graphWidget.setYLink(
                self.equalizer.channel2.graphWidget
            )
        else:
            newIcon.addPixmap(
                QtGui.QPixmap("icons/play.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )
            self.equalizer.channel1.graphWidget.setXLink(
                self.equalizer.channel2.graphWidget
            )
            self.equalizer.channel1.graphWidget.setYLink(
                self.equalizer.channel2.graphWidget
            )
            self.equalizer.channel2.graphWidget.setXLink(
                self.equalizer.channel1.graphWidget
            )
            self.equalizer.channel2.graphWidget.setYLink(
                self.equalizer.channel1.graphWidget
            )
        self.playPauseBtn.setIcon(newIcon)

    def handleZoomIn(self):
        self.equalizer.channel1.zoom_in()
        self.equalizer.channel2.zoom_in()

    def handleZoomOut(self):
        self.equalizer.channel1.zoom_out()
        self.equalizer.channel2.zoom_out()

    def handleReset(self):
        self.equalizer.channel1.reset()
        self.equalizer.channel2.reset()
        self.originalSignalGraph.layout().addWidget(self.equalizer.channel1.graphWidget)
        self.mutatedSignalGraph.layout().addWidget(self.equalizer.channel2.graphWidget)
        

    def playOriginalSignal(self):
        self.mediaPlayer.setAudioOutput(self.originaAudio)
        self.mediaPlayer.setSource(QtCore.QUrl.fromLocalFile(self.originalSignal))
        self.originaAudio.setVolume(50)
        self.mediaPlayer.setPosition(0)
        self.mediaPlayer.play()
        newIcon = QtGui.QIcon()
        newIcon.addPixmap(
            QtGui.QPixmap("icons/pause.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.originalPlayBtn.setIcon(newIcon)
        self.originalPlayBtn.clicked.disconnect()
        self.originalPlayBtn.clicked.connect(self.stopOriginalSignal)

    def playMutatedSignal(self):
        self.mutatedMediaPlayer.setAudioOutput(self.mutatedAudio)
        self.mutatedMediaPlayer.setSource(QtCore.QUrl.fromLocalFile("out1.wav"))
        self.mutatedAudio.setVolume(50)
        self.mutatedMediaPlayer.setPosition(0)
        self.mutatedMediaPlayer.play()
        newIcon = QtGui.QIcon()
        newIcon.addPixmap(
            QtGui.QPixmap("icons/pause.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.updatedPlayBtn.setIcon(newIcon)
        self.updatedPlayBtn.clicked.disconnect()
        self.updatedPlayBtn.clicked.connect(self.stopMutatedSignal)

    def stopMutatedSignal(self):
        self.mutatedMediaPlayer.stop()
        newIcon = QtGui.QIcon()
        newIcon.addPixmap(
            QtGui.QPixmap("icons/play.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.updatedPlayBtn.setIcon(newIcon)
        self.updatedPlayBtn.clicked.disconnect()
        self.updatedPlayBtn.clicked.connect(self.playMutatedSignal)

    def stopOriginalSignal(self):
        self.mediaPlayer.stop()
        newIcon = QtGui.QIcon()
        newIcon.addPixmap(
            QtGui.QPixmap("icons/play.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.originalPlayBtn.setIcon(newIcon)
        self.originalPlayBtn.clicked.disconnect()
        self.originalPlayBtn.clicked.connect(self.playOriginalSignal)

    # Handle toggle speed menu slot
    def handleToggleSpeedMenu(self):
        # Create a new QMenu
        speedMenu = QMenu()
        for speed in speeds:
            # Fill the menu with the speeds list
            speedAction = speedMenu.addAction(speed)
            # Connect each action with the handleChangeSpeed slot
            speedAction.triggered.connect(
                partial(self.handleChangeSpeed, float(speed.split("x")[0]))
            )

        # Position the QMenu
        button_rect = self.speedBtn.rect()
        menu_x = self.speedBtn.mapToGlobal(button_rect.topRight()).x()
        menu_y = self.speedBtn.mapToGlobal(button_rect.topRight()).y() - 5
        # Execute the QMenu
        speedMenu.exec(QPoint(menu_x, menu_y))

    def handleChangeSpeed(self, speedValue):
        self.equalizer.channel1.change_speed(speedValue)
        self.equalizer.channel2.change_speed(speedValue)
        self.speedBtn.setText(
            f"{int(speedValue) if int(speedValue) == speedValue else speedValue}x"
        )

    def selectModeComboBoxChanged(self):
        for i in reversed(range(self.slidersFrame.layout().count())):
            self.slidersFrame.layout().itemAt(i).widget().setParent(None)

        selectedMode = modes[self.selectModeComBox.currentIndex()]
        self.equalizer.change_mode(str(selectedMode["name"]))
        for i in range(selectedMode["slidersCount"]):
            self.addSlider(selectedMode["labels"][i])

    def handleChangeWindow(self):
        self.currentWindow = str(windows[self.selectWindowComBox.currentIndex()])
        self.equalizer.change_window(str(self.currentWindow))
        print(self.currentWindow)

    def addSlider(self, title):
        newWidget = QWidget()
        slider = QSlider()
        slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(1)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(1)
        newLayout = QVBoxLayout()
        newWidget.setLayout(newLayout)
        newWidget.layout().addWidget(slider)
        label = QLabel()
        label.setText(title)
        newWidget.layout().addWidget(label)

        self.slidersFrame.layout().addWidget(newWidget)
        i = self.slidersFrame.layout().count() - 1
        slider.valueChanged.connect(
            lambda value, index=i: self.sliderValueChanged(index)
        )

    def handleUploadFile(self):
        file = QFileDialog.getOpenFileName(
            self, "Open file", ".\\", "Wav files (*.wav)"
        )
        if file:
            signalName = os.path.splitext(os.path.basename(file[0]))[0]
            newSignal = Signal(signalName)
            self.originalSignal = file[0]
            newSignal.convert_wav_csv(file[0])
            self.equalizer.add_signal(newSignal)

    def sliderValueChanged(self, index):
        newValue = (
            self.slidersFrame.layout()
            .itemAt(index)
            .widget()
            .layout()
            .itemAt(0)
            .widget()
            .value()
        )
        self.equalizer.change_gain(index, newValue, self.currentWindow)
        # print(f"New Value is {newValue}")


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
