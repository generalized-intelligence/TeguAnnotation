# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zippanel.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_zippanel(object):
    def setupUi(self, zippanel):
        zippanel.setObjectName("zippanel")
        zippanel.resize(1016, 684)
        self.verticalLayout = QtWidgets.QVBoxLayout(zippanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBtn = QtWidgets.QGroupBox(zippanel)
        self.groupBtn.setObjectName("groupBtn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBtn)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnServal = QtWidgets.QPushButton(self.groupBtn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnServal.sizePolicy().hasHeightForWidth())
        self.btnServal.setSizePolicy(sizePolicy)
        self.btnServal.setObjectName("btnServal")
        self.horizontalLayout.addWidget(self.btnServal)
        self.btnZipTool = QtWidgets.QPushButton(self.groupBtn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnZipTool.sizePolicy().hasHeightForWidth())
        self.btnZipTool.setSizePolicy(sizePolicy)
        self.btnZipTool.setObjectName("btnZipTool")
        self.horizontalLayout.addWidget(self.btnZipTool)
        self.checkUsing7z = QtWidgets.QCheckBox(self.groupBtn)
        self.checkUsing7z.setObjectName("checkUsing7z")
        self.horizontalLayout.addWidget(self.checkUsing7z)
        self.btnCut = QtWidgets.QPushButton(self.groupBtn)
        self.btnCut.setObjectName("btnCut")
        self.horizontalLayout.addWidget(self.btnCut)
        self.btnSave = QtWidgets.QPushButton(self.groupBtn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnStart = QtWidgets.QPushButton(self.groupBtn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.verticalLayout.addWidget(self.groupBtn)
        self.txtOut = QtWidgets.QPlainTextEdit(zippanel)
        self.txtOut.setObjectName("txtOut")
        self.verticalLayout.addWidget(self.txtOut)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(zippanel)
        QtCore.QMetaObject.connectSlotsByName(zippanel)

    def retranslateUi(self, zippanel):
        _translate = QtCore.QCoreApplication.translate
        zippanel.setWindowTitle(_translate("zippanel", "zip"))
        self.groupBtn.setTitle(_translate("zippanel", "Pack Upload"))
        self.btnServal.setText(_translate("zippanel", "Select Serval File"))
        self.btnZipTool.setText(_translate("zippanel", "Select 7z.exe File"))
        self.checkUsing7z.setText(_translate("zippanel", "Use Internal Zipfile Tool"))
        self.btnCut.setText(_translate("zippanel", "Split Serval File"))
        self.btnSave.setText(_translate("zippanel", "Select Save Path"))
        self.btnStart.setText(_translate("zippanel", "Start Packing"))

