"""
@author:caocongcong
"""
from PyQt5.QtWidgets import QDialog, QLabel, QGroupBox, QFormLayout, QLineEdit, QDialogButtonBox, QVBoxLayout
from constant.PriTypeEnum import pri_type
from constant.FsTypeEnum import fs_type
from primary_signal.signal_source import signal_source


class ConfigRadarDetials(QDialog):
    def __init__(self, pri_type, fs_type):
        super(ConfigRadarDetials, self).__init__()
        self.setWindowTitle("雷达参数输入")

        self.createForm(pri_type, fs_type)
        self.pri_type = pri_type
        self.fs_type = fs_type

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.save_event)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.generate_signal = None

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
        if input_fs_type == fs_type.fs_big_band_lfm or input_fs_type == fs_type.fs_jitter_lfm:
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
                        layout.addRow(QLabel("脉组内个数："), self.fs_group_number)
            else:
                self.group_fs_text = QLineEdit()
                self.group_fs_text.setText("例: 210, 220, 230")
                layout.addRow(QLabel("频率分集的频点:"), self.group_fs_text)
        self.formGroupBox.setLayout(layout)

    # 重载退出函数
    def exec_(self):
        super(ConfigRadarDetials, self).exec_()
        return self.generate_signal

    # 正常返回函数
    def save_event(self):
        try:
            pw_parm = float(self.plue_width.text())
            DOA_parm = float(self.DOA.text())
            fs_type_parm = 0
            pri_type_parm = 0
            fs_parm = []
            pri_parm = []

            # 首先进行频率参数处理
            if self.fs_type == fs_type.fs_fixed:
                # 固定频率
                fs_type_parm = 1
                fs_parm.append(float(self.fs_f0.text()))
            elif self.fs_type == fs_type.fs_jitter_between_pulse:
                # 脉间捷变
                fs_type_parm = 2
                fs_parm.append(float(self.fs_f0.text()))
                fs_parm.append(float(self.fs_jitter.text()))
            elif self.fs_type == fs_type.fs_group:
                # 分集
                fs_type_parm = 3
                primary_text = ''.join(self.group_fs_text.text().split())
                fs_grop_list = primary_text.split(",")
                group_fs = []
                for value in fs_grop_list:
                    group_fs.append(float(value))
                fs_parm.append(group_fs)
            elif self.fs_type == fs_type.fs_jitter_group:
                # 脉组捷变
                fs_type_parm = 4
                fs_parm.append(float(self.fs_f0.text()))
                fs_parm.append(float(self.fs_group_number.text()))
                fs_parm.append(float(self.fs_jitter.text()))
            elif self.fs_type == fs_type.fs_jitter_lfm:
                fs_type_parm = 5
                fs_parm.append(float(self.fs_lfm_f0.text()))
                fs_parm.append(float(self.fs_lfm_band.text()))
            else:
                fs_type_parm = 6
                fs_parm.append(float(self.fs_lfm_f0.text()))
                fs_parm.append(float(self.fs_lfm_band.text()))
                fs_parm.append(float(self.fs_lfm_jetter.text()))
            if self.pri_type == pri_type.pri_fixed:
                # 固定重频
                pri_type_parm = 1
                pri_parm.append(float(self.pri_value.text()))
            elif self.pri_type == pri_type.pri_deviation or self.pri_type == pri_type.pri_jitter:
                pri_type_parm = 2
                pri_parm.append(float(self.pri_value.text()))
                pri_parm.append(float(self.pri_jetter.text()))
            else:
                pri_type_parm = 3
                pri_parm.append(float(self.pri_value.text()))
                pri_parm.append(int(self.pri_groupNumber.text()))
                pri_parm.append(float(self.pri_jetter.text()))
            self.generate_signal = signal_source(pw_parm, DOA_parm, fs_type_parm, fs_parm, pri_type_parm, pri_parm)
            self.accept()
        except:
            print("产生信号出错")
            self.reject()
