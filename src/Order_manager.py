# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Order_manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OrderEditWindow(object):
    def setupUi(self, OrderEditWindow):
        OrderEditWindow.setObjectName("OrderEditWindow")
        OrderEditWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(OrderEditWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editOrderTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.editOrderTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editOrderTitleLabel.setObjectName("editOrderTitleLabel")
        self.verticalLayout.addWidget(self.editOrderTitleLabel)
        self.orderNumberLayout = QtWidgets.QHBoxLayout()
        self.orderNumberLayout.setObjectName("orderNumberLayout")
        self.orderNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.orderNumberLabel.setObjectName("orderNumberLabel")
        self.orderNumberLayout.addWidget(self.orderNumberLabel)
        self.orderNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.orderNumberLineEdit.setObjectName("orderNumberLineEdit")
        self.orderNumberLayout.addWidget(self.orderNumberLineEdit)
        self.verticalLayout.addLayout(self.orderNumberLayout)
        self.flightNumberLayout = QtWidgets.QHBoxLayout()
        self.flightNumberLayout.setObjectName("flightNumberLayout")
        self.flightNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.flightNumberLabel.setObjectName("flightNumberLabel")
        self.flightNumberLayout.addWidget(self.flightNumberLabel)
        self.flightNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.flightNumberLineEdit.setObjectName("flightNumberLineEdit")
        self.flightNumberLayout.addWidget(self.flightNumberLineEdit)
        self.verticalLayout.addLayout(self.flightNumberLayout)
        self.seatNumberLayout = QtWidgets.QHBoxLayout()
        self.seatNumberLayout.setObjectName("seatNumberLayout")
        self.seatNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.seatNumberLabel.setObjectName("seatNumberLabel")
        self.seatNumberLayout.addWidget(self.seatNumberLabel)
        self.seatNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.seatNumberLineEdit.setObjectName("seatNumberLineEdit")
        self.seatNumberLayout.addWidget(self.seatNumberLineEdit)
        self.verticalLayout.addLayout(self.seatNumberLayout)
        self.orderStatusLayout = QtWidgets.QHBoxLayout()
        self.orderStatusLayout.setObjectName("orderStatusLayout")
        self.orderStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.orderStatusLabel.setObjectName("orderStatusLabel")
        self.orderStatusLayout.addWidget(self.orderStatusLabel)
        self.orderStatusLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.orderStatusLineEdit.setObjectName("orderStatusLineEdit")
        self.orderStatusLayout.addWidget(self.orderStatusLineEdit)
        self.verticalLayout.addLayout(self.orderStatusLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.saveOrderButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveOrderButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveOrderButton.setObjectName("saveOrderButton")
        self.buttonLayout.addWidget(self.saveOrderButton)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setObjectName("backButton")
        self.buttonLayout.addWidget(self.backButton)
        self.verticalLayout.addLayout(self.buttonLayout)
        OrderEditWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OrderEditWindow)
        QtCore.QMetaObject.connectSlotsByName(OrderEditWindow)

    def retranslateUi(self, OrderEditWindow):
        _translate = QtCore.QCoreApplication.translate
        OrderEditWindow.setStyleSheet(_translate("OrderEditWindow", "QMainWindow {\n"
"    background-color: #F5F5F5;\n"
"    font-family: \'Segoe UI\', sans-serif;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #0078D7;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    min-width: 150px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005FAC;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"}"))
        self.editOrderTitleLabel.setStyleSheet(_translate("OrderEditWindow", "font-size: 20px; font-weight: bold; color: #333;"))
        self.editOrderTitleLabel.setText(_translate("OrderEditWindow", "编辑订单信息"))
        self.orderNumberLabel.setText(_translate("OrderEditWindow", "订单号："))
        self.orderNumberLineEdit.setPlaceholderText(_translate("OrderEditWindow", "修改订单号"))
        self.flightNumberLabel.setText(_translate("OrderEditWindow", "航班号："))
        self.flightNumberLineEdit.setPlaceholderText(_translate("OrderEditWindow", "修改航班号"))
        self.seatNumberLabel.setText(_translate("OrderEditWindow", "座位号："))
        self.seatNumberLineEdit.setPlaceholderText(_translate("OrderEditWindow", "修改座位号"))
        self.orderStatusLabel.setText(_translate("OrderEditWindow", "订单状态："))
        self.orderStatusLineEdit.setPlaceholderText(_translate("OrderEditWindow", "修改订单状态"))
        self.saveOrderButton.setText(_translate("OrderEditWindow", "保存修改"))
        self.backButton.setText(_translate("OrderEditWindow", "返回上一页"))
