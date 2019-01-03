"""
@author:caocongcong
"""
from PyQt5.QtWidgets import QDialog, QLabel, QGroupBox, QFormLayout, QLineEdit, QDialogButtonBox, QVBoxLayout
from constant.PriTypeEnum import pri_type
from constant.FsTypeEnum import fs_type

class ConfigRadarDetials(QDialog):
    def __init__(self, pri_type, fs_type):
        super(ConfigRadarDetials, self).__init__()
        self.setWindowTitle("雷达参数输入")

        self.createForm(pri_type, fs_type)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)


    def createForm(self, input_pri_type, input_fs_type):
        self.formGroupBox = QGroupBox("参数设置")
        layout = QFormLayout()
        self.plue_width = QLineEdit()
        layout.addRow(QLabel("脉宽(us):"), self.plue_width)
        self.DOA = QLineEdit()
        layout.addRow(QLabel("到达角:"), self.DOA)
        self.pri_value = QLineEdit()
        layout.addRow(QLabel("脉冲重复间隔(us)"), self.pri_value)
        if input_pri_type != pri_type.pri_fixed:
            self.pri_jetter = QLineEdit()
            layout.addRow(QLabel("重频变化范围(%)"), self.pri_jetter)
            if input_pri_type == pri_type.pri_group:
                self.pri_groupNumber = QLineEdit()
                layout.addRow(QLabel("重频脉组个数:"), self.pri_groupNumber)
        if input_fs_type == fs_type.fs_big_band_lfm or input_fs_type==fs_type.fs_jitter_lfm:
            self.fs_lfm_f0 = QLineEdit()
            layout.addRow(QLabel("LFM起始频率(MHz)："), self.fs_lfm_f0)
            self.fs_lfm_band = QLineEdit()
            layout.addRow(QLabel("LFM带宽(MHz):"), self.fs_lfm_band)
            if input_fs_type == fs_type.fs_jitter_lfm:
                self.fs_lfm_jetter = QLineEdit()
                layout.addRow(QLabel("LFM捷变范围(%):"), self.fs_lfm_jetter)
            else:
                self.fs_frame_number = QLineEdit()
                layout.addRow(QLabel("大带宽LFM跨帧数:"), self.fs_frame_number)
        else:
            if input_fs_type != fs_type.fs_group:
                self.fs_f0 = QLineEdit()
                layout.addRow(QLabel("信号频率(MHz):"), self.fs_f0)
                if input_fs_type == fs_type.fs_jitter_group or input_fs_type == fs_type.fs_jitter_between_pulse:
                    self.fs_jitter = QLineEdit()
                    layout.addRow(QLabel("频率捷变范围(%):"), self.fs_jitter)
                    if input_fs_type == fs_type.fs_jitter_group:
                        self.fs_group_number = QLineEdit()
                        layout.addRow(QLabel("脉组内个数："),self.fs_group_number)
            else:
                self.group_fs_text = QLineEdit()
                self.group_fs_text.setText("例: 210, 220, 230")
                layout.addRow(QLabel("频率分集的频点:"), self.group_fs_text)
        self.formGroupBox.setLayout(layout)

    # 重载退出函数
    def exec_(self):
        super(ConfigRadarDetials, self).exec_()
        # todo 进行信号格式转换，得到所需要的格式
        return "caocongcong"
