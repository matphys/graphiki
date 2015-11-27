+import math
+import pylab
+from matplotlib import mlab
+
+tmin = -20.0
+tmax = 20.0
+
+tx = 0.01
+tlist = mlab.frange (tmin, tmax, tx)
+
+pylab.ion()
+
+for a in range (50):
+        xlist = [math.sin (t + a ) for t in tlist]
+        ylist = [math.cos ( t * 2) for t in tlist] 
+        pylab.clf()
+        pylab.plot (xlist, ylist)
+        pylab.draw()
+
+pylab.close()
