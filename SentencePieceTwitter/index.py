#Carlos Esteban Murillo S. 1526857

from GUI.gui import *

import sentencepiece as sp
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class myGUI(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.modelWordPath = 'Model/m_word.model'
		self.modelPrefixesPath = 'Model/m_user.model'
		self.modelPath = self.modelWordPath
		self.sel = True
		
		#My method
		self.pushButton.clicked.connect(self.letsTknzr)
		
		#Combo box method
		self.comboBox.currentIndexChanged.connect(self.selectionchange)
		
		#Open File
		self.pushButton_3.clicked.connect(self.openFile)
		
	def letsTknzr(self):
		
		#--- Charging model Sentence Piece ---
		spp = sp.SentencePieceProcessor()
		spp.load(self.modelPath)
		
		tkzed = spp.encode_as_pieces(self.plainTextEdit.toPlainText())
		output = self.cleanFormat(tkzed)
		self.plainTextEdit_2.setPlainText(output)
		
	def cleanFormat(self, tkzed):
		for i in range(len(tkzed)):
			tkzed[i] = tkzed[i].replace("▁", " ")
		
		aux = str(tkzed)
		aux = aux.replace("', '", " | ")
		return aux

	def selectionchange(self, i):
		
		if(i == 0):
			self.modelPath = self.modelWordPath
			self.pushButton_3.setText("Change Model \nWords")
			self.sel = True
		else:
			self.modelPath = self.modelPrefixesPath
			self.pushButton_3.setText("Change Model \nPrefixes")
			self.sel = False
	
	def openFile(self):
		
		Tk().withdraw()
		filename = askopenfilename()
		if filename:
			if(self.sel):
				self.modelWordPath = filename
			else:
				self.modelPrefixesPath = filename
			self.modelPath = filename

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = myGUI()
    window.show()
    app.exec_()
