import math
import numpy as np
import pylab
import matplotlib.pyplot as plt
x=np.arange(-10,10,0.01)
t=np.arange(-10,10,0.01)
a=np.arange(-10,10,0.01)
plt.subplot(221)
plt.plot(x,x**2 - x - 6)
plt.axis('equal')
plt.grid(True)
plt.title(r'$x*x - 6 -x$')

plt.subplot(222)
plt.plot(x,((np.log(x**2+1)-((x**2)**0.5)/10)/(np.log(1+np.tan(1/(1+(np.sin(x))**2))))))
plt.axis('equal')
plt.grid(True)
plt.title(r'$Long_fig$')
plt.show()

funk = str(input())
for h in range(2000):
    ylist[h] =  eval(str(funk.replace("x",str(x[h]))))
plt.subplot(223)
plt.plot(x,ylist)
plt.axis('equal')
plt.grid(True)
plt.title(r'$Your func$')
