"""
@author:caocongcong
"""
import sys
from GUI.CreateRadarwithEventGUI import CreateRadarwithEventGUI
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = CreateRadarwithEventGUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())