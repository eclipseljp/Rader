"""
@author:caocongcong
为图形界面增加事件
"""
from GUI.CreateRadarGUI import Ui_Dialog
class CreateRadarwithEventGUI(Ui_Dialog):
    def __init__(self, Dialog):
        super().setupUi(Dialog)
        self.LFM.stateChanged.connect(self.LFM_state_change())
        self.single_fs.stateChanged.connect(self.single_fs_change_state())

    # 保存按钮的函数
    def saveEvent(self):
        pass

    # 取消按钮的函数
    def cancelEvent(self):
        pass

    # LFM state change 函数
    def LFM_state_change(self):
        print("LFM status change")
        if self.LFM.isChecked():
            self.LFM_checked()
        else:
            self.LFM_unchecked()
    # LFM checked所对应的函数
    def LFM_checked(self):
        self.fs_type.
        ()
        self.fs_type.setDisabled()

    # LFM取消checked
    def LFM_unchecked(self):
        self.single_fs.setEnabled()
        self.fs_type.setEnabled()

    # single_fs_change_state
    def single_fs_change_state(self):
        if self.single_fs.isChecked():
            self.single_fs_checked()
        else:
            self.single_fs_unchecked()

    # single_fs checked所对应的函数
    def single_fs_checked(self):
        self.LFM.setDisabled()
        self.lfm_type.setDisabled()

    # single_fs_unchecked所对应的函数
    def single_fs_unchecked(self):
        self.LFM.setEnabled()
        self.lfm_type.setEnabled()

