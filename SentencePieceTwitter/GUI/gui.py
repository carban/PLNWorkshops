# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        MainWindow.setStyleSheet("background-color: rgb(77, 200, 241);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 140, 831, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color: rgb(19, 23, 255);\n"
"border-radius: 20px;\n"
"")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 180, 131, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("#pushButton {\n"
"  background-color: #4CAF50; \n"
"  color: black; \n"
"  border: none ;\n"
"}\n"
"\n"
"#pushButton:hover {\n"
"  background-color: rgb(66, 255, 24);\n"
"}\n"
"")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 240, 131, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("#pushButton_2 {\n"
"  background-color: rgb(223, 210, 60);\n"
"  color: black; \n"
"  border: none ;\n"
"}\n"
"\n"
"#pushButton_2:hover {\n"
"  background-color: rgb(255, 248, 35);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 360, 831, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color: rgb(19, 23, 255);\n"
"border-radius: 20px;\n"
"")
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(240, -20, 511, 154))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("GUI/../bird.png"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 330, 831, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(842, 140, 21, 421))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(860, 300, 131, 41))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("#comboBox {\n"
"  background-color: rgb(255, 209, 156);\n"
"  color: black; \n"
"  border: none ;\n"
"}\n"
"\n"
"#comboBox:hover {\n"
"  background-color: rgb(255, 164, 85);\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 360, 131, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("#pushButton_3 {\n"
"  background-color: rgb(255, 157, 172);\n"
"  color: black; \n"
"  border: none ;\n"
"}\n"
"\n"
"#pushButton_3:hover {\n"
"  background-color: rgb(255, 73, 246);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 330, 77, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(890, 140, 77, 21))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_file = QtWidgets.QAction(MainWindow)
        self.actionNew_file.setObjectName("actionNew_file")

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.plainTextEdit.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SentenceTweet"))
        self.pushButton.setText(_translate("MainWindow", "Tokenize"))
        self.pushButton_2.setText(_translate("MainWindow", "Clean"))
        self.label.setText(_translate("MainWindow", "SentenceTweet"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Words"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Prefixes"))
        self.pushButton_3.setText(_translate("MainWindow", "Change Model \n"
"Words"))
        self.label_3.setText(_translate("MainWindow", "Insert Tweets"))
        self.label_4.setText(_translate("MainWindow", "Output"))
        self.label_5.setText(_translate("MainWindow", "Options"))
        self.actionNew_file.setText(_translate("MainWindow", "New file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
