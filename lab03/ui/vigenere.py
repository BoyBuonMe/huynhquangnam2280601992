# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/vigenere.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VigenereCipher(object):
    def setupUi(self, CaesarCipher):
        CaesarCipher.setObjectName("CaesarCipher")
        CaesarCipher.resize(991, 730)
        self.widget = QtWidgets.QWidget(CaesarCipher)
        self.widget.setGeometry(QtCore.QRect(9, 9, 973, 712))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(100, 370, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtKey = QtWidgets.QTextEdit(self.widget)
        self.txtKey.setGeometry(QtCore.QRect(240, 360, 561, 31))
        self.txtKey.setObjectName("txtKey")
        self.btnEncrypt = QtWidgets.QPushButton(self.widget)
        self.btnEncrypt.setGeometry(QtCore.QRect(290, 610, 141, 31))
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.txtPlainText = QtWidgets.QTextEdit(self.widget)
        self.txtPlainText.setGeometry(QtCore.QRect(240, 190, 561, 121))
        self.txtPlainText.setObjectName("txtPlainText")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 240, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnDecrypt = QtWidgets.QPushButton(self.widget)
        self.btnDecrypt.setGeometry(QtCore.QRect(560, 610, 141, 31))
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(390, 70, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(100, 500, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtCipherText = QtWidgets.QTextEdit(self.widget)
        self.txtCipherText.setGeometry(QtCore.QRect(240, 440, 561, 131))
        self.txtCipherText.setObjectName("txtCipherText")

        self.retranslateUi(CaesarCipher)
        QtCore.QMetaObject.connectSlotsByName(CaesarCipher)

    def retranslateUi(self, CaesarCipher):
        _translate = QtCore.QCoreApplication.translate
        CaesarCipher.setWindowTitle(_translate("CaesarCipher", "Dialog"))
        self.label_2.setText(_translate("CaesarCipher", "Key:"))
        self.btnEncrypt.setText(_translate("CaesarCipher", "Encrypt"))
        self.label.setText(_translate("CaesarCipher", "PlainText:"))
        self.btnDecrypt.setText(_translate("CaesarCipher", "Decrypt"))
        self.label_4.setText(_translate("CaesarCipher", "Vigenere cipher"))
        self.label_3.setText(_translate("CaesarCipher", "CipherText:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaesarCipher = QtWidgets.QDialog()
    ui = Ui_VigenereCipher()
    ui.setupUi(CaesarCipher)
    CaesarCipher.show()
    sys.exit(app.exec_())
