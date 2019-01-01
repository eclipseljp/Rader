"""
@author:caocongcong
"""
from GUI.mainGUI import Ui_MainWindow
from GUI.CreateRadarwithEventGUI import CreateRadarwithEventGUI
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from GUI.CreateRadarDialog import SaveDialog
class GUISetup(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.create_radar.clicked.connect(self.addSignalEvent)
        self.create_ra

    def addSignalEvent(self):
        dialog = SaveDialog(self)
        dialog.show()







