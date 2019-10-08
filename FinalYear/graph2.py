import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Maximization', 'Minimization', 'New Method')
y_pos = np.arange(len(objects))
#performance = [2.99999999998e-06, 5.00000000003e-06]
#performance = [f_list[0], f_list[1], f_list[2]]
#f = open('times.txt', 'r')
with open("times2.txt", "r") as times2:
	f_list = [float(i) for line in times2 for i in line.split(',') if i.strip()]
	total = f_list[0] + f_list[1]
with open("asstime.txt", "r") as asstime:
    flist = [float(i) for line in asstime for i in line.split(',') if i.strip()]
    assP = flist[0]
performance = [f_list[0], f_list[1], flist[0]]
main_total = total + flist[0]
timetext = open('times3.txt','w')
timetext.write(str(main_total))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Processing Time')
plt.title('Processing Time for Algorithms Per Dataset 2')
plt.show()