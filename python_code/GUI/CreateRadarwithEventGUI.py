"""
@author:caocongcong
为图形界面增加事件
"""
from GUI.CreateRadarGUI import Ui_Dialog
from PyQt5.QtWidgets import QMessageBox
from model.createRadarVo import createRadarVo
class CreateRadarwithEventGUI(Ui_Dialog):
    def __init__(self, Dialog):
        super().setupUi(Dialog)
        self.LFM.stateChanged.connect(self.LFM_state_change)
        self.single_fs.stateChanged.connect(self.single_fs_change_state)
        self.sure.clicked.connect(self.saveEvent)

    # 保存按钮的函数
    def saveEvent(self):
        self.check_value()
        radar_id = self.radar_sn.text()
        radar_name = self.radar_name.text()
        # todo
        # 进行验证



    # 取消按钮的函数
    def cancelEvent(self):
        pass

    # LFM state change 函数
    def LFM_state_change(self):
        if self.LFM.isChecked():
            self.LFM_checked()
        else:
            self.LFM_unchecked()

    # LFM checked所对应的函数
    def LFM_checked(self):
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
        self.LFM.setDisabled(True)
        self.lfm_type.setDisabled(True)

    # single_fs_unchecked所对应的函数
    def single_fs_unchecked(self):
        self.LFM.setEnabled(True)
        self.lfm_type.setEnabled(True)

