import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import numpy as np
import pandas as pd

datafile = "loggedlux.txt"

app = pg.mkQApp("VEML7700 Signal Plotter")
win = pg.GraphicsLayoutWidget(show=True, title="VEML7700 Signal Plotter")
win.resize(1000, 600)
win.setWindowTitle("VEML7700 Signal Plotter")

pg.setConfigOptions(antialias=True)

plotter = win.addPlot()
plotter.showGrid(x=True, y=True)
plotter.setLabel('bottom', 'Time', units='s')
plotter.setLabel('left', 'Intensity', units='arb.')

curve = plotter.plot(pen='g')

def update():
    global plotter
    global y


    data = pd.read_csv(datafile, header=None, skiprows=1)

    curve.setData(data[0], data[1])

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1000)

if __name__ == '__main__':
    pg.exec()
