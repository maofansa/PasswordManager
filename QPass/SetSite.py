# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\SpecterShell\Documents\Workspace\QPass\SetSite.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetSite(object):
    def setupUi(self, SetSite):
        SetSite.setObjectName("SetSite")
        SetSite.resize(486, 245)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\SpecterShell\\Documents\\Workspace\\QPass\\icon/language-black-48dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SetSite.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(SetSite)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelAddress = QtWidgets.QLabel(SetSite)
        self.labelAddress.setObjectName("labelAddress")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelAddress)
        self.lineEditAddress = QtWidgets.QLineEdit(SetSite)
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditAddress)
        self.labelComment = QtWidgets.QLabel(SetSite)
        self.labelComment.setObjectName("labelComment")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelComment)
        self.plainTextComment = QtWidgets.QPlainTextEdit(SetSite)
        self.plainTextComment.setObjectName("plainTextComment")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextComment)
        self.labelTitle = QtWidgets.QLabel(SetSite)
        self.labelTitle.setObjectName("labelTitle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelTitle)
        self.lineEditTitle = QtWidgets.QLineEdit(SetSite)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditTitle)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SetSite)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(SetSite)
        self.buttonBox.accepted.connect(SetSite.accept)
        self.buttonBox.rejected.connect(SetSite.reject)
        QtCore.QMetaObject.connectSlotsByName(SetSite)

    def retranslateUi(self, SetSite):
        _translate = QtCore.QCoreApplication.translate
        SetSite.setWindowTitle(_translate("SetSite", "站点"))
        self.labelAddress.setText(_translate("SetSite", "地址"))
        self.lineEditAddress.setText(_translate("SetSite", "http://swu.edu.cn"))
        self.labelComment.setText(_translate("SetSite", "备注"))
        self.labelTitle.setText(_translate("SetSite", "名称"))
