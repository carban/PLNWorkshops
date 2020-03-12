After installing PyQt and QtDesigner, you will design your gui wtih QtDesigner environment. For translate the .ui file to a .py file you must write in your terminal: 

`$ pyuic5 -x gui.ui -o gui.py`

Later, you will need a index.py file for controlling logic and gui. Here is an example

```python
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
