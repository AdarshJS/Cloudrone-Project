# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Template.ui'
#
# Created: Tue Dec 22 16:00:22 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1310, 740)
        self.Attitude_Name = QtGui.QLabel(Form)
        self.Attitude_Name.setGeometry(QtCore.QRect(850, 230, 211, 20))
        self.Attitude_Name.setAcceptDrops(False)
        self.Attitude_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Attitude_Name.setObjectName(_fromUtf8("Attitude_Name"))
        self.Heading_Name = QtGui.QLabel(Form)
        self.Heading_Name.setGeometry(QtCore.QRect(1080, 230, 211, 20))
        self.Heading_Name.setAcceptDrops(False)
        self.Heading_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Heading_Name.setObjectName(_fromUtf8("Heading_Name"))
        self.Turn_Name = QtGui.QLabel(Form)
        self.Turn_Name.setGeometry(QtCore.QRect(850, 360, 211, 20))
        self.Turn_Name.setAcceptDrops(False)
        self.Turn_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Turn_Name.setObjectName(_fromUtf8("Turn_Name"))
        self.Throttle_Name = QtGui.QLabel(Form)
        self.Throttle_Name.setGeometry(QtCore.QRect(1080, 360, 211, 20))
        self.Throttle_Name.setAcceptDrops(False)
        self.Throttle_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Throttle_Name.setObjectName(_fromUtf8("Throttle_Name"))
        self.Battery = QtGui.QProgressBar(Form)
        self.Battery.setGeometry(QtCore.QRect(1210, 422, 61, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Battery.setFont(font)
        self.Battery.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Battery.setProperty("value", 50)
        self.Battery.setTextVisible(True)
        self.Battery.setOrientation(QtCore.Qt.Vertical)
        self.Battery.setInvertedAppearance(False)
        self.Battery.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.Battery.setObjectName(_fromUtf8("Battery"))
        self.Battery_Name = QtGui.QLabel(Form)
        self.Battery_Name.setGeometry(QtCore.QRect(1200, 640, 91, 20))
        self.Battery_Name.setAcceptDrops(False)
        self.Battery_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Battery_Name.setObjectName(_fromUtf8("Battery_Name"))
        self.Throttle = QtGui.QProgressBar(Form)
        self.Throttle.setGeometry(QtCore.QRect(1080, 290, 211, 51))
        self.Throttle.setProperty("value", 24)
        self.Throttle.setObjectName(_fromUtf8("Throttle"))
        self.EXIT = QtGui.QPushButton(Form)
        self.EXIT.setGeometry(QtCore.QRect(1190, 690, 99, 27))
        self.EXIT.setObjectName(_fromUtf8("EXIT"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 642, 130, 88))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.GPS = QtGui.QVBoxLayout(self.layoutWidget)
        self.GPS.setMargin(0)
        self.GPS.setObjectName(_fromUtf8("GPS"))
        self.GPS_Name = QtGui.QLabel(self.layoutWidget)
        self.GPS_Name.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.GPS_Name.setFont(font)
        self.GPS_Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GPS_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.GPS_Name.setObjectName(_fromUtf8("GPS_Name"))
        self.GPS.addWidget(self.GPS_Name)
        self.Latitude = QtGui.QHBoxLayout()
        self.Latitude.setObjectName(_fromUtf8("Latitude"))
        self.Latitude_Name = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Latitude_Name.setFont(font)
        self.Latitude_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Latitude_Name.setObjectName(_fromUtf8("Latitude_Name"))
        self.Latitude.addWidget(self.Latitude_Name)
        self.Latitude_LCD = QtGui.QLCDNumber(self.layoutWidget)
        self.Latitude_LCD.setEnabled(True)
        self.Latitude_LCD.setAutoFillBackground(True)
        self.Latitude_LCD.setSmallDecimalPoint(True)
        self.Latitude_LCD.setDigitCount(7)
        self.Latitude_LCD.setObjectName(_fromUtf8("Latitude_LCD"))
        self.Latitude.addWidget(self.Latitude_LCD)
        self.GPS.addLayout(self.Latitude)
        self.Longitude = QtGui.QHBoxLayout()
        self.Longitude.setObjectName(_fromUtf8("Longitude"))
        self.Longitude_Name = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Longitude_Name.setFont(font)
        self.Longitude_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Longitude_Name.setObjectName(_fromUtf8("Longitude_Name"))
        self.Longitude.addWidget(self.Longitude_Name)
        self.Lonigitude_LCD = QtGui.QLCDNumber(self.layoutWidget)
        self.Lonigitude_LCD.setEnabled(True)
        self.Lonigitude_LCD.setAutoFillBackground(True)
        self.Lonigitude_LCD.setSmallDecimalPoint(True)
        self.Lonigitude_LCD.setDigitCount(7)
        self.Lonigitude_LCD.setObjectName(_fromUtf8("Lonigitude_LCD"))
        self.Longitude.addWidget(self.Lonigitude_LCD)
        self.GPS.addLayout(self.Longitude)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 660, 209, 60))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.DATA_1 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.DATA_1.setMargin(0)
        self.DATA_1.setObjectName(_fromUtf8("DATA_1"))
        self.Altitude = QtGui.QHBoxLayout()
        self.Altitude.setObjectName(_fromUtf8("Altitude"))
        self.Altitude_Name = QtGui.QLabel(self.layoutWidget1)
        self.Altitude_Name.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.Altitude_Name.setFont(font)
        self.Altitude_Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Altitude_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Altitude_Name.setObjectName(_fromUtf8("Altitude_Name"))
        self.Altitude.addWidget(self.Altitude_Name)
        self.Altitude_LCD = QtGui.QLCDNumber(self.layoutWidget1)
        self.Altitude_LCD.setEnabled(True)
        self.Altitude_LCD.setAutoFillBackground(True)
        self.Altitude_LCD.setSmallDecimalPoint(True)
        self.Altitude_LCD.setDigitCount(7)
        self.Altitude_LCD.setObjectName(_fromUtf8("Altitude_LCD"))
        self.Altitude.addWidget(self.Altitude_LCD)
        self.Altitude_Units = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Altitude_Units.setFont(font)
        self.Altitude_Units.setAlignment(QtCore.Qt.AlignCenter)
        self.Altitude_Units.setObjectName(_fromUtf8("Altitude_Units"))
        self.Altitude.addWidget(self.Altitude_Units)
        self.DATA_1.addLayout(self.Altitude)
        self.Pressure = QtGui.QHBoxLayout()
        self.Pressure.setObjectName(_fromUtf8("Pressure"))
        self.Pressure_Name = QtGui.QLabel(self.layoutWidget1)
        self.Pressure_Name.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.Pressure_Name.setFont(font)
        self.Pressure_Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Pressure_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Pressure_Name.setObjectName(_fromUtf8("Pressure_Name"))
        self.Pressure.addWidget(self.Pressure_Name)
        self.Pressure_LCD = QtGui.QLCDNumber(self.layoutWidget1)
        self.Pressure_LCD.setEnabled(True)
        self.Pressure_LCD.setAutoFillBackground(True)
        self.Pressure_LCD.setSmallDecimalPoint(True)
        self.Pressure_LCD.setDigitCount(7)
        self.Pressure_LCD.setObjectName(_fromUtf8("Pressure_LCD"))
        self.Pressure.addWidget(self.Pressure_LCD)
        self.Pressure_Units = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Pressure_Units.setFont(font)
        self.Pressure_Units.setAlignment(QtCore.Qt.AlignCenter)
        self.Pressure_Units.setObjectName(_fromUtf8("Pressure_Units"))
        self.Pressure.addWidget(self.Pressure_Units)
        self.DATA_1.addLayout(self.Pressure)
        self.layoutWidget2 = QtGui.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(520, 660, 265, 60))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.Speed = QtGui.QVBoxLayout(self.layoutWidget2)
        self.Speed.setMargin(0)
        self.Speed.setObjectName(_fromUtf8("Speed"))
        self.VERTICAL_SPEED = QtGui.QHBoxLayout()
        self.VERTICAL_SPEED.setObjectName(_fromUtf8("VERTICAL_SPEED"))
        self.Vert_Speed_Name = QtGui.QLabel(self.layoutWidget2)
        self.Vert_Speed_Name.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.Vert_Speed_Name.setFont(font)
        self.Vert_Speed_Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Vert_Speed_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Vert_Speed_Name.setObjectName(_fromUtf8("Vert_Speed_Name"))
        self.VERTICAL_SPEED.addWidget(self.Vert_Speed_Name)
        self.Vert_Speed_LCD = QtGui.QLCDNumber(self.layoutWidget2)
        self.Vert_Speed_LCD.setEnabled(True)
        self.Vert_Speed_LCD.setAutoFillBackground(True)
        self.Vert_Speed_LCD.setSmallDecimalPoint(True)
        self.Vert_Speed_LCD.setDigitCount(7)
        self.Vert_Speed_LCD.setObjectName(_fromUtf8("Vert_Speed_LCD"))
        self.VERTICAL_SPEED.addWidget(self.Vert_Speed_LCD)
        self.Vert_Speed_Units = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Vert_Speed_Units.setFont(font)
        self.Vert_Speed_Units.setAlignment(QtCore.Qt.AlignCenter)
        self.Vert_Speed_Units.setObjectName(_fromUtf8("Vert_Speed_Units"))
        self.VERTICAL_SPEED.addWidget(self.Vert_Speed_Units)
        self.Speed.addLayout(self.VERTICAL_SPEED)
        self.AIR_SPEED = QtGui.QHBoxLayout()
        self.AIR_SPEED.setObjectName(_fromUtf8("AIR_SPEED"))
        self.Air_Speed_Name = QtGui.QLabel(self.layoutWidget2)
        self.Air_Speed_Name.setMinimumSize(QtCore.QSize(16, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.Air_Speed_Name.setFont(font)
        self.Air_Speed_Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Air_Speed_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Air_Speed_Name.setObjectName(_fromUtf8("Air_Speed_Name"))
        self.AIR_SPEED.addWidget(self.Air_Speed_Name)
        self.Air_Speed_LCD = QtGui.QLCDNumber(self.layoutWidget2)
        self.Air_Speed_LCD.setEnabled(True)
        self.Air_Speed_LCD.setAutoFillBackground(True)
        self.Air_Speed_LCD.setSmallDecimalPoint(True)
        self.Air_Speed_LCD.setDigitCount(7)
        self.Air_Speed_LCD.setObjectName(_fromUtf8("Air_Speed_LCD"))
        self.AIR_SPEED.addWidget(self.Air_Speed_LCD)
        self.Air_Speed_Units = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Air_Speed_Units.setFont(font)
        self.Air_Speed_Units.setAlignment(QtCore.Qt.AlignCenter)
        self.Air_Speed_Units.setObjectName(_fromUtf8("Air_Speed_Units"))
        self.AIR_SPEED.addWidget(self.Air_Speed_Units)
        self.Speed.addLayout(self.AIR_SPEED)
        self.layoutWidget3 = QtGui.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(880, 687, 258, 34))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.MODE_DISPLAY = QtGui.QHBoxLayout(self.layoutWidget3)
        self.MODE_DISPLAY.setMargin(0)
        self.MODE_DISPLAY.setObjectName(_fromUtf8("MODE_DISPLAY"))
        self.Mode_Name = QtGui.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Mode_Name.setFont(font)
        self.Mode_Name.setObjectName(_fromUtf8("Mode_Name"))
        self.MODE_DISPLAY.addWidget(self.Mode_Name)
        self.Display = QtGui.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Display.setFont(font)
        self.Display.setObjectName(_fromUtf8("Display"))
        self.MODE_DISPLAY.addWidget(self.Display)
        self.Test = QtGui.QSlider(Form)
        self.Test.setGeometry(QtCore.QRect(1170, 440, 29, 160))
        self.Test.setOrientation(QtCore.Qt.Vertical)
        self.Test.setObjectName(_fromUtf8("Test"))
        self.Frame = QtGui.QLabel(Form)
        self.Frame.setGeometry(QtCore.QRect(10, 10, 832, 624))
        self.Frame.setText(_fromUtf8(""))
        self.Frame.setObjectName(_fromUtf8("Frame"))
        self.Attitude_Image = QtGui.QLabel(Form)
        self.Attitude_Image.setGeometry(QtCore.QRect(850, 10, 210, 210))
        self.Attitude_Image.setText(_fromUtf8(""))
        self.Attitude_Image.setObjectName(_fromUtf8("Attitude_Image"))
        self.Heading_Image = QtGui.QLabel(Form)
        self.Heading_Image.setGeometry(QtCore.QRect(1080, 10, 210, 210))
        self.Heading_Image.setText(_fromUtf8(""))
        self.Heading_Image.setObjectName(_fromUtf8("Heading_Image"))
        self.Turn_Image = QtGui.QLabel(Form)
        self.Turn_Image.setGeometry(QtCore.QRect(850, 290, 210, 53))
        self.Turn_Image.setText(_fromUtf8(""))
        self.Turn_Image.setObjectName(_fromUtf8("Turn_Image"))
        self.Frame_Zoom = QtGui.QLabel(Form)
        self.Frame_Zoom.setGeometry(QtCore.QRect(850, 420, 320, 240))
        self.Frame_Zoom.setText(_fromUtf8(""))
        self.Frame_Zoom.setObjectName(_fromUtf8("Frame_Zoom"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Test, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Battery.setValue)
        QtCore.QObject.connect(self.EXIT, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Attitude_Name.setText(_translate("Form", "Attitude Indicator", None))
        self.Heading_Name.setText(_translate("Form", "Heading Indicator", None))
        self.Turn_Name.setText(_translate("Form", "Turn Indicator", None))
        self.Throttle_Name.setText(_translate("Form", "Throttle Level", None))
        self.Battery_Name.setText(_translate("Form", "Battery", None))
        self.EXIT.setText(_translate("Form", "EXIT", None))
        self.GPS_Name.setText(_translate("Form", "GPS", None))
        self.Latitude_Name.setText(_translate("Form", "Lat :", None))
        self.Longitude_Name.setText(_translate("Form", "Long :", None))
        self.Altitude_Name.setText(_translate("Form", "Altitude :", None))
        self.Altitude_Units.setText(_translate("Form", "ft", None))
        self.Pressure_Name.setText(_translate("Form", "Pressure :", None))
        self.Pressure_Units.setText(_translate("Form", "bar", None))
        self.Vert_Speed_Name.setText(_translate("Form", "Vertical Speed :", None))
        self.Vert_Speed_Units.setText(_translate("Form", "ft/s", None))
        self.Air_Speed_Name.setText(_translate("Form", "Air Speed :", None))
        self.Air_Speed_Units.setText(_translate("Form", "m/s", None))
        self.Mode_Name.setText(_translate("Form", "MODE : ", None))
        self.Display.setText(_translate("Form", "AUTOMATIC", None))

