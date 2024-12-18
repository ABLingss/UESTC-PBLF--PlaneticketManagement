# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_flights.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FlightSearchWindow(object):
    def setupUi(self, FlightSearchWindow):
        FlightSearchWindow.setObjectName("FlightSearchWindow")
        FlightSearchWindow.resize(972, 635)
        self.centralwidget = QtWidgets.QWidget(FlightSearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchLayout = QtWidgets.QHBoxLayout()
        self.searchLayout.setObjectName("searchLayout")
        self.departureLabel = QtWidgets.QLabel(self.centralwidget)
        self.departureLabel.setObjectName("departureLabel")
        self.searchLayout.addWidget(self.departureLabel)
        self.departureComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.departureComboBox.setObjectName("departureComboBox")
        self.searchLayout.addWidget(self.departureComboBox)
        self.destinationLabel = QtWidgets.QLabel(self.centralwidget)
        self.destinationLabel.setObjectName("destinationLabel")
        self.searchLayout.addWidget(self.destinationLabel)
        self.destinationComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.destinationComboBox.setObjectName("destinationComboBox")
        self.searchLayout.addWidget(self.destinationComboBox)
        self.departureTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.departureTimeLabel.setObjectName("departureTimeLabel")
        self.searchLayout.addWidget(self.departureTimeLabel)
        self.departureTimeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.departureTimeComboBox.setObjectName("departureTimeComboBox")
        self.searchLayout.addWidget(self.departureTimeComboBox)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.searchLayout.addWidget(self.searchButton)
        self.verticalLayout.addLayout(self.searchLayout)
        self.flightTable = QtWidgets.QTableWidget(self.centralwidget)
        self.flightTable.setRowCount(0)
        self.flightTable.setColumnCount(4)
        self.flightTable.setProperty("horizontalHeaderLabels", ['航班号', '出发地', '目的地', '出发时间'])
        self.flightTable.setObjectName("flightTable")
        self.verticalLayout.addWidget(self.flightTable)
        self.backToMainButton = QtWidgets.QPushButton(self.centralwidget)
        self.backToMainButton.setObjectName("backToMainButton")
        self.verticalLayout.addWidget(self.backToMainButton)
        self.verticalLayout.setStretch(1, 1)
        FlightSearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FlightSearchWindow)
        QtCore.QMetaObject.connectSlotsByName(FlightSearchWindow)

    def retranslateUi(self, FlightSearchWindow):
        _translate = QtCore.QCoreApplication.translate
        FlightSearchWindow.setStyleSheet(_translate("FlightSearchWindow", "QMainWindow {\n"
"    background-color: #F0F0F0;\n"
"    font-family: \'Segoe UI\', sans-serif;\n"
"}\n"
"\n"
"QComboBox, QPushButton, QTableWidget {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #0078D7;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005FAC;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    border: 1px solid #ccc;\n"
"    color: #333;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"    border-bottom: 1px solid #ccc;\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"    background-color: #0078D7;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader::section {\n"
"    border: 1px solid #ccc;\n"
"    border-style: none;\n"
"}"))
        self.departureLabel.setText(_translate("FlightSearchWindow", "出发地:"))
        self.destinationLabel.setText(_translate("FlightSearchWindow", "目的地:"))
        self.departureTimeLabel.setText(_translate("FlightSearchWindow", "出发时间:"))
        self.searchButton.setText(_translate("FlightSearchWindow", "查询"))
        self.backToMainButton.setText(_translate("FlightSearchWindow", "返回主界面"))
