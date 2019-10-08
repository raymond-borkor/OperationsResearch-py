from __future__ import print_function
import munkres
from munkres import Munkres
from munkres import print_matrix 
from munkres import make_cost_matrix
from munkres import DISALLOWED
import time, string
import numpy as np
from collections import Counter
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
from string import ascii_lowercase
#import assignment_prob_hungarian
import os

print ("*** Welcome to the Ray Algorithm Module ***")
print ("\n Select Choice for Benchmarking. ")
m = Munkres()

def main():
    choice = raw_input("0) Test Smaller Dataset"
                   "\n1) Module 1 (Minimization)"
                   "\n2) Module 2 (Maximization)"
                   "\n3) Module 3 (Transportation)"
                   "\n4) Module 4 (Assignment Problem)"
                   "\n5) Time Comparison (Compare)"
                   "\n6) Exit (exit/close will do)"
                   "\n7) Benchmarking"
                   "\n : ")
    if choice == 'bench':
      bench()
    if choice == 'small':
      os.system('python sdsbench.py')
    if choice == 'minimize':
      mini()
    if choice == 'maximize':
      maxi()
    if choice == 'transport':
      os.system('python NW2.py')
    if choice == 'assign':
      os.system ('python assignment_prob_hungarian.py')
      main()
    if choice == 'close' or 'exit':
      exit()
    if choice == 'time' or 'compare':
      os.system('python graph.py')
    if choice == 'bench':
      bench()
        # assignment_prob_hungarian
def bench():
  choose = raw_input(
                    "\n1) Comparing Processing times For Dataset One (Big) on all algorithms"
                    "\n2) Comparing Processing times For Dataset Two (Small) on all algorithms"
                    "\n3) Compare Total Processing time for all DataSets"
                    "\n4) Back. "
                    "\n : ")
  if choose == 'data1':
    os.system('python graph.py')
    bench()
  if choose == 'data2':
    os.system('python graph2.py')
    bench()
  if choose == 'total':
    os.system('python graph3.py')
    bench()
  if choose == "back":
    main()

def mini():
    #matrix = [[20, 16, 22, 18],
     #         [25, 28, 15, 21],
      #        [27, 20, 23, 26],
       #       [24, 22, 23, 22]]
    #matrix = [[20, 60, 50, 55, 67, 78, 89, 87, 90, 89],
     #         [],
      #        [],
       #       [],
        #      [],
         #     [],
          #    [],
           #   [],
            #  [],
             # [],]
    f = open('TextFile1.txt')
    n = int(f.readline())
    matrix = []
    for i in range (n):
      list1 = map(int, (f.readline()).split())
      matrix.append(list1)
    #matrix = []
    m = Munkres()
    indexes = m.compute(matrix)
    print_matrix(matrix, msg='Lowest cost through this matrix:')
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
        print ('(%d, %d) -> %d' % (row, column, value))
    print ('total cost: %d' % total)
    start_time = time.clock()
    timex = time.clock() - start_time
    time2 = ("Time =", timex, "seconds")
    print(time2)
    #timex1 = string(timex)
    timetext = open('times.txt','w')
    timetext.write(str(timex))
    main()

def maxi():
     #matrix = [[20, 16, 22, 18],
      #        [25, 28, 15, 21],
       #       [27, 20, 23, 26],
        #      [24, 22, 23, 22]]
    f = open('TextFile1.txt')
    n = int(f.readline())
    matrix = []
    for i in range (n):
      list1 = map(int, (f.readline()).split())
      matrix.append(list1)
    cost_matrix = make_cost_matrix(matrix)
    m = Munkres()
    indexes = m.compute(cost_matrix)
    print_matrix(matrix, msg='Highest profits through this matrix:')
    total = 0
    for row, column in indexes:
      value = matrix[row][column]
      total += value
      print ('(%d, %d) -> %d' % (row, column, value))
    print ('total profit=%d' % total)
    start_time = time.clock()
    timex = time.clock() - start_time
    time2 = ("Time =", timex, "seconds")
    print(time2)
    #timex1 = string(timex)
    timetext = open('times.txt','a+')
    timetext.write(str(timex))
    main()

def transport():
    costs  = {'W': {'A': 34, 'B': 84, 'C': 12, 'D': 75},
              'X': {'A': 45, 'B': 56, 'C': 90, 'D': 87},
              'Y': {'A': 68, 'B': 67, 'C': 68, 'D': 54}}
    demand = {'A': 80, 'B': 65, 'C': 70, 'D': 55}
    cols = sorted(demand.iterkeys())
    supply = {'W': 75, 'X': 125, 'Y': 100}
    res = dict((k, defaultdict(int)) for k in costs)
    g = {}
    
    #g contains all the columns and rows names like - a,b,c,... and so on
    for x in supply:
        g[x] = sorted(costs[x].iterkeys(), key=lambda g: costs[x][g])
    for x in demand:
        g[x] = sorted(costs.iterkeys(), key=lambda g: costs[g][x])

    while g:
        d = {}
        for x in demand:
            d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else costs[g[x][0]][x]
        s = {}
        for x in supply:
            s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]]) if len(g[x]) > 1 else costs[x][g[x][0]]
        f = max(d, key=lambda n: d[n])
        t = max(s, key=lambda n: s[n])
        t, f = (f, g[f][0]) if d[f] > s[t] else (g[t][0], t)
        v = min(supply[f], demand[t])
        res[f][t] += v
        demand[t] -= v
        if demand[t] == 0:
            for k, n in supply.iteritems():
                if n != 0:
                    g[k].remove(t)
            del g[t]
            del demand[t]
        supply[f] -= v
        if supply[f] == 0:
            for k, n in demand.iteritems():
                if n != 0:
                    g[k].remove(f)
            del g[f]
            del supply[f]
 
    for n in cols:
        print ("\t", n),
    print
    cost = 0
    for g in sorted(costs):
        print (g, "\t"),
        for n in cols:
            y = res[g][n]
            if y != 0:
                print (y),
            cost += y * costs[g][n]
            print ("\t"),
        print
    print ("\n\nTotal Cost = ",cost)
    start_time = time.clock()
    print()
    time1 = ("Time =", time.clock() - start_time, "seconds")
    print (time1)
    main()
#class assignM():
 #   def init_labels(cost):
  #      n = len(cost)
   #     lx = [0] * n
    #    ly = [0] * n
     #   for x in range(n):
      #      for y in range(n):
       #         lx[x] = max(lx[x], cost[x][y])
        #return lx,ly






if __name__ == '__main__':
    main()
    #f mini.time1 > maxi.time2:
     #   print ("module one executes faster than module two")
    start_time = time.clock()
    print()
    print("Time =", time.clock() - start_time, "seconds")
