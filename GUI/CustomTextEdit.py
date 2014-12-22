# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt


class CustomTextEdit(QtGui.QTextEdit):
    def __init__(self, parent):
        QtGui.QTextEdit.__init__(self)
        self.window = parent

    def keyPressEvent(self, event):
        modifiers = QtGui.QApplication
        flag = (modifiers == QtCore.Qt.ShiftModifier)
        if event.key() == Qt.Key_Return and not flag:
            self.window.sender()
        elif event.key() == Qt.Key_Enter and not flag:
            self.window.sender()
        else:
            QtGui.QTextEdit.keyPressEvent(self,  event)

    def insertFromMimeData(self, source):
        self.insertPlainText(unicode(source.text()))