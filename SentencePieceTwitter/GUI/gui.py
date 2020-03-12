# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(77, 200, 241);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 140, 801, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 110, 41))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 320, 110, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(214, 203, 48);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 370, 801, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 320, 151, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(120, -20, 511, 154))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("bird.png"))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
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
        self.pushButton_3.setText(_translate("MainWindow", "Change Model"))
        self.label.setText(_translate("MainWindow", "SentenceTweet"))
        self.actionNew_file.setText(_translate("MainWindow", "New file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
