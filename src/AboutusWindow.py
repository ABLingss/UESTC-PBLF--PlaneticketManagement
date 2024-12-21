# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutusWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutUsWindow(object):
    def setupUi(self, AboutUsWindow):
        AboutUsWindow.setObjectName("AboutUsWindow")
        AboutUsWindow.resize(800, 602)
        self.centralwidget = QtWidgets.QWidget(AboutUsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aboutUsTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.aboutUsTitleLabel.setObjectName("aboutUsTitleLabel")
        self.verticalLayout.addWidget(self.aboutUsTitleLabel)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 750, 500))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(750, 500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setObjectName("scrollAreaLayout")
        self.teamMemberLabel1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.teamMemberLabel1.setObjectName("teamMemberLabel1")
        self.scrollAreaLayout.addWidget(self.teamMemberLabel1)
        self.teamMemberLabel2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.teamMemberLabel2.setObjectName("teamMemberLabel2")
        self.scrollAreaLayout.addWidget(self.teamMemberLabel2)
        self.teamMemberLabel3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.teamMemberLabel3.setObjectName("teamMemberLabel3")
        self.scrollAreaLayout.addWidget(self.teamMemberLabel3)
        self.teamMemberLabel4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.teamMemberLabel4.setObjectName("teamMemberLabel4")
        self.scrollAreaLayout.addWidget(self.teamMemberLabel4)
        self.teamMemberLabel5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.teamMemberLabel5.setObjectName("teamMemberLabel5")
        self.scrollAreaLayout.addWidget(self.teamMemberLabel5)
        self.teamMemberLabel6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.teamMemberLabel6.setObjectName("teamMemberLabel6")
        self.scrollAreaLayout.addWidget(self.teamMemberLabel6)
        self.teamMemberLabel7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.teamMemberLabel7.setObjectName("teamMemberLabel7")
        self.scrollAreaLayout.addWidget(self.teamMemberLabel7)
        self.teamMemberLabel8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.teamMemberLabel8.setObjectName("teamMemberLabel8")
        self.scrollAreaLayout.addWidget(self.teamMemberLabel8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setObjectName("backButton")
        self.buttonLayout.addWidget(self.backButton)
        self.verticalLayout.addLayout(self.buttonLayout)
        AboutUsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutUsWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutUsWindow)

    def retranslateUi(self, AboutUsWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutUsWindow.setStyleSheet(_translate("AboutUsWindow", "QMainWindow {\n"
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
"QLabel {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: none;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    border: 1px solid #ccc;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"    padding: 10px;\n"
"    background-color: #F5F5F5;\n"
"}"))
        self.aboutUsTitleLabel.setText(_translate("AboutUsWindow", "关于我们"))
        self.teamMemberLabel1.setText(_translate("AboutUsWindow", "张三 - 项目经理"))
        self.teamMemberLabel2.setText(_translate("AboutUsWindow", "李四 - 后端开发"))
        self.teamMemberLabel3.setText(_translate("AboutUsWindow", "王五 - 前端开发"))
        self.teamMemberLabel4.setText(_translate("AboutUsWindow", "赵六 - 测试工程师"))
        self.teamMemberLabel5.setText(_translate("AboutUsWindow", "孙七 - UI设计师"))
        self.teamMemberLabel6.setText(_translate("AboutUsWindow", "周八 - 数据分析师"))
        self.teamMemberLabel7.setText(_translate("AboutUsWindow", "吴九 - 系统架构师"))
        self.teamMemberLabel8.setText(_translate("AboutUsWindow", "郑十 - 流程优化专家"))
        self.backButton.setText(_translate("AboutUsWindow", "返回主菜单"))