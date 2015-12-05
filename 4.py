import matplotlib.pyplot as plt;
import numpy as np
import matplotlib.pyplot as plt
s = list(map(str,str((open("input.txt","r")).read()).split()))
lengths = [len(s[i]) for i in range(len(s))]
lengths.sort()
performance = [lengths.count(lengths[k]) for k in range(len(s))]
y_pos = []
for n in range(len(s)):
    if lengths.count(lengths[n]) == 0:
        y_pos.append(lengths[n])
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, perfomance)
plt.ylabel('counts')
plt.title('lengths')

plt.show()
