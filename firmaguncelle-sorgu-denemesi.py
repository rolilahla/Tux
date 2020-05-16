# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\firmaguncelle-sorgu-denemesi.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur



class Ui_Firmaguncelle(object):
    def setupUi(self, Firmaguncelle):
        self.yaz = VbagKur()
        Firmaguncelle.setObjectName("Firmaguncelle")
        Firmaguncelle.resize(683, 457)
        self.gridLayout_2 = QtWidgets.QGridLayout(Firmaguncelle)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(Firmaguncelle)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(Firmaguncelle)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 2)
        self.listWidget = QtWidgets.QListWidget(Firmaguncelle)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(Firmaguncelle)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 5, 1, 2, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 212, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(264, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 2, 1, 1)

        self.retranslateUi(Firmaguncelle)
        self.lineEdit_6.textChanged['QString'].connect(self.bul)
        self.listWidget.doubleClicked['QModelIndex'].connect(self.frame.update)
        QtCore.QMetaObject.connectSlotsByName(Firmaguncelle)

    def retranslateUi(self, Firmaguncelle):
        _translate = QtCore.QCoreApplication.translate
        Firmaguncelle.setWindowTitle(_translate("Firmaguncelle", "Müşteri Bilgisi Güncelle"))
        self.label_7.setText(_translate("Firmaguncelle", "Firma Ara"))
        self.label.setText(_translate("Firmaguncelle", "Müşteri Kodu"))
        self.label_2.setText(_translate("Firmaguncelle", "Müşteri Adı"))
        self.label_3.setText(_translate("Firmaguncelle", "Vergi Dairesi"))
        self.label_4.setText(_translate("Firmaguncelle", "Vergi No"))
        self.label_6.setText(_translate("Firmaguncelle", "Telefon"))
        self.label_5.setText(_translate("Firmaguncelle", "Adres"))
        self.pushButton.setText(_translate("Firmaguncelle", "GÜNCELLE"))

    def bul(self):
        self.listWidget.clear()
        sonuc = self.yaz.coklu_komut("SELECT ad FROM firmalar WHERE ad LIKE '{}'".format(self.lineEdit_6.text()+"%"))        
        for i in range(len(sonuc)):
            #burada hata ayıklayacaksın
            #eğer dönen sonuç yoksa TypeError hatası verecek len'den kaynaklı
            self.listWidget.addItem(sonuc[i][0])

    def doldur(self):
        pass

    def guncelle(self):
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Firmaguncelle = QtWidgets.QDialog()
    ui = Ui_Firmaguncelle()
    ui.setupUi(Firmaguncelle)
    Firmaguncelle.show()
    sys.exit(app.exec_())
