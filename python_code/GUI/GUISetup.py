"""
@author:caocongcong
"""
from PyQt5.QtCore import Qt

from GUI.mainGUI import Ui_MainWindow
from GUI.CreateRadarwithEventGUI import CreateRadarwithEventGUI
from GUI.ConfigRadarDetials import ConfigRadarDetials
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem, QMenu, QFileDialog, QAction, QMessageBox
from primary_signal.get_primary_signal import priamry_signal
from primary_signal.ADC import AD
from primary_signal.const_value import constValue

class GUISetup(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        # 整体界面进行初始化
        self.main_ui.setupUi(self)
        self.bar_init()


        # 初始化表格
        self.table_init()
        # 为空间增加事件
        self.add_event()
        self.primary_radar= []
        self.signals = []


    # 进行状态栏和菜单栏的初始化
    def bar_init(self):
        self.statusBar().showMessage('当前状态:参数配置')

        exitAction = QAction('&仿真开始', self)
        exitAction.setStatusTip('仿真开始')
        exitAction.triggered.connect(self.begin_simu)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&仿真控制')
        fileMenu.addAction(exitAction)


    # 进行表格的初始化
    def table_init(self):
        self.table = self.main_ui.tableWidget
        self.table.setColumnCount(4)  ##设置表格一共有五列
        self.table.setHorizontalHeaderLabels(['编号', '名字', '重频类型', '频率类型'])  # 设置表头文字
        # 禁止修改
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置为整行选择
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 为行增加右击函数
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.custom_right_menu)

    # 为主界面上的控件增加响应
    def add_event(self):
        self.main_ui.create_radar.clicked.connect(self.addSignalEvent)
        self.main_ui.pushButton_2.clicked.connect(self.delete_all_radar)
        self.main_ui.signal_button.clicked.connect(self.get_signal_file_path)
        self.main_ui.pdw_button.clicked.connect(self.get_pdw_file_path)
        self.main_ui.pushButton_4.clicked.connect(self.save_setting)
        self.main_ui.pushButton_3.clicked.connect(self.config_setting)

    # 对增加信号按钮的响应
    def addSignalEvent(self):
        create_radar_dialog = CreateRadarwithEventGUI()
        create_radar_dialog.show()
        value = create_radar_dialog.exec_()
        if value:
            self.primary_radar.append(value)
            row = self.table.rowCount()
            self.table.setRowCount(row + 1)
            radar_id = value.radar_id
            radar_name = value.radar_name
            fs_type = value.fs_type.value
            pri_type = value.pri_type.value
            self.table.setItem(row, 0, QTableWidgetItem(radar_id))
            self.table.setItem(row, 1, QTableWidgetItem(radar_name))
            self.table.setItem(row, 2, QTableWidgetItem(pri_type))
            self.table.setItem(row, 3, QTableWidgetItem(fs_type))

    # 对删除所有雷达信号的响应
    def delete_all_radar(self):
        self.primary_radar = []
        self.signals = []
        self.table.setRowCount(0)
        self.table.clearContents()

    # 增加右键菜单
    def custom_right_menu(self, pos):
        # 创建表格
        menu = QMenu()
        opt1 = menu.addAction("配置雷达参数")
        opt2 = menu.addAction("删除雷达")
        action = menu.exec_(self.table.mapToGlobal(pos))
        if action == opt1:
            # do something
            row_index = self.table.currentRow()
            current_radar = self.primary_radar[row_index]
            configDetailsDialog = ConfigRadarDetials(current_radar.pri_type, current_radar.fs_type)
            configDetailsDialog.show()
            value = configDetailsDialog.exec_()
            if value:
                self.signals.append(value)
                print(str(value))


        elif action == opt2:
            # 获取雷达参数并进行删除
            row_index = self.table.currentRow()
            if row_index != -1:
                self.primary_radar.pop(row_index)
                self.signals.pop(row_index)
                self.table.removeRow(row_index)

    def get_signal_file_path(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if dir_name:
            self.main_ui.lineEdit_4.setText(dir_name)
            print(dir_name)

    def get_pdw_file_path(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if dir_name:
            self.main_ui.lineEdit_3.setText(dir_name)
            print(dir_name)


    def begin_simu(self):
        # try:
        self.statusBar().showMessage("仿真进行中")
            # 进行模拟信号的产生
        print("开始产生模拟信号")
        priamry_signal_test = priamry_signal(self.signals, self.simu_time)
            # 写入原始数据
            # priamry_signal_test.write_data("..\data\primary_data.txt")
        # priamry_signal_test.show_data(1000, 2000)
        print("模拟信号产生完毕，开始采样")
        tmp_AD = AD(priamry_signal_test.primary_data, self.simu_time, constValue.frame_length)
        tmp_AD.AD_data()
        print("采样成功")
        # except Exception as e :
        #     print(e)
        #     QMessageBox.about(self, "错误提示", "仿真发生错误，可能是参数设置或者其他错误")



    def save_setting(self):
        self.SNR = int(self.main_ui.SNR_Data.text())
        self.simu_time = int(self.main_ui.lineEdit_2.text())
        self.ad_fs_band = []
        if self.main_ui.low_ad_fs.isChecked():
            self.ad_fs_band.append(200)
        if self.main_ui.mid_ad_fs.isChecked():
            self.ad_fs_band.append(600)
        if self.main_ui.high_ad_fs.isChecked():
            self.ad_fs_band.append(1000)
        self.pdw_write_path = self.main_ui.lineEdit_3.text()
        self.priamry_write_path = self.main_ui.lineEdit_4.text()

        self.main_ui.SNR_Data.setDisabled(True)
        self.main_ui.lineEdit_2.setDisabled(True)
        self.main_ui.low_ad_fs.setDisabled(True)
        self.main_ui.mid_ad_fs.setDisabled(True)
        self.main_ui.high_ad_fs.setDisabled(True)
        self.main_ui.lineEdit_3.setDisabled(True)
        self.main_ui.lineEdit_4.setDisabled(True)

    def config_setting(self):
        self.main_ui.SNR_Data.setEnabled(True)
        self.main_ui.lineEdit_2.setEnabled(True)
        self.main_ui.low_ad_fs.setEnabled(True)
        self.main_ui.mid_ad_fs.setEnabled(True)
        self.main_ui.high_ad_fs.setEnabled(True)
        self.main_ui.lineEdit_3.setEnabled(True)
        self.main_ui.lineEdit_4.setEnabled(True)