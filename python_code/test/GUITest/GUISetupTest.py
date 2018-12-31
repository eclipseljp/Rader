"""
@author:caocongcong
"""
import sys
from GUI.GUISetup import GUISetup
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = GUISetup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
