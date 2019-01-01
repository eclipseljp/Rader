"""
@author:caocongcong
"""
from GUI.mainGUI import Ui_MainWindow
from GUI.CreateRadarwithEventGUI import CreateRadarwithEventGUI
from PyQt5.QtWidgets import QMainWindow
class GUISetup(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.create_radar_dialog = CreateRadarwithEventGUI()
        self.main_ui.create_radar.clicked.connect(self.addSignalEvent)

    def addSignalEvent(self):
        self.create_radar_dialog.show()
        value = self.create_radar_dialog.exec_()
        if value:
            print(value.radar_id)









