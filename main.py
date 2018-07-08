from PyQt5.QtWidgets import (QPushButton, QLineEdit, QHBoxLayout, QTextEdit, QWidget, QVBoxLayout, QGridLayout,
                             QGroupBox, QLabel, QApplication, QTabWidget)
from PyQt5.QtGui import QTextOption, QIntValidator
from PyQt5.sip import *

import sys


class numEdit(QLineEdit):
    def __init__(self, value=0):
        super(numEdit, self).__init__(value)
        self.setValidator(QIntValidator(0, 999))

    def getValue(self):
        try:
            return int(self.text())
        except:
            return 0


class mainui(QTabWidget):
    def __init__(self, parent=None):
        super(mainui, self).__init__(parent)
        self.lcmDesEdit = QTextEdit("")
        self.lcmScrEdit = QTextEdit("0x56,0x25,0x23,0x23,0x32,0x55,0x32")
        self.lcmScrEdit.setWordWrapMode(QTextOption.NoWrap)
        self.lcmDesEdit.setWordWrapMode(QTextOption.NoWrap)
        self.width_edit = numEdit("480")
        self.vbp_edit = numEdit("8")
        self.vfp_edit = numEdit("8")
        self.vsl_edit = numEdit("8")
        self.high_edit = numEdit("960")
        self.hbp_edit = numEdit("10")
        self.hfp_edit = numEdit("10")
        self.hsl_edit = numEdit("10")
        self.lane_edit = numEdit("2")
        self.pll_edit = numEdit("200")
        self.fps_edit = numEdit("")
        self.fps_edit.setEnabled(False)
        self.lcm_tab = QWidget()
        self.cam_tab = QWidget()
        self.resize(800, 500)
        self.addTab(self.lcm_tab, "lcm")
        self.addTab(self.cam_tab, "camera")
        self.LcmUi()
        self.CamUi()

    def LcmUi(self):
        mainLayout = QVBoxLayout()
        lcmTimeLayout = QGridLayout()
        lcmCorelayout = QHBoxLayout()
        lcmTimeGridGroupBox = QGroupBox("lcm timing")
        lcmCoreGridGroupBox = QGroupBox("lcm Core")

        width_label = QLabel("WIDTH")
        vbp_label = QLabel("VBP")
        vfp_label = QLabel("VFP")
        vsl_label = QLabel("VSL")
        high_label = QLabel("HIGH")
        hbp_label = QLabel("HBP")
        hfp_label = QLabel("HFP")
        hsl_label = QLabel("HSL")
        lane_label = QLabel("Lane")
        pll_label = QLabel("PLL")

        fps_label = QLabel("FPS: ")

        self.width_edit.editingFinished.connect(self.calculation_fps)
        self.vbp_edit.editingFinished.connect(self.calculation_fps)
        self.vfp_edit.editingFinished.connect(self.calculation_fps)
        self.vsl_edit.editingFinished.connect(self.calculation_fps)
        self.high_edit.editingFinished.connect(self.calculation_fps)
        self.hbp_edit.editingFinished.connect(self.calculation_fps)
        self.hfp_edit.editingFinished.connect(self.calculation_fps)
        self.hsl_edit.editingFinished.connect(self.calculation_fps)
        self.lane_edit.editingFinished.connect(self.calculation_fps)
        self.pll_edit.editingFinished.connect(self.calculation_fps)

        lcmTimeLayout.setSpacing(10)
        lcmTimeLayout.addWidget(width_label, 1, 0)
        lcmTimeLayout.addWidget(self.width_edit, 1, 1)
        lcmTimeLayout.addWidget(vbp_label, 1, 2)
        lcmTimeLayout.addWidget(self.vbp_edit, 1, 3)
        lcmTimeLayout.addWidget(vfp_label, 1, 4)
        lcmTimeLayout.addWidget(self.vfp_edit, 1, 5)
        lcmTimeLayout.addWidget(vsl_label, 1, 6)
        lcmTimeLayout.addWidget(self.vsl_edit, 1, 7)

        lcmTimeLayout.addWidget(high_label, 2, 0)
        lcmTimeLayout.addWidget(self.high_edit, 2, 1)
        lcmTimeLayout.addWidget(hbp_label, 2, 2)
        lcmTimeLayout.addWidget(self.hbp_edit, 2, 3)
        lcmTimeLayout.addWidget(hfp_label, 2, 4)
        lcmTimeLayout.addWidget(self.hfp_edit, 2, 5)
        lcmTimeLayout.addWidget(hsl_label, 2, 6)
        lcmTimeLayout.addWidget(self.hsl_edit, 2, 7)

        lcmTimeLayout.addWidget(lane_label, 3, 0)
        lcmTimeLayout.addWidget(self.lane_edit, 3, 1)
        lcmTimeLayout.addWidget(pll_label, 3, 2)
        lcmTimeLayout.addWidget(self.pll_edit, 3, 3)
        lcmTimeLayout.addWidget(fps_label, 3, 4)
        lcmTimeLayout.addWidget(self.fps_edit, 3, 5)
        lcmTimeGridGroupBox.setLayout(lcmTimeLayout)

        lcmCorelayout.addWidget(self.lcmScrEdit)
        lcmCorelayout.addWidget(self.lcmDesEdit)
        lcmCoreGridGroupBox.setLayout(lcmCorelayout)

        btn = QPushButton(" switch ")
        btn.clicked.connect(self.lcmCoreSwitch)
        mainLayout.addWidget(lcmTimeGridGroupBox)
        mainLayout.addWidget(lcmCoreGridGroupBox)
        mainLayout.addWidget(btn)
        self.lcm_tab.setLayout(mainLayout)
        pass

    def CamUi(self):
        mainLayout = QVBoxLayout()
        CameraInfoGridGroupBox = QGroupBox("Camera info")
        cameraInfoLayout = QGridLayout()
        name_label = QLabel("camera name")
        name_edit = QLineEdit("")
        id_label = QLabel("ID ")
        id_edit = QLineEdit("")
        path_label = QLabel("path")
        path_edit = QLineEdit("")
        cameraInfoLayout.setSpacing(10)
        cameraInfoLayout.addWidget(name_label, 1, 0)
        cameraInfoLayout.addWidget(name_edit, 1, 1)
        cameraInfoLayout.addWidget(id_label, 2, 0)
        cameraInfoLayout.addWidget(id_edit, 2, 1)
        cameraInfoLayout.addWidget(path_label, 3, 0)
        cameraInfoLayout.addWidget(path_edit, 3, 1)
        CameraInfoGridGroupBox.setLayout(cameraInfoLayout)
        mainLayout.addWidget(CameraInfoGridGroupBox)
        btn = QPushButton("Auto add ")
        mainLayout.addWidget(btn)
        outputEdit = QTextEdit()
        outputEdit.setEnabled(False)
        mainLayout.addWidget(outputEdit)
        self.cam_tab.setLayout(mainLayout)
        pass

    def calculation_fps(self):
        if self.pll_edit.getValue() and self.lane_edit.getValue() and self.high_edit.getValue() and self.width_edit and self.hsl_edit.getValue() and self.hbp_edit.getValue() and self.hfp_edit.getValue() and self.vbp_edit.getValue() and self.vfp_edit.getValue() and self.vsl_edit.getValue():
            bit_ns = 1000 / self.pll_edit.getValue() / 2 / self.pll_edit.getValue()
            lane_us = (
                      self.hfp_edit.getValue() + self.hbp_edit.getValue() + self.hsl_edit.getValue() + self.width_edit.getValue()) * bit_ns * 24 / 1000
            fps = 10000 / (lane_us * (
            self.vfp_edit.getValue() + self.vbp_edit.getValue() + self.vsl_edit.getValue() + self.high_edit.getValue()))
            fps = round(fps, 2)
            self.fps_edit.setText(str(fps))
        pass

    def lcmCoreSwitch(self):
        self.lcmDesEdit.clear()
        src = self.lcmScrEdit.toPlainText().split("\n")
        for line in src:
            line = line.split(",")
            cmd = line[0]
            count = len(line)
            if cmd.find("0x") != -1:
                des="{%s,%d,{" %(cmd,count-1)
                for i in range(1,count):
                    if i != count-1:
                        des+="%s," %line[i]
                    else:
                        des+="%s" %line[i]
                des+="}},"
                self.lcmDesEdit.append(des)
            else:
                self.lcmDesEdit.append("")

    def checkLcmSrcCoreValid(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainui()
    win.show()
    sys.exit(app.exec_())
