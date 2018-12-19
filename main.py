import sys
import time
import os
import threading

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np


#my files
import image_resource_rc
import design
import variables
import plotter
variables.init()

class MainApp(QtGui.QMainWindow, design.Ui_MainWindow):

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically

        self.pushButton.clicked.connect(self.motor_working)  # When the button is pressed
                                                            # Execute motor_working function

        self.pushButton_fwd.clicked.connect(self.motor_working_fwd)
        self.pushButton_bwd.clicked.connect(self.motor_working_bwd)

        self.radioButton.clicked.connect(self.circuit_breaker)

        self.fan_pic = QtGui.QLabel(parent=self)
        self.fan_pic.setGeometry(QtCore.QRect(150, 450, 100, 110))

        self.motor_pic = QtGui.QLabel(parent=self)


        self.motor_pic.setGeometry(QtCore.QRect(40, 450, 100, 110))

        self.threadIt()

    def motor_working(self):
        if(variables.circuit_breaker==1):
            variables.working=0
            variables.motor_forward=1
            variables.motor_backward=0


    def circuit_breaker(self):
        if(variables.circuit_breaker==1):
            variables.circuit_breaker=0
            variables.working=0
            variables.motor_forward=0
            variables.motor_backward=0
        elif(variables.circuit_breaker==0):
            variables.circuit_breaker=1

    def motor_working_fwd(self):
        if(variables.circuit_breaker==1):
            variables.working=1
            variables.motor_forward=1
            variables.motor_backward=0


    def motor_working_bwd(self):
        if(variables.circuit_breaker==1):
            variables.working=1
            variables.motor_backward=1
            variables.motor_forward=0


    def threadIt(self):
        threading.Timer(0.5, self.threadIt).start()


        if(variables.fan==1):
            self.fan_pic.setPixmap(QtGui.QPixmap("fan_on.png"))
        elif(variables.fan==0):
            self.fan_pic.setPixmap(QtGui.QPixmap("fan_off.png"))

        if(variables.working==0):
            self.motor_pic.setPixmap(QtGui.QPixmap("motor_off.png"))
        elif(variables.motor_forward==1):
            self.motor_pic.setPixmap(QtGui.QPixmap("motor_forward.png"))
        elif(variables.motor_backward==1):
            self.motor_pic.setPixmap(QtGui.QPixmap("motor_backwards.png"))



        self.fan_pic.show()


        #future work - showing current and average temp, and total operation time
        #of fan and motor
        #self.text = QtGui.QTextEdit(parent=self)
        #self.text.setReadOnly(True)
        #string_number=str(variables.current_temperature)
        #print(string_number)

        #self.text.textCursor().insertBlock('Motor Temperature: ' + string_number)
        #self.text.textCursor().movePosition(1)
        #self.text.textCursor().noWrap()
        #self.update()
        #self.text.setGeometry(600, 400, 110, 50)
        #QtGui.QGuiApplication.processEvents()








def main():
    app = QtGui.QApplication( ["Motor Control Interface"])
    form = MainApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
