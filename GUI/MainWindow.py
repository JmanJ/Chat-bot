# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui

from CustomTextEdit import CustomTextEdit
from Bot_Module.ChatAnalyzer import ChatAnalyzer

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.font = QtGui.QFont()
        self.font.setFamily(_fromUtf8("Times New Roman"))
        self.font.setPointSize(12)
        self.char_format = QtGui.QTextCharFormat()
        self.char_format.setFont(self.font)
        self.text_editor = CustomTextEdit(self)
        self.text_editor.setFont(self.font)
        self.setCentralWidget(self.text_editor)
        self.chat_analysis = ChatAnalyzer()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle(_fromUtf8("Chat-bot"))
        self.setEnabled(True)
        self.resize(275, 397)
        self.setMinimumSize(QtCore.QSize(250, 320))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setStyleSheet("background-color: rgb(45, 45, 45);color:#e6e6e6;")

    def sender(self):
        message = self.text_editor.toPlainText()
        mess = unicode(message)
        #mess = unicode(message.toUtf8(), encoding="UTF-8")
        print "Входящее сообщение: "
        print mess
        self.chat_analysis.message_processing(mess)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
