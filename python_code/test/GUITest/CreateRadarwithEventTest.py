"""
@author:caocongcong
"""
import sys
from GUI import CreateRadarwithEventGUI
from PyQt5.QtWidgets import QApplication, QDialog
if __name__ == "__main__":
    app = QApplication(sys.argv)
    qDialog = QDialog()
    ui = CreateRadarwithEventGUI.Ui_Dialog()
    ui.setupUi(qDialog)
    qDialog.show()
    sys.exit(app.exec_())