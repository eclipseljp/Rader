"""
@author:caocongcong
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.ConfigRadarDetials import ConfigRadarDetials
from constant.FsTypeEnum import fs_type
from constant.PriTypeEnum import pri_type

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ConfigRadarDetials(pri_type.pri_group, fs_type.fs_big_band_lfm)
    ui.show()
    sys.exit(app.exec_())