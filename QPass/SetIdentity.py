# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\SpecterShell\Documents\Workspace\QPass\SetIdentity.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetIdentity(object):
    def setupUi(self, SetIdentity):
        SetIdentity.setObjectName("SetIdentity")
        SetIdentity.resize(486, 245)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Repositories\\PasswordManager\\QPass\\QPass\\icon/person-black-48dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SetIdentity.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(SetIdentity)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelAccount = QtWidgets.QLabel(SetIdentity)
        self.labelAccount.setObjectName("labelAccount")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelAccount)
        self.lineEditAccount = QtWidgets.QLineEdit(SetIdentity)
        self.lineEditAccount.setObjectName("lineEditAccount")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditAccount)
        self.labelComment = QtWidgets.QLabel(SetIdentity)
        self.labelComment.setObjectName("labelComment")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelComment)
        self.plainTextComment = QtWidgets.QPlainTextEdit(SetIdentity)
        self.plainTextComment.setObjectName("plainTextComment")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextComment)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SetIdentity)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(SetIdentity)
        self.buttonBox.accepted.connect(SetIdentity.accept)
        self.buttonBox.rejected.connect(SetIdentity.reject)
        QtCore.QMetaObject.connectSlotsByName(SetIdentity)

    def retranslateUi(self, SetIdentity):
        _translate = QtCore.QCoreApplication.translate
        SetIdentity.setWindowTitle(_translate("SetIdentity", "??????"))
        self.labelAccount.setText(_translate("SetIdentity", "??????"))
        self.lineEditAccount.setText(_translate("SetIdentity", "prisident@swu.edu.cn"))
        self.labelComment.setText(_translate("SetIdentity", "??????"))
