from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Win_Main(object):
    def setupUi(self, Win_Main):
        Win_Main.setObjectName("Win_Main")
        Win_Main.resize(369, 411)
        self.centralwidget = QtWidgets.QWidget(Win_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.AppNameText = QtWidgets.QLabel(self.centralwidget)
        self.AppNameText.setGeometry(QtCore.QRect(10, 10, 351, 71))
        self.AppNameText.setObjectName("AppNameText")
        self.StartupText = QtWidgets.QLabel(self.centralwidget)
        self.StartupText.setGeometry(QtCore.QRect(10, 360, 351, 41))
        self.StartupText.setObjectName("StartupText")
        self.AppName = QtWidgets.QPushButton(self.centralwidget)
        self.AppName.setGeometry(QtCore.QRect(10, 10, 351, 71))
        self.AppName.setStyleSheet("QPushButton {\n"
"    background-color: rgb(31, 31, 31);\n"
"    border: 3px soild rgb(200,200,200);\n"
"    border-radius: 7px;\n"
"    color:  rgb(200,200,200);\n"
"}\n"
"")
        self.AppName.setText("")
        self.AppName.setObjectName("AppName")
        self.StartUp = QtWidgets.QPushButton(self.centralwidget)
        self.StartUp.setGeometry(QtCore.QRect(10, 360, 351, 41))
        self.StartUp.setStyleSheet("QPushButton {\n"
"    background-color: rgb(31, 31, 31);\n"
"    border: 3px soild rgb(200,200,200);\n"
"    border-radius: 7px;\n"
"    color:  rgb(200,200,200);\n"
"}\n"
"")
        self.StartUp.setText("")
        self.StartUp.setObjectName("StartUp")
        self.CreateList_box = QtWidgets.QGroupBox(self.centralwidget)
        self.CreateList_box.setGeometry(QtCore.QRect(10, 90, 351, 261))
        self.CreateList_box.setStyleSheet("QGroupBox {\n"
"    color: rgb(31, 31, 31);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(31, 31, 31);\n"
"}")
        self.CreateList_box.setObjectName("CreateList_box")
        self.Line = QtWidgets.QLabel(self.CreateList_box)
        self.Line.setGeometry(QtCore.QRect(0, 10, 351, 20))
        self.Line.setStyleSheet("QLabel {\n"
"    color: #fff\n"
"}")
        self.Line.setObjectName("Line")
        self.Start_btn = QtWidgets.QPushButton(self.CreateList_box)
        self.Start_btn.setGeometry(QtCore.QRect(70, 210, 211, 31))
        self.Start_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200,200,200);\n"
"    border: 3px soild rgb(200,200,200);\n"
"    border-radius: 5px;\n"
"    color:  rgb(31, 31, 31);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(94, 142, 255);\n"
"    border: 3px soild rgb(200,200,200);\n"
"    border-radius: 5px;\n"
"    color:  rgb(31, 31, 31);\n"
"}")
        self.Start_btn.setObjectName("Start_btn")
        self.minimum_txt = QtWidgets.QLineEdit(self.CreateList_box)
        self.minimum_txt.setGeometry(QtCore.QRect(10, 50, 331, 21))
        self.minimum_txt.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(200,200,200);\n"
"    border: 3px soild rgb(200,200,200);\n"
"    border-radius: 5px;\n"
"    color:  rgb(31, 31, 31);\n"
"}\n"
"")
        self.minimum_txt.setText("")
        self.minimum_txt.setObjectName("minimum_txt")
        self.Name = QtWidgets.QLabel(self.CreateList_box)
        self.Name.setGeometry(QtCore.QRect(0, 0, 351, 20))
        self.Name.setObjectName("Name")
        self.label_1 = QtWidgets.QLabel(self.CreateList_box)
        self.label_1.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.label_1.setObjectName("label_1")
        self.maximum_txt = QtWidgets.QLineEdit(self.CreateList_box)
        self.maximum_txt.setGeometry(QtCore.QRect(10, 100, 331, 21))
        self.maximum_txt.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(200,200,200);\n"
"    border: 3px soild rgb(200,200,200);\n"
"    border-radius: 5px;\n"
"    color:  rgb(31, 31, 31);\n"
"}\n"
"")
        self.maximum_txt.setText("")
        self.maximum_txt.setObjectName("maximum_txt")
        self.label_2 = QtWidgets.QLabel(self.CreateList_box)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.CreateList_box)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 51, 16))
        self.label_3.setObjectName("label_3")
        self.type_txt = QtWidgets.QComboBox(self.CreateList_box)
        self.type_txt.setGeometry(QtCore.QRect(10, 150, 331, 22))
        self.type_txt.setStyleSheet("* {\n"
"    background-color: rgb(200,200,200);\n"
"    border: 3px soild rgb(200,200,200);\n"
"    border-radius: 5px;\n"
"    color:  rgb(31, 31, 31);\n"
"}\n"
"")
        self.type_txt.setObjectName("type_txt")
        self.type_txt.addItem("")
        self.type_txt.addItem("")
        self.type_txt.addItem("")
        self.AppName.raise_()
        self.StartUp.raise_()
        self.CreateList_box.raise_()
        self.AppNameText.raise_()
        self.StartupText.raise_()
        Win_Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Win_Main)
        QtCore.QMetaObject.connectSlotsByName(Win_Main)

    def retranslateUi(self, Win_Main):
        _translate = QtCore.QCoreApplication.translate
        Win_Main.setWindowTitle(_translate("Win_Main", "CTL"))
        self.AppNameText.setText(_translate("Win_Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">C</span><span style=\" font-size:36pt; color:#ffffff; vertical-align:sub;\">T</span><span style=\" font-size:36pt; color:#ffffff;\">L</span></p></body></html>"))
        self.StartupText.setText(_translate("Win_Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Sbez Loop </span><span style=\" font-size:16pt; color:#ffffff; vertical-align:sub;\">SPY</span></p></body></html>"))
        self.CreateList_box.setTitle(_translate("Win_Main", "-"))
        self.Line.setText(_translate("Win_Main", "<html><head/><body><p align=\"center\">ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ</p></body></html>"))
        self.Start_btn.setText(_translate("Win_Main", "Start"))
        self.Name.setText(_translate("Win_Main", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Create List</span></p></body></html>"))
        self.label_1.setText(_translate("Win_Main", "<html><head/><body><p><span style=\" color:#ffffff;\">Minimum lenght :</span></p></body></html>"))
        self.label_2.setText(_translate("Win_Main", "<html><head/><body><p><span style=\" color:#ffffff;\">Maximum lenght :</span></p></body></html>"))
        self.label_3.setText(_translate("Win_Main", "<html><head/><body><p><span style=\" color:#ffffff;\">Type :</span></p></body></html>"))
        self.type_txt.setItemText(0, _translate("Win_Main", "Number"))
        self.type_txt.setItemText(1, _translate("Win_Main", "Charaters"))
        self.type_txt.setItemText(2, _translate("Win_Main", "Marks"))