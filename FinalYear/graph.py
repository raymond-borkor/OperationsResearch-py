import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Maximization','Minimization','New Method')
y_pos = np.arange(len(objects))
#performance = [2.99999999998e-06, 5.00000000003e-06]
#f = open('times.txt', 'r')
with open("times.txt", "r") as times1:
    f_list = [float(i) for line in times1 for i in line.split(',') if i.strip()]
    total = [f_list[0] + f_list[1]]
with open("asstime2.txt","r") as times11:
	flist = [float(i) for line in times11 for i in line.split(',') if i.strip()]
	assP1 = flist[0]
performance = [f_list[0], f_list[1], flist[0]]
majtotal = f_list[0] + f_list[1] + flist[0]
timetext = open('times3.txt','a+')
timetext.write(str(majtotal))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Processing Time')
plt.title('Processing Time for Algorithms (Big Data Set)')
plt.show()