from PyQt5.QtGui import *
import variables


variables.init()

class  window(QLineEdit):

    def __init__(self, parent=None, **kargs):
        QLineEdit.__init__(self, **kargs)
        self.setParent(parent)


        self.setValidator(QIntValidator())
        self.setMaxLength(3)
        self.textChanged.connect(self.textchanged)


    def textchanged(self,text):
        if (len(text)==0 or len(text)==1):
            text=100
        variables.max_temperature=int(text)

class  window_lower(QLineEdit):

    def __init__(self, parent=None, **kargs):
        QLineEdit.__init__(self, **kargs)
        self.setParent(parent)


        self.setValidator(QIntValidator())
        self.setMaxLength(3)
        self.textChanged.connect(self.textchanged)


    def textchanged(self,text):
        if (len(text)==0 or len(text)==1):
            text=10
        variables.min_temperature=int(text)



if __name__ == '__main__':
    import sys
    w = window()
    w = window_lower()
    w.show()
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()# -*- coding: utf-8 -*-
