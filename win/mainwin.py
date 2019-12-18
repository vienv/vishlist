# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VishListDialog(object):
    def setupUi(self, VishListDialog):
        VishListDialog.setObjectName("VishListDialog")
        VishListDialog.resize(404, 303)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(VishListDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(VishListDialog)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(VishListDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout_3.addWidget(self.nameEdit)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.splitter = QtWidgets.QSplitter(VishListDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.priceBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.priceBox.setObjectName("priceBox")
        self.verticalLayout.addWidget(self.priceBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.linkEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.linkEdit.setObjectName("linkEdit")
        self.verticalLayout_2.addWidget(self.linkEdit)
        self.verticalLayout_5.addWidget(self.splitter)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(VishListDialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.commentEdit = QtWidgets.QTextEdit(VishListDialog)
        self.commentEdit.setObjectName("commentEdit")
        self.verticalLayout_4.addWidget(self.commentEdit)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SaveButton = QtWidgets.QPushButton(VishListDialog)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        self.CancelButton = QtWidgets.QPushButton(VishListDialog)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(VishListDialog)
        QtCore.QMetaObject.connectSlotsByName(VishListDialog)

    def retranslateUi(self, VishListDialog):
        _translate = QtCore.QCoreApplication.translate
        VishListDialog.setWindowTitle(_translate("VishListDialog", "Вишлист"))
        self.label.setText(_translate("VishListDialog", "Название товара"))
        self.nameEdit.setPlaceholderText(_translate("VishListDialog", "Введите наименование"))
        self.label_3.setText(_translate("VishListDialog", "Цена, руб"))
        self.label_2.setText(_translate("VishListDialog", "Ссылка на страницу"))
        self.linkEdit.setPlaceholderText(_translate("VishListDialog", "https://example.com/market/id123"))
        self.label_4.setText(_translate("VishListDialog", "Примечание"))
        self.SaveButton.setText(_translate("VishListDialog", "Сохранить"))
        self.CancelButton.setText(_translate("VishListDialog", "Отмена"))
