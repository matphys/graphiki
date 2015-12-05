import math
import pylab
from matplotlib import mlab
import numpy as np
a = 1
xmin = -20.0
xmax = 20.0

dx = 0.01
listt = np.arange(xmin,xmax,dx)
ylist = [np.cos(2*t) for t in listt]
pylab.ion()

for n in range (50):
        a += 0.01
        xlist = [np.cos(t*a) for t in listt]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()
pylab.close()
