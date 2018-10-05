# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stepper_manager_interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 339)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.speedSlider = QtWidgets.QSlider(self.centralwidget)
        self.speedSlider.setGeometry(QtCore.QRect(30, 160, 141, 22))
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setObjectName("speedSlider")
        self.joystickXYLabel = QtWidgets.QLabel(self.centralwidget)
        self.joystickXYLabel.setGeometry(QtCore.QRect(60, 50, 71, 31))
        self.joystickXYLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.joystickXYLabel.setObjectName("joystickXYLabel")
        self.speedLabel = QtWidgets.QLabel(self.centralwidget)
        self.speedLabel.setGeometry(QtCore.QRect(70, 140, 47, 13))
        self.speedLabel.setObjectName("speedLabel")
        self.moveUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveUpButton.setGeometry(QtCore.QRect(80, 10, 31, 31))
        self.moveUpButton.setObjectName("moveUpButton")
        self.moveDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveDownButton.setGeometry(QtCore.QRect(80, 90, 31, 31))
        self.moveDownButton.setObjectName("moveDownButton")
        self.moveLeftButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveLeftButton.setGeometry(QtCore.QRect(30, 50, 31, 31))
        self.moveLeftButton.setObjectName("moveLeftButton")
        self.moveRightButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveRightButton.setGeometry(QtCore.QRect(130, 50, 31, 31))
        self.moveRightButton.setObjectName("moveRightButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(80, 270, 261, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.moveToButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveToButton.setGeometry(QtCore.QRect(200, 70, 141, 23))
        self.moveToButton.setObjectName("moveToButton")
        self.currentYLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentYLabel.setGeometry(QtCore.QRect(290, 40, 47, 13))
        self.currentYLabel.setObjectName("currentYLabel")
        self.currentXLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentXLabel.setGeometry(QtCore.QRect(290, 10, 47, 13))
        self.currentXLabel.setObjectName("currentXLabel")
        self.targetXEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.targetXEdit.setGeometry(QtCore.QRect(200, 10, 81, 20))
        self.targetXEdit.setObjectName("targetXEdit")
        self.targetYEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.targetYEdit.setGeometry(QtCore.QRect(200, 40, 81, 20))
        self.targetYEdit.setObjectName("targetYEdit")
        self.widthEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.widthEdit.setGeometry(QtCore.QRect(260, 130, 81, 20))
        self.widthEdit.setObjectName("widthEdit")
        self.heightEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.heightEdit.setGeometry(QtCore.QRect(260, 160, 81, 20))
        self.heightEdit.setObjectName("heightEdit")
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(200, 220, 141, 23))
        self.scanButton.setObjectName("scanButton")
        self.setHeightLabel = QtWidgets.QLabel(self.centralwidget)
        self.setHeightLabel.setGeometry(QtCore.QRect(200, 160, 47, 13))
        self.setHeightLabel.setObjectName("setHeightLabel")
        self.setWidthLabel = QtWidgets.QLabel(self.centralwidget)
        self.setWidthLabel.setGeometry(QtCore.QRect(200, 130, 47, 13))
        self.setWidthLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setWidthLabel.setObjectName("setWidthLabel")
        self.resolutionEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.resolutionEdit.setGeometry(QtCore.QRect(260, 190, 81, 20))
        self.resolutionEdit.setObjectName("resolutionEdit")
        self.setResolutionLabel = QtWidgets.QLabel(self.centralwidget)
        self.setResolutionLabel.setGeometry(QtCore.QRect(200, 190, 61, 16))
        self.setResolutionLabel.setObjectName("setResolutionLabel")
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(10, 270, 47, 13))
        self.progressLabel.setObjectName("progressLabel")
        self.realWidthLabel = QtWidgets.QLabel(self.centralwidget)
        self.realWidthLabel.setGeometry(QtCore.QRect(360, 130, 47, 13))
        self.realWidthLabel.setObjectName("realWidthLabel")
        self.realHeightLabel = QtWidgets.QLabel(self.centralwidget)
        self.realHeightLabel.setGeometry(QtCore.QRect(360, 160, 47, 13))
        self.realHeightLabel.setObjectName("realHeightLabel")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setGeometry(QtCore.QRect(30, 220, 31, 23))
        self.pauseButton.setObjectName("pauseButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setEnabled(False)
        self.stopButton.setGeometry(QtCore.QRect(70, 220, 31, 23))
        self.stopButton.setObjectName("stopButton")
        self.setToZeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.setToZeroButton.setGeometry(QtCore.QRect(30, 190, 131, 23))
        self.setToZeroButton.setObjectName("setToZeroButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Прорамма управления сканером"))
        self.joystickXYLabel.setText(_translate("MainWindow", "(x, y)"))
        self.speedLabel.setText(_translate("MainWindow", "Скорость"))
        self.moveUpButton.setText(_translate("MainWindow", "▲"))
        self.moveDownButton.setText(_translate("MainWindow", "▼"))
        self.moveLeftButton.setText(_translate("MainWindow", "◀"))
        self.moveRightButton.setText(_translate("MainWindow", "▶"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.moveToButton.setText(_translate("MainWindow", "Переместить"))
        self.currentYLabel.setText(_translate("MainWindow", "TextLabel"))
        self.currentXLabel.setText(_translate("MainWindow", "TextLabel"))
        self.scanButton.setText(_translate("MainWindow", "Сканировать"))
        self.setHeightLabel.setText(_translate("MainWindow", "Высота"))
        self.setWidthLabel.setText(_translate("MainWindow", "Ширина"))
        self.resolutionEdit.setText(_translate("MainWindow", "1"))
        self.setResolutionLabel.setText(_translate("MainWindow", "Разрешение"))
        self.progressLabel.setText(_translate("MainWindow", "TextLabel"))
        self.realWidthLabel.setText(_translate("MainWindow", "TextLabel"))
        self.realHeightLabel.setText(_translate("MainWindow", "TextLabel"))
        self.pauseButton.setText(_translate("MainWindow", "❚❚ "))
        self.stopButton.setText(_translate("MainWindow", "◼"))
        self.setToZeroButton.setText(_translate("MainWindow", "Обнулить координаты"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

