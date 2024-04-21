# Form implementation generated from reading ui file '.\UI\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 765)
        MainWindow.setStyleSheet("#mainWidget{\n"
"    background-color: #F0F0F0;\n"
"}\n"
"#slidersFrame{\n"
"    background-color: #f5f5f5;\n"
"}\n"
"#leftFrame{\n"
"    background-color: #f5f5f5;\n"
"}\n"
"QPushButton{\n"
"  background-color: #333333;\n"
"  border: none;\n"
"  border-radius: 6px;\n"
"  color: #cccccc;\n"
"  font-size: 14px;\n"
"  font-weight: 500;\n"
"  line-height: 20px;\n"
"  list-style: none;\n"
"  padding: 4px 12px;\n"
"  height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(51, 51, 51, 0.5);\n"
"     text-decoration: none;\n"
"}\n"
"QPushButton:focus{\n"
"     outline: 1px transparent;\n"
"}\n"
"QLabel{\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"}\n"
"QGroupBox{\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    padding:30px 0px 0px 0px;\n"
"    border:none;\n"
"}\n"
"QLineEdit{\n"
"    border:none;\n"
"    padding:4px 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"QListWidget{\n"
"    border:none;\n"
"    border-radius: 3px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QScrollArea{\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.leftFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.leftFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.leftFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.browseBtn = QtWidgets.QPushButton(parent=self.leftFrame)
        self.browseBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.browseBtn.setObjectName("browseBtn")
        self.verticalLayout_2.addWidget(self.browseBtn)
        self.frame = QtWidgets.QFrame(parent=self.leftFrame)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.orignalSignalGB_3 = QtWidgets.QGroupBox(parent=self.frame)
        self.orignalSignalGB_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.orignalSignalGB_3.setStyleSheet("QFrame{\n"
"    background-color: #F0F0F0;\n"
"    border-radius: 22px;\n"
"    border: 1px solid rgb(51, 51, 51);\n"
"}\n"
"QLabel{\n"
"    border:none;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton{\n"
"  background-color: #333333;\n"
"  border: none;\n"
"  border-radius: 12px;\n"
"  color: #cccccc;\n"
"  font-size: 14px;\n"
"  font-weight: 500;\n"
"  line-height: 19px;\n"
"  list-style: none;\n"
"  padding: 4px 4px;\n"
"\n"
"}")
        self.orignalSignalGB_3.setObjectName("orignalSignalGB_3")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.orignalSignalGB_3)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.originalFrame = QtWidgets.QFrame(parent=self.orignalSignalGB_3)
        self.originalFrame.setMaximumSize(QtCore.QSize(16777215, 45))
        self.originalFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.originalFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.originalFrame.setObjectName("originalFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.originalFrame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.originalPlayBtn = QtWidgets.QPushButton(parent=self.originalFrame)
        self.originalPlayBtn.setMinimumSize(QtCore.QSize(30, 0))
        self.originalPlayBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.originalPlayBtn.setObjectName("originalPlayBtn")
        self.horizontalLayout_12.addWidget(self.originalPlayBtn)
        self.verticalLayout_19.addWidget(self.originalFrame)
        self.horizontalLayout_2.addWidget(self.orignalSignalGB_3)
        self.updatedSignalGB_3 = QtWidgets.QGroupBox(parent=self.frame)
        self.updatedSignalGB_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.updatedSignalGB_3.setStyleSheet("QFrame{\n"
"    background-color: #F0F0F0;\n"
"    border-radius: 22px;\n"
"    border: 1px solid rgb(51, 51, 51);\n"
"}\n"
"QLabel{\n"
"    border:none;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton{\n"
"  background-color: #333333;\n"
"  border: none;\n"
"  border-radius: 12px;\n"
"  color: #cccccc;\n"
"  font-size: 14px;\n"
"  font-weight: 500;\n"
"  line-height: 19px;\n"
"  list-style: none;\n"
"  padding: 4px 4px;\n"
"\n"
"}")
        self.updatedSignalGB_3.setObjectName("updatedSignalGB_3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.updatedSignalGB_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.updatedFrame = QtWidgets.QFrame(parent=self.updatedSignalGB_3)
        self.updatedFrame.setMaximumSize(QtCore.QSize(16777215, 45))
        self.updatedFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.updatedFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.updatedFrame.setObjectName("updatedFrame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.updatedFrame)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.updatedPlayBtn = QtWidgets.QPushButton(parent=self.updatedFrame)
        self.updatedPlayBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.updatedPlayBtn.setObjectName("updatedPlayBtn")
        self.horizontalLayout_13.addWidget(self.updatedPlayBtn)
        self.verticalLayout_20.addWidget(self.updatedFrame)
        self.horizontalLayout_2.addWidget(self.updatedSignalGB_3)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(parent=self.leftFrame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.frame_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_25.addWidget(self.groupBox_2)
        self.selectModeComBox = QtWidgets.QComboBox(parent=self.frame_3)
        self.selectModeComBox.setObjectName("selectModeComBox")
        self.selectModeComBox.addItem("")
        self.verticalLayout_25.addWidget(self.selectModeComBox)
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_25.addWidget(self.groupBox)
        self.selectWindowComBox = QtWidgets.QComboBox(parent=self.frame_3)
        self.selectWindowComBox.setObjectName("selectWindowComBox")
        self.verticalLayout_25.addWidget(self.selectWindowComBox)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.applyChangesBtn = QtWidgets.QPushButton(parent=self.leftFrame)
        self.applyChangesBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.applyChangesBtn.setObjectName("applyChangesBtn")
        self.verticalLayout_2.addWidget(self.applyChangesBtn)
        self.horizontalLayout.addWidget(self.leftFrame)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.ControllerFrame = QtWidgets.QFrame(parent=self.frame_5)
        self.ControllerFrame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.ControllerFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ControllerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ControllerFrame.setObjectName("ControllerFrame")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.ControllerFrame)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.playPauseBtn = QtWidgets.QPushButton(parent=self.ControllerFrame)
        self.playPauseBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\../../First-Task/UI/icons/play.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.playPauseBtn.setIcon(icon)
        self.playPauseBtn.setIconSize(QtCore.QSize(30, 30))
        self.playPauseBtn.setObjectName("playPauseBtn")
        self.horizontalLayout_15.addWidget(self.playPauseBtn)
        self.resetBtn = QtWidgets.QPushButton(parent=self.ControllerFrame)
        self.resetBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\UI\\../../First-Task/UI/icons/reset.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.resetBtn.setIcon(icon1)
        self.resetBtn.setIconSize(QtCore.QSize(30, 30))
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout_15.addWidget(self.resetBtn)
        self.zoomInBtn = QtWidgets.QPushButton(parent=self.ControllerFrame)
        self.zoomInBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\UI\\../../First-Task/UI/icons/zoomIn.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.zoomInBtn.setIcon(icon3)
        self.zoomInBtn.setIconSize(QtCore.QSize(30, 30))
        self.zoomInBtn.setObjectName("zoomInBtn")
        self.horizontalLayout_15.addWidget(self.zoomInBtn)
        self.zoomOutBtn = QtWidgets.QPushButton(parent=self.ControllerFrame)
        self.zoomOutBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\UI\\../../First-Task/UI/icons/zoomOut.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.zoomOutBtn.setIcon(icon4)
        self.zoomOutBtn.setIconSize(QtCore.QSize(30, 30))
        self.zoomOutBtn.setObjectName("zoomOutBtn")
        self.horizontalLayout_15.addWidget(self.zoomOutBtn)
        self.speedBtn = QtWidgets.QPushButton(parent=self.ControllerFrame)
        self.speedBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\UI\\../../First-Task/UI/icons/snapshot.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.speedBtn.setIcon(icon5)
        self.speedBtn.setIconSize(QtCore.QSize(30, 30))
        self.speedBtn.setObjectName("speedBtn")
        self.horizontalLayout_15.addWidget(self.speedBtn)
        spacerItem = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.verticalLayout_22.addWidget(self.ControllerFrame)
        self.verticalLayout_21.addWidget(self.frame_5)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.originalSignalGraph = QtWidgets.QFrame(parent=self.frame_8)
        self.originalSignalGraph.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.originalSignalGraph.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.originalSignalGraph.setObjectName("originalSignalGraph")
        self.verticalLayout_23.addWidget(self.originalSignalGraph)
        self.mutatedSignalGraph = QtWidgets.QFrame(parent=self.frame_8)
        self.mutatedSignalGraph.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mutatedSignalGraph.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mutatedSignalGraph.setObjectName("mutatedSignalGraph")
        self.verticalLayout_23.addWidget(self.mutatedSignalGraph)
        self.horizontalLayout_16.addLayout(self.verticalLayout_23)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_9.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.originalSignalSpectrogram = QtWidgets.QFrame(parent=self.frame_9)
        self.originalSignalSpectrogram.setMaximumSize(QtCore.QSize(250, 16777215))
        self.originalSignalSpectrogram.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.originalSignalSpectrogram.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.originalSignalSpectrogram.setObjectName("originalSignalSpectrogram")
        self.verticalLayout_24.addWidget(self.originalSignalSpectrogram)
        self.mutatedSignalSpectrogram = QtWidgets.QFrame(parent=self.frame_9)
        self.mutatedSignalSpectrogram.setMaximumSize(QtCore.QSize(250, 16777215))
        self.mutatedSignalSpectrogram.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mutatedSignalSpectrogram.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mutatedSignalSpectrogram.setObjectName("mutatedSignalSpectrogram")
        self.verticalLayout_24.addWidget(self.mutatedSignalSpectrogram)
        self.horizontalLayout_16.addWidget(self.frame_9)
        self.verticalLayout_21.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.bottomFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.bottomFrame.setMinimumSize(QtCore.QSize(0, 250))
        self.bottomFrame.setMaximumSize(QtCore.QSize(16777215, 250))
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottomFrame.setObjectName("bottomFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.slidersFrame = QtWidgets.QFrame(parent=self.bottomFrame)
        self.slidersFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.slidersFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.slidersFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.slidersFrame.setObjectName("slidersFrame")
        self.horizontalLayout_3_5 = QtWidgets.QHBoxLayout(self.slidersFrame)
        self.horizontalLayout_3_5.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.addWidget(self.slidersFrame)
        self.freqGraph = QtWidgets.QFrame(parent=self.bottomFrame)
        self.freqGraph.setMaximumWidth(700)
        self.freqGraph.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.freqGraph.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.freqGraph.setObjectName("freqGraph")
        self.horizontalLayout_3.addWidget(self.freqGraph)
        self.verticalLayout.addWidget(self.bottomFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        playIcon = QtGui.QIcon()
        playIcon.addPixmap(
            QtGui.QPixmap("icons/play.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        stopIcon = QtGui.QIcon()
        stopIcon.addPixmap(
            QtGui.QPixmap("icons/pause.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        resetIcon = QtGui.QIcon()
        resetIcon.addPixmap(
            QtGui.QPixmap("icons/reset.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        zoomInIcon = QtGui.QIcon()
        zoomInIcon.addPixmap(
            QtGui.QPixmap("icons/zoomIn.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        zoomOutIcon = QtGui.QIcon()
        zoomOutIcon.addPixmap(
            QtGui.QPixmap("icons/zoomOut.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.originalPlayBtn.setIcon(playIcon)
        self.updatedPlayBtn.setIcon(playIcon)
        self.playPauseBtn.setIcon(stopIcon)
        self.resetBtn.setIcon(resetIcon)
        self.zoomInBtn.setIcon(zoomInIcon)
        self.zoomOutBtn.setIcon(zoomOutIcon)
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browseBtn.setText(_translate("MainWindow", "Browse Files"))
        self.orignalSignalGB_3.setTitle(_translate("MainWindow", "Orignal Signal"))
        self.updatedSignalGB_3.setTitle(_translate("MainWindow", "Updated Signal"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Select Mode"))
        self.selectModeComBox.setItemText(0, _translate("MainWindow", "Uniform"))
        self.groupBox.setTitle(_translate("MainWindow", "Select Window"))
        self.applyChangesBtn.setText(_translate("MainWindow", "Apply Changes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
