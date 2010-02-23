# -*- coding: utf-8 -*-

#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
#
# Form implementation generated from reading ui file 'md5_calc_gui.ui'


from PyQt4 import QtCore, QtGui

class Ui_FormMD5(object):
    def setupUi(self, FormMD5):
        FormMD5.setObjectName("FormMD5")
        FormMD5.resize(600, 250)
        FormMD5.setWindowTitle("MD5 Calculator")
        self.gridLayout = QtGui.QGridLayout(FormMD5)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtGui.QPlainTextEdit(FormMD5)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.LineShowMD5 = QtGui.QLineEdit(FormMD5)
        self.LineShowMD5.setObjectName("LineShowMD5")
        self.gridLayout.addWidget(self.LineShowMD5, 2, 0, 1, 1)
        self.CalcMD5 = QtGui.QPushButton(FormMD5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalcMD5.sizePolicy().hasHeightForWidth())
        self.CalcMD5.setSizePolicy(sizePolicy)
        self.CalcMD5.setObjectName("CalcMD5")
        self.gridLayout.addWidget(self.CalcMD5, 0, 1, 3, 1)

        self.retranslateUi(FormMD5)
        QtCore.QMetaObject.connectSlotsByName(FormMD5)

    def retranslateUi(self, FormMD5):
        self.CalcMD5.setText(QtGui.QApplication.translate("FormMD5", "Calculate\n""MD5 HASH", None, QtGui.QApplication.UnicodeUTF8))
        
