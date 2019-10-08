#graph for comparing processiong time on both datasets

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('DataSet 1 (Big)','DataSet 2 (Small)')
y_pos = np.arange(len(objects))
#performance = [2.99999999998e-06, 5.00000000003e-06]
#f = open('times.txt', 'r')
with open("times3.txt", "r") as times1:
    f_list = [float(i) for line in times1 for i in line.split(',') if i.strip()]
    performance = [f_list[0], f_list[1]]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Processing Time')
plt.title('Data Set Comparison')
plt.show()