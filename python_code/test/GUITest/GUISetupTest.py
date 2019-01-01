"""
@author:caocongcong
"""
import sys
from GUI.GUISetup import GUISetup
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = GUISetup()
    ui.show()
    sys.exit(app.exec_())
