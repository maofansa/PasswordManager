# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\SpecterShell\Documents\Workspace\QPass\SetRecord.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetRecord(object):
    def setupUi(self, SetRecord):
        SetRecord.setObjectName("SetRecord")
        SetRecord.resize(486, 246)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\SpecterShell\\Documents\\Workspace\\QPass\\icon/receipt_long-black-48dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SetRecord.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(SetRecord)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelIdentity = QtWidgets.QLabel(SetRecord)
        self.labelIdentity.setObjectName("labelIdentity")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelIdentity)
        self.labelComment = QtWidgets.QLabel(SetRecord)
        self.labelComment.setObjectName("labelComment")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelComment)
        self.plainTextComment = QtWidgets.QPlainTextEdit(SetRecord)
        self.plainTextComment.setObjectName("plainTextComment")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.plainTextComment)
        self.labelSite = QtWidgets.QLabel(SetRecord)
        self.labelSite.setObjectName("labelSite")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelSite)
        self.labelPassword = QtWidgets.QLabel(SetRecord)
        self.labelPassword.setObjectName("labelPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(SetRecord)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.comboBoxIdentity = QtWidgets.QComboBox(SetRecord)
        self.comboBoxIdentity.setObjectName("comboBoxIdentity")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxIdentity)
        self.comboBoxSite = QtWidgets.QComboBox(SetRecord)
        self.comboBoxSite.setObjectName("comboBoxSite")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxSite)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SetRecord)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(SetRecord)
        self.buttonBox.accepted.connect(SetRecord.accept)
        self.buttonBox.rejected.connect(SetRecord.reject)
        QtCore.QMetaObject.connectSlotsByName(SetRecord)

    def retranslateUi(self, SetRecord):
        _translate = QtCore.QCoreApplication.translate
        SetRecord.setWindowTitle(_translate("SetRecord", "记录"))
        self.labelIdentity.setText(_translate("SetRecord", "身份"))
        self.labelComment.setText(_translate("SetRecord", "备注"))
        self.labelSite.setText(_translate("SetRecord", "站点"))
        self.labelPassword.setText(_translate("SetRecord", "密码"))