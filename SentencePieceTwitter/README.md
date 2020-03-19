# Tokenize with Sentence Piece

Sentecepiece uses a non supervised method for sentences tokenization. On this workshop I implemented a sentences tokenization through <b>word</b> and <b>prefixes</b> models. the last one allows users model using the tags < sep >, < cls > (BERT).

For install the requirements for this workshop you need PyQt5 and sentnecepiece packages.

`$ pip3 install pyqt5 pyqt5-tools`

`$ pip3 install sentencepiece`

For execute the gui, run index file with `$ python3 index.py`

# Instructions For build GUI by Qt (Python)

After installing PyQt and QtDesigner, you will design your gui wtih QtDesigner environment. For translate the .ui file to a .py file you must write in your terminal: 

`$ pyuic5 -x gui.ui -o gui.py`

Later, you will need a index.py file for controlling logic and gui. Here is an example

```python
# GUI folder who contains gui.py file
from GUI.gui import *

class myGUI(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
    
		#My method
		self.pushButton.clicked.connect(self.hello)
	
	def hello(self):
		print("Hello")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = myGUI()
    window.show()
    app.exec_()
    ```
