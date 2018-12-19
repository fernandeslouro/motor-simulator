import time
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import os
import variables
import image_resource_rc
from PyQt5.QtWidgets import QLabel
from threading import Thread
from PyQt5.QtGui import QApplication, QMainWindow


variables.init()

class  CustomWidget(pg.GraphicsWindow):

    def __init__(self, parent=None, **kargs):
        pg.GraphicsWindow.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle('Motor Temperature')
        self.p1 = self.addPlot(labels =  {'left':'Temperature (ºC)'})
        self.dataBlue=np.asarray([[1,15]])
        self.curve1 = self.p1.plot()

        timer = pg.QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000) # number of seconds (every 1000) for next update

        self.vLineup = pg.InfiniteLine(pos=variables.max_temperature, angle=0, movable=True,pen=[100,100,200,200])
        self.vLinelow = pg.InfiniteLine(pos=variables.min_temperature, angle=0, movable=False,pen=[100,100,200,200])

        self.p1.addItem(self.vLineup, ignoreBounds=True)
        self.p1.addItem(self.vLinelow, ignoreBounds=True)



    def getData(self):

        self.dataBlue=self.dataBlue.tolist()

        if (variables.working==1):
            if ((self.dataBlue[-1][1]<variables.max_temperature and self.dataBlue[-1][1]>variables.min_temperature) and variables.fan==0):
                self.vec=[self.dataBlue[-1][0]+1, self.dataBlue[-1][1]+1]
            elif ((self.dataBlue[-1][1]<variables.max_temperature and self.dataBlue[-1][1]>variables.min_temperature) and variables.fan==1):
                self.vec=[self.dataBlue[-1][0]+1, self.dataBlue[-1][1]-1]
            elif ((self.dataBlue[-1][1]>=variables.max_temperature) ):
                variables.fan=1
                self.vec=[self.dataBlue[-1][0]+1, self.dataBlue[-1][1]-1]
            elif ((self.dataBlue[-1][1]<=variables.min_temperature)):
                variables.fan=0
                self.vec=[self.dataBlue[-1][0]+1, self.dataBlue[-1][1]+1]
        elif (variables.working==0):
            if (self.dataBlue[-1][1]==15):
                self.vec=[self.dataBlue[-1][0]+1, self.dataBlue[-1][1]+0]
                variables.fan=0
            else:
                self.vec=[self.dataBlue[-1][0]+1, self.dataBlue[-1][1]-1]
                variables.fan=0

        

        variables.current_temperature=self.vec[1]
        self.dataBlue.append(self.vec)

        self.dataBlue=np.asarray(self.dataBlue)

    def plot(self):
        self.p1.removeItem(self.vLineup)
        self.p1.removeItem(self.vLinelow)

        if (variables.max_temperature<variables.min_temperature):
            intermediate=variables.max_temperature
            variables.max_temperature=variables.min_temperature
            variables.min_temperature=intermediate

        self.vLineup = pg.InfiniteLine(pos=variables.max_temperature, angle=0, movable=True,pen=[100,100,200,200])
        self.vLinelow = pg.InfiniteLine(pos=variables.min_temperature, angle=0, movable=False,pen=[100,100,200,200])
        self.vineLiit = pg.InfiniteLine(pos=300, pen='r', angle=0, movable=False)

        self.p1.addItem(self.vLineup, ignoreBounds=True)
        self.p1.addItem(self.vLinelow, ignoreBounds=True)

        self.curve1.setData(self.dataBlue, pen='y', symbol='o', symbolPen=None, symbolSize=4, symbolBrush=('b'))




    def update(self):
        self.getData()
        self.plot()




if __name__ == '__main__':
    import sys

    w = CustomWidget()
    w.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()# -*- coding: utf-8 -*-
