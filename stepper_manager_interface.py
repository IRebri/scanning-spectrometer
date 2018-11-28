# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stepper_manager_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 469)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.speedSlider = QtWidgets.QSlider(self.centralwidget)
        self.speedSlider.setGeometry(QtCore.QRect(30, 160, 141, 22))
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(1050)
        self.speedSlider.setSingleStep(3)
        self.speedSlider.setProperty("value", 10)
        self.speedSlider.setSliderPosition(10)
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.speedSlider.setObjectName("speedSlider")
        self.joystickXYLabel = QtWidgets.QLabel(self.centralwidget)
        self.joystickXYLabel.setGeometry(QtCore.QRect(60, 50, 71, 31))
        self.joystickXYLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.joystickXYLabel.setObjectName("joystickXYLabel")
        self.speedLabel = QtWidgets.QLabel(self.centralwidget)
        self.speedLabel.setGeometry(QtCore.QRect(30, 140, 131, 20))
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
        self.progressBar.setGeometry(QtCore.QRect(70, 400, 371, 23))
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
        self.pointWidthEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pointWidthEdit.setGeometry(QtCore.QRect(250, 130, 51, 20))
        self.pointWidthEdit.setObjectName("pointWidthEdit")
        self.pointHeightEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pointHeightEdit.setGeometry(QtCore.QRect(250, 160, 51, 20))
        self.pointHeightEdit.setObjectName("pointHeightEdit")
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(200, 360, 141, 23))
        self.scanButton.setObjectName("scanButton")
        self.setHeightLabel = QtWidgets.QLabel(self.centralwidget)
        self.setHeightLabel.setGeometry(QtCore.QRect(200, 160, 47, 13))
        self.setHeightLabel.setObjectName("setHeightLabel")
        self.setWidthLabel = QtWidgets.QLabel(self.centralwidget)
        self.setWidthLabel.setGeometry(QtCore.QRect(200, 130, 47, 13))
        self.setWidthLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setWidthLabel.setObjectName("setWidthLabel")
        self.resolutionEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.resolutionEdit.setGeometry(QtCore.QRect(270, 190, 51, 20))
        self.resolutionEdit.setObjectName("resolutionEdit")
        self.setResolutionLabel = QtWidgets.QLabel(self.centralwidget)
        self.setResolutionLabel.setGeometry(QtCore.QRect(200, 190, 61, 16))
        self.setResolutionLabel.setObjectName("setResolutionLabel")
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(0, 400, 47, 13))
        self.progressLabel.setObjectName("progressLabel")
        self.pointsLabel = QtWidgets.QLabel(self.centralwidget)
        self.pointsLabel.setGeometry(QtCore.QRect(310, 150, 31, 16))
        self.pointsLabel.setObjectName("pointsLabel")
        self.stepsLabel = QtWidgets.QLabel(self.centralwidget)
        self.stepsLabel.setGeometry(QtCore.QRect(410, 150, 47, 13))
        self.stepsLabel.setObjectName("stepsLabel")
        self.setToZeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.setToZeroButton.setGeometry(QtCore.QRect(30, 190, 131, 23))
        self.setToZeroButton.setObjectName("setToZeroButton")
        self.enableXCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.enableXCheckBox.setGeometry(QtCore.QRect(40, 230, 141, 17))
        self.enableXCheckBox.setChecked(True)
        self.enableXCheckBox.setObjectName("enableXCheckBox")
        self.enableYCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.enableYCheckBox.setGeometry(QtCore.QRect(40, 250, 141, 17))
        self.enableYCheckBox.setChecked(True)
        self.enableYCheckBox.setObjectName("enableYCheckBox")
        self.stepWidthEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.stepWidthEdit.setGeometry(QtCore.QRect(350, 130, 51, 20))
        self.stepWidthEdit.setObjectName("stepWidthEdit")
        self.stepHeightEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.stepHeightEdit.setGeometry(QtCore.QRect(350, 160, 51, 20))
        self.stepHeightEdit.setObjectName("stepHeightEdit")
        self.zigzagRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.zigzagRadioButton.setGeometry(QtCore.QRect(210, 220, 82, 17))
        self.zigzagRadioButton.setChecked(True)
        self.zigzagRadioButton.setObjectName("zigzagRadioButton")
        self.spiralRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.spiralRadioButton.setEnabled(False)
        self.spiralRadioButton.setGeometry(QtCore.QRect(310, 220, 82, 17))
        self.spiralRadioButton.setObjectName("spiralRadioButton")
        self.integrationTimeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.integrationTimeEdit.setGeometry(QtCore.QRect(200, 260, 171, 20))
        self.integrationTimeEdit.setObjectName("integrationTimeEdit")
        self.integrationTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.integrationTimeLabel.setGeometry(QtCore.QRect(200, 240, 121, 16))
        self.integrationTimeLabel.setObjectName("integrationTimeLabel")
        self.virtualSpecCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.virtualSpecCheckBox.setGeometry(QtCore.QRect(200, 340, 171, 17))
        self.virtualSpecCheckBox.setChecked(True)
        self.virtualSpecCheckBox.setObjectName("virtualSpecCheckBox")
        self.scanToAverageEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.scanToAverageEdit.setGeometry(QtCore.QRect(200, 310, 171, 20))
        self.scanToAverageEdit.setObjectName("scanToAverageEdit")
        self.scanToAverageLabel = QtWidgets.QLabel(self.centralwidget)
        self.scanToAverageLabel.setGeometry(QtCore.QRect(200, 290, 201, 21))
        self.scanToAverageLabel.setObjectName("scanToAverageLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа управления сканером"))
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
        self.targetXEdit.setText(_translate("MainWindow", "0"))
        self.targetYEdit.setText(_translate("MainWindow", "0"))
        self.pointWidthEdit.setText(_translate("MainWindow", "10"))
        self.pointHeightEdit.setText(_translate("MainWindow", "10"))
        self.scanButton.setText(_translate("MainWindow", "Сканировать"))
        self.setHeightLabel.setText(_translate("MainWindow", "Высота"))
        self.setWidthLabel.setText(_translate("MainWindow", "Ширина"))
        self.resolutionEdit.setText(_translate("MainWindow", "1"))
        self.setResolutionLabel.setText(_translate("MainWindow", "Разрешение"))
        self.progressLabel.setText(_translate("MainWindow", "Прогресс"))
        self.pointsLabel.setText(_translate("MainWindow", "точек"))
        self.stepsLabel.setText(_translate("MainWindow", "шагов"))
        self.setToZeroButton.setText(_translate("MainWindow", "Обнулить координаты"))
        self.enableXCheckBox.setText(_translate("MainWindow", "Включить двигатель X"))
        self.enableYCheckBox.setText(_translate("MainWindow", "Включить двигатель Y"))
        self.stepWidthEdit.setText(_translate("MainWindow", "10"))
        self.stepHeightEdit.setText(_translate("MainWindow", "10"))
        self.zigzagRadioButton.setText(_translate("MainWindow", "Зигзаг"))
        self.spiralRadioButton.setText(_translate("MainWindow", "Спираль"))
        self.integrationTimeEdit.setText(_translate("MainWindow", "50000"))
        self.integrationTimeLabel.setText(_translate("MainWindow", "Время накопления (мкс)"))
        self.virtualSpecCheckBox.setText(_translate("MainWindow", "Виртуальный спектрометр"))
        self.scanToAverageEdit.setText(_translate("MainWindow", "1"))
        self.scanToAverageLabel.setText(_translate("MainWindow", "Число измерений для усреднения"))

