"""
@author:caocongcong
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class SaveDialog(QDialog):  # 继承QDialog类
    def __init__(self, parent=None):
        super(SaveDialog, self).__init__(parent)
        label = QLabel("Title")
        lineEdit = QTextBrowser()
        label.setBuddy(lineEdit)
        cacelButton = QPushButton("Cacel")
        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.close)  # 当点击save按钮时，对话框将会消失，点击Cacel按钮时，则不会消失。
        buttonBox = QDialogButtonBox(QtCore.Qt.Horizontal)
        buttonBox.addButton(saveButton, QDialogButtonBox.RejectRole)
        buttonBox.addButton(cacelButton, QDialogButtonBox.YesRole)

        topLeftLayout = QVBoxLayout()
        topLeftLayout.addWidget(label)
        topLeftLayout.addWidget(lineEdit)
        leftLayout = QHBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addStretch(1)
        mainLayout = QGridLayout()
        mainLayout.addLayout(leftLayout, 0, 0)
        mainLayout.addWidget(buttonBox, 1, 0)
        self.setLayout(mainLayout)
        self.setWindowTitle("Save or Not")


