# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gemiturekle.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mesajlar as mes


class Ui_CinsEkle(object):
    def setupUi(self, CinsEkle):
        CinsEkle.setObjectName("CinsEkle")
        CinsEkle.resize(382, 54)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CinsEkle.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(CinsEkle)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(CinsEkle)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(CinsEkle)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(CinsEkle)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.retranslateUi(CinsEkle)
        self.pushButton.clicked.connect(self.cins_yaz)
        QtCore.QMetaObject.connectSlotsByName(CinsEkle)

    def retranslateUi(self, CinsEkle):
        _translate = QtCore.QCoreApplication.translate
        CinsEkle.setWindowTitle(_translate("CinsEkle", "Gemi Türü Ekle"))
        self.label.setText(_translate("CinsEkle", "Yeni Gemi Türü Ekle"))
        self.pushButton.setText(_translate("CinsEkle", "Ekle"))

    def cins_yaz(self):
        self.yaz = VbagKur()
        ad = self.lineEdit.text()
        if ad =="":
            mesaj = "Lütfen bir gemi türü giriniz !!"
            mes.uyari(mesaj, "Bilgi Giriş Hatası")
        else:
            self.yaz.isle("INSERT INTO gemitur VALUES(NULL, '{}')".format(ad))
            mesaj = ad + " türü veritabanına eklendi"
            mes.uyari(mesaj, "Kayıt Eklendi")
            self.lineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CinsEkle = QtWidgets.QDialog()
    ui = Ui_CinsEkle()
    ui.setupUi(CinsEkle)
    CinsEkle.show()
    sys.exit(app.exec_())
