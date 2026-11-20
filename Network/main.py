# pip install PySide6 scapy psutil matplotlib pyqtgraph pandas numpy requests netifaces python-dotenv pytest black ruff
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import psutil
import socket

for interface, addresses in psutil.net_if_addrs().items():
    for address in addresses:
        if address.family == socket.AF_INET:
            print(interface, address.address)
# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)
        
        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.text)
        

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
