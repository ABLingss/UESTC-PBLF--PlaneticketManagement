# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Profile_manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileManagementWindow(object):
    def setupUi(self, ProfileManagementWindow):
        ProfileManagementWindow.setObjectName("ProfileManagementWindow")
        ProfileManagementWindow.resize(800, 602)
        self.centralwidget = QtWidgets.QWidget(ProfileManagementWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.profileTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.profileTitleLabel.setObjectName("profileTitleLabel")
        self.verticalLayout.addWidget(self.profileTitleLabel)
        self.currentInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentInfoLabel.setObjectName("currentInfoLabel")
        self.verticalLayout.addWidget(self.currentInfoLabel)
        self.currentInfoLayout = QtWidgets.QVBoxLayout()
        self.currentInfoLayout.setObjectName("currentInfoLayout")
        self.currentUsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentUsernameLabel.setObjectName("currentUsernameLabel")
        self.currentInfoLayout.addWidget(self.currentUsernameLabel)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.currentInfoLayout.addWidget(self.label)
        self.currentEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentEmailLabel.setObjectName("currentEmailLabel")
        self.currentInfoLayout.addWidget(self.currentEmailLabel)
        self.currentPhoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentPhoneLabel.setObjectName("currentPhoneLabel")
        self.currentInfoLayout.addWidget(self.currentPhoneLabel)
        self.verticalLayout.addLayout(self.currentInfoLayout)
        self.editInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.editInfoLabel.setObjectName("editInfoLabel")
        self.verticalLayout.addWidget(self.editInfoLabel)
        self.usernameLayout = QtWidgets.QHBoxLayout()
        self.usernameLayout.setObjectName("usernameLayout")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLayout.addWidget(self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.usernameLayout.addWidget(self.usernameLineEdit)
        self.verticalLayout.addLayout(self.usernameLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.IDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IDLineEdit.setObjectName("IDLineEdit")
        self.horizontalLayout_2.addWidget(self.IDLineEdit)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.emailLayout = QtWidgets.QHBoxLayout()
        self.emailLayout.setObjectName("emailLayout")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setObjectName("emailLabel")
        self.emailLayout.addWidget(self.emailLabel)
        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.emailLayout.addWidget(self.emailLineEdit)
        self.verticalLayout.addLayout(self.emailLayout)
        self.phoneLayout = QtWidgets.QHBoxLayout()
        self.phoneLayout.setObjectName("phoneLayout")
        self.phoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.phoneLabel.setObjectName("phoneLabel")
        self.phoneLayout.addWidget(self.phoneLabel)
        self.phoneLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.phoneLayout.addWidget(self.phoneLineEdit)
        self.verticalLayout.addLayout(self.phoneLayout)
        self.passwordLayout = QtWidgets.QHBoxLayout()
        self.passwordLayout.setObjectName("passwordLayout")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordLayout.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLayout.addWidget(self.passwordLineEdit)
        self.verticalLayout.addLayout(self.passwordLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.buttonLayout.addWidget(self.saveButton)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.buttonLayout.addWidget(self.backButton)
        self.verticalLayout.addLayout(self.buttonLayout)
        ProfileManagementWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfileManagementWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileManagementWindow)

    def retranslateUi(self, ProfileManagementWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileManagementWindow.setStyleSheet(_translate("ProfileManagementWindow", "QMainWindow {\n"
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
"}\n"
"\n"
"QTextEdit {\n"
"    border: 1px solid #ccc;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"    padding: 10px;\n"
"}"))
        self.profileTitleLabel.setText(_translate("ProfileManagementWindow", "修改个人信息"))
        self.currentInfoLabel.setText(_translate("ProfileManagementWindow", "当前信息："))
        self.currentUsernameLabel.setText(_translate("ProfileManagementWindow", "用户名：user01"))
        self.label.setText(_translate("ProfileManagementWindow", "身份证号：123456790-="))
        self.currentEmailLabel.setText(_translate("ProfileManagementWindow", "邮箱：user01@example.com"))
        self.currentPhoneLabel.setText(_translate("ProfileManagementWindow", "手机号：12345678901"))
        self.editInfoLabel.setText(_translate("ProfileManagementWindow", "修改信息："))
        self.usernameLabel.setText(_translate("ProfileManagementWindow", "用户名："))
        self.usernameLineEdit.setPlaceholderText(_translate("ProfileManagementWindow", "修改用户名（留空表示不修改）"))
        self.label_2.setText(_translate("ProfileManagementWindow", "TextLabel"))
        self.IDLineEdit.setPlaceholderText(_translate("ProfileManagementWindow", "修改用户名（留空表示不修改）"))
        self.emailLabel.setText(_translate("ProfileManagementWindow", "邮箱："))
        self.emailLineEdit.setPlaceholderText(_translate("ProfileManagementWindow", "修改邮箱地址（留空表示不修改）"))
        self.phoneLabel.setText(_translate("ProfileManagementWindow", "手机号："))
        self.phoneLineEdit.setPlaceholderText(_translate("ProfileManagementWindow", "修改手机号（留空表示不修改）"))
        self.passwordLabel.setText(_translate("ProfileManagementWindow", "修改密码："))
        self.passwordLineEdit.setPlaceholderText(_translate("ProfileManagementWindow", "输入新密码（留空表示不修改）"))
        self.saveButton.setText(_translate("ProfileManagementWindow", "保存修改"))
        self.backButton.setText(_translate("ProfileManagementWindow", "返回上一页"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileManagementWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfileManagementWindow()
    ui.setupUi(ProfileManagementWindow)
    ProfileManagementWindow.show()
    sys.exit(app.exec_())