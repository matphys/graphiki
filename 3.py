import math
import numpy as np
import pylab
import matplotlib.pyplot as plt
x=np.arange(-3,3,0.01)
funk = str(input())
ylist = []
for h in range(len(x)):
    ylist.append(eval(str(funk.replace("x",str(x[h])))))
plt.plot(x,ylist)
plt.axis('equal')
plt.grid(True)
plt.title(r'$Your func$')
plt.show()
