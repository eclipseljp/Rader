"""
@author:caocongcong
为图形界面增加事件
"""
from GUI.CreateRadarGUI import Ui_Dialog
from constant.SignalTypeEnum import signal_type
from constant.PriTypeEnum import pri_type
from constant.FsTypeEnum import fs_type
from model.createRadarVo import createRadarVo
from PyQt5.QtWidgets import QDialog


class CreateRadarwithEventGUI(QDialog, Ui_Dialog):
    def __init__(self):
        super(CreateRadarwithEventGUI, self).__init__()
        self.setupUi(self)
        self.LFM.stateChanged.connect(self.LFM_state_change)
        self.single_fs.stateChanged.connect(self.single_fs_change_state)
        self.sure.clicked.connect(self.saveEvent)
        self.pushButton_2.clicked.connect(self.cancelEvent)
        self.signal_type = None

    # 保存按钮的函数
    def saveEvent(self):
        radar_id = self.radar_sn.text()
        radar_name = self.radar_name.text()
        input_fs_type = None
        if self.signal_type == signal_type.single_fs:
            input_fs_type = fs_type(self.fs_type.currentText())
        else:
            input_fs_type = fs_type(self.lfm_type.currentText())
        input_pri_type = pri_type(self.pri_type.currentText())
        self.createdRadar = createRadarVo(radar_id, radar_name, input_fs_type, input_pri_type)
        self.accept()

    # 重载退出函数
    def exec_(self):
        super(CreateRadarwithEventGUI, self).exec_()
        return self.createdRadar
    # 取消按钮的函数
    def cancelEvent(self):
        self.reject()

    # LFM state change 函数
    def LFM_state_change(self):
        if self.LFM.isChecked():
            self.LFM_checked()
        else:
            self.LFM_unchecked()

    # LFM checked所对应的函数
    def LFM_checked(self):
        self.signal_type = signal_type.LFM
        self.fs_type.setDisabled(True)
        self.fs_type.setDisabled(True)

    # LFM取消checked
    def LFM_unchecked(self):
        self.single_fs.setEnabled(True)
        self.fs_type.setEnabled(True)

    # single_fs_change_state
    def single_fs_change_state(self):
        if self.single_fs.isChecked():
            self.single_fs_checked()
        else:
            self.single_fs_unchecked()

    # single_fs checked所对应的函数
    def single_fs_checked(self):
        self.signal_type = signal_type.single_fs
        self.LFM.setDisabled(True)
        self.lfm_type.setDisabled(True)

    # single_fs_unchecked所对应的函数
    def single_fs_unchecked(self):
        self.LFM.setEnabled(True)
        self.lfm_type.setEnabled(True)
