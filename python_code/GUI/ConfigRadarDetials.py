"""
@author:caocongcong
"""
from PyQt5.QtWidgets import QDialog, QLabel, QFrame, QPushButton


class ConfigRadarDetials(QDialog):
    def __init__(self, pri_type, fs_type):
        super(ConfigRadarDetials, self).__init__()
        self.resize(400, 500)
        frameStyle = QFrame.Sunken | QFrame.Panel

        self.pulse_width_label = QLabel()
        self.pulse_width_label.setFrameStyle(frameStyle)
        self.pulse_width_button = QPushButton("选择脉宽")

        self.DOC__label = QLabel()
        self.DOC_label.setFrameStyle(frameStyle)
        self.DOC_button = QPushButton("选择到达角")

        self.pri_value_label =