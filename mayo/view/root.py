from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentWindow

class Root(FluentWindow):
    def __init__(self):
        super().__init__()
        self.init_window()
    
    def init_window(self):
        self.resize(800, 600)
        self.setMinimumWidth(750)
        self.setWindowTitle('Mayo')

        self.show()
        QApplication.processEvents()