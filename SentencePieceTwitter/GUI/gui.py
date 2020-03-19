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
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 140, 841, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 140, 131, 41))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 190, 131, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(214, 203, 48);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 370, 841, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(222, 222, 222);\n"
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
        self.line.setGeometry(QtCore.QRect(10, 340, 831, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(842, 140, 21, 421))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(860, 250, 131, 41))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(250, 211, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 310, 131, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 165, 162);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 77, 21))
        self.label_4.setObjectName("label_4")
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
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "SentenceTweet"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Words"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Prefixes"))
        self.pushButton_3.setText(_translate("MainWindow", "Change Model \n"
"Words"))
        self.label_3.setText(_translate("MainWindow", "Insert Tweets"))
        self.label_4.setText(_translate("MainWindow", "Output"))
        self.actionNew_file.setText(_translate("MainWindow", "New file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
