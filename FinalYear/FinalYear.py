from __future__ import print_function
import munkres
from munkres import Munkres
from munkres import print_matrix 
from munkres import make_cost_matrix
from munkres import DISALLOWED
import time
from ortools.graph import pywrapgraph


m = Munkres()

choice1 = eval(input("Enter Choice: "
        "A) Minimum Cost Flow/Network/Bitparte Graph "
        "B) Munkres Module (Hungarian Method (Reduced iterations)) "
        "C) Solving as Transportation Problem: "
))

if choice1 == 2:
    mat00 = input("Enter number: ")
    mat10 = input("Enter number: ")
    mat20 = input("Enter number: ")
    mat01 = input("Enter number: ")
    mat11 = input("Enter number: ")
    mat21 = input("Enter number: ")
    mat02 = input("Enter number: ")
    mat12 = input("Enter number: ")
    mat22 = input("Enter number: ")
    matrix = [[mat00, mat01, mat02],
              [mat10, mat11, mat12],
              [mat20, mat21, mat22]]
    m = Munkres()
    indexes = m.compute(matrix)
    print_matrix(matrix, msg='Lowest cost through this matrix:')
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
        print ('(%d, %d) -> %d' % (row, column, value))
    print ('total cost: %d' % total)
elif choice1 == 2:
    mat00 = input("Enter number: ")
    mat10 = input("Enter number: ")
    mat20 = input("Enter number: ")
    mat01 = input("Enter number: ")
    mat11 = input("Enter number: ")
    mat21 = input("Enter number: ")
    mat02 = input("Enter number: ")
    mat12 = input("Enter number: ")
    mat22 = input("Enter number: ")
    matrix = [[mat00, mat01, mat02],
              [mat10, mat11, mat12],
              [mat20, mat21, mat22]]
    cost_matrix = make_cost_matrix(matrix)
    # cost_matrix == [[5, 1, 9],
    #                 [0, 7, 8],
    #                 [2, 3, 6]]
    m = Munkres()
    indexes = m.compute(cost_matrix)
    print_matrix(matrix, msg='Highest profits through this matrix:')
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
        print ('(%d, %d) -> %d' % (row, column, value))
    print ('total profit=%d' % total)
elif choice1 == 3:
    matrix = [[5, 9, DISALLOWED],
              [10, DISALLOWED, 2],
              [8, 7, 4]]
    cost_matrix = make_cost_matrix(matrix, lambda cost: (sys.maxsize - cost) if    
                                          (cost != DISALLOWED) else DISALLOWED)
    m = Munkres()
    indexes = m.compute(cost_matrix)
    print_matrix(matrix, msg='Highest profit through this matrix:')
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
        print ('(%d, %d) -> %d' % (row, column, value))
    print ('total profit=%d' % total)

elif choice1 == "A" or "a":
    print ("*********** Minimum Cost Flow ***************")
  # Instantiate a SimpleMinCostFlow solver.
    min_cost_flow = pywrapgraph.SimpleMinCostFlow()
  # Define the directed graph for the flow.

    start_nodes = [0, 0, 0, 0] + [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4] + [5, 6, 7, 8]
    end_nodes =   [1, 2, 3, 4] + [5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8] + [9, 9, 9, 9]
    capacities =  [1, 1, 1, 1] + [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] + [1, 1, 1, 1 ]
    costs  = ([0, 0, 0, 0] + [90, 76, 75, 70, 56, 85, 55, 65, 125, 95, 99, 105, 45, 110, 95, 115]
                + [0, 0, 0, 0])
  # Define an array of supplies at each node.
    supplies = [4, 0, 0, 0, 0, 0, 0, 0, 0, -4]
    source = 0
    sink = 9
    tasks = 4

  # Add each arc.
    for i in range(len(start_nodes)):
        min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], costs[i])

  # Add node supplies.

    for i in range(len(supplies)):
        min_cost_flow.SetNodeSupply(i, supplies[i])
  # Find the minimum cost flow between node 0 and node 10.
    if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
        print('Total cost = ', min_cost_flow.OptimalCost())
        print()
    for arc in range(min_cost_flow.NumArcs()):

      # Can ignore arcs leading out of source or into sink.
      if min_cost_flow.Tail(arc)!=source and min_cost_flow.Head(arc)!=sink:

        # Arcs in the solution have a flow value of 1. Their start and end nodes
        # give an assignment of worker to task.

        if min_cost_flow.Flow(arc) > 0:
          print('Worker %d assigned to task %d.  Cost = %d' % (
                min_cost_flow.Tail(arc),
                min_cost_flow.Head(arc),
                min_cost_flow.UnitCost(arc)))
else:
    print('There was an issue with the min cost flow input.')

if __name__ == '__main__':
  start_time = time.clock()
  print()
  print("Time =", time.clock() - start_time, "seconds")

