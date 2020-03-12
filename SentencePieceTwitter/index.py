from GUI.gui import *
import sentencepiece as sp

from PyQt5.QtWidgets import QFileDialog


class myGUI(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.modelPath = "Model/m_word.model"
		
		#My method
		self.pushButton.clicked.connect(self.letsTknzr)
		
		#Open File
		#self.pushButton_3.clicked.connect(self.openFile)
		
	def letsTknzr(self):
		#--- Charging model Sentence Piece ---
		spWord = sp.SentencePieceProcessor()
		spWord.load(self.modelPath)
		
		tkzed = str(spWord.encode_as_pieces(self.plainTextEdit.toPlainText()))
		self.plainTextEdit_2.setPlainText(tkzed)

	"""
	def openFile(self):
		print(QtWidgets)
		name = QtWidgets.QfileDialog.getOpenFileName(self, 'Open File')
		file = open(name, 'r')
		with file:
			text = file.read()
			print(text)
	"""

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = myGUI()
    window.show()
    app.exec_()
