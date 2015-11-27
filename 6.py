+import matplotlib.pyplot as plt
+import numpy as np
+inp = open('input.txt','r') 
+  
+A = inp.read().split()
+Az = [len(x) for x in A]
+C = [0] * max(Az)
+for i in Az:
+    C[i-1] += 1 
+
+y_pos = [1+i for i in range(max(Az)]
+
+plt.bar(y_pos, C, align='center', alpha=0.7)
+plt.xticks(y_pos, y_pos)
+plt.ylabel('Value')
+plt.title('Bar title')
+
+plt.show()
