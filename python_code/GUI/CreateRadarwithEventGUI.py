"""
@author:caocongcong
为图形界面增加事件
"""
from GUI.CreateRadarGUI import Ui_Dialog
from constant.SignalTypeEnum import signal_type
from constant.PriTypeEnum import pri_type
from constant.FsTypeEnum import fs_type
from model.createRadarVo import createRadarVo
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDialog


class CreateRadarwithEventGUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
        self.dialog.LFM.stateChanged.connect(self.LFM_state_change)
        self.dialog.single_fs.stateChanged.connect(self.single_fs_change_state)
        self.dialog.sure.clicked.connect(self.saveEvent)
        self.dialog.pushButton_2.clicked.connect(self.cancelEvent)
        self.signal_type = None

    # 保存按钮的函数
    def saveEvent(self):
        radar_id = self.dialog.radar_sn.text()
        radar_name = self.dialog.radar_name.text()
        input_fs_type = None
        if self.signal_type == signal_type.single_fs:
            input_fs_type = fs_type(self.dialog.fs_type.currentText())
        else:
            input_fs_type = fs_type(self.dialog.lfm_type.currentText())
        input_pri_type = pri_type(self.dialog.pri_type.currentText())
        self.createdRadar = createRadarVo(radar_id, radar_name, input_fs_type, input_pri_type)
        print(self.createdRadar)
        QCoreApplication.instance().quit()

    # 取消按钮的函数
    def cancelEvent(self):
        QCoreApplication.instance().quit()

    # LFM state change 函数
    def LFM_state_change(self):
        if self.dialog.LFM.isChecked():
            self.LFM_checked()
        else:
            self.LFM_unchecked()

    # LFM checked所对应的函数
    def LFM_checked(self):
        self.dialog.signal_type = signal_type.LFM
        self.dialog.fs_type.setDisabled(True)
        self.dialog.fs_type.setDisabled(True)

    # LFM取消checked
    def LFM_unchecked(self):
        self.single_fs.setEnabled(True)
        self.fs_type.setEnabled(True)

    # single_fs_change_state
    def single_fs_change_state(self):
        if self.dialog.single_fs.isChecked():
            self.single_fs_checked()
        else:
            self.single_fs_unchecked()

    # single_fs checked所对应的函数
    def single_fs_checked(self):
        self.dialog.signal_type = signal_type.single_fs
        self.dialog.LFM.setDisabled(True)
        self.dialog.lfm_type.setDisabled(True)

    # single_fs_unchecked所对应的函数
    def single_fs_unchecked(self):
        self.dialog.LFM.setEnabled(True)
        self.dialog.lfm_type.setEnabled(True)
