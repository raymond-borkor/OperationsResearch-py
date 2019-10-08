#from txtdata import *


class Vogel():

    def __init__(self, warehouses, stores, supply, demand, cost):
        self.warehouses = warehouses
        self.stores = stores
        self.supply = supply
        self.demand = demand
        self.cost = cost

    def rows_dict(self):
        rows_d = {}
        for i in range(len(self.supply)):
            if self.supply[i] > 0:
                row = []
                for j in range(self.stores):
                    row.append(self.cost[i][j])
                rows_d[i] = row
        return rows_d

    def cols_dict(self):
        cols_d = {}
        for l in range(len(self.demand)):
            if self.demand[l] > 0:
                col = []
                for k in range(self.warehouses):
                    col.append(self.cost[k][l])
                cols_d[l] = col
        return cols_d

    @staticmethod
    def two_mins(array):
        temp = []
        if array == ['']:
            minimum = -1
            return minimum
        else:
            for i in range(len(array)):
                if array[i] == ['']:
                    i += 1
                else:
                    temp.append(array[i])

            temp = sorted(temp)
            if len(temp) > 1:
                minimum = abs(temp[0] - temp[1])
            else:
                minimum = temp[0]
            return minimum

    @staticmethod
    def diff_r(rows_d, supply, cols_d):

        diff_rows = {}

        for i in rows_d:
            if supply[i] > 0:
                minimum = Vogel.two_mins(rows_d[i])
                diff_rows[i] = minimum
            elif supply[i] == 0 and rows_d[i] != ['']:
                rows_d[i] = ['']
                for k in cols_d:
                    if cols_d[k] != ['']:
                        cols_d[k][i] = ['']

        return diff_rows

    @staticmethod
    def diff_c(cols_d, demand, rows_d):

        diff_cols = {}

        for i in cols_d:
            if demand[i] > 0:
                minimum = Vogel.two_mins(cols_d[i])
                diff_cols[i] = minimum
            elif demand[i] == 0 and cols_d[i] != ['']:
                cols_d[i] = ['']
                for k in rows_d:
                    if rows_d[k] != ['']:
                        rows_d[k][i] = ['']

        return diff_cols

    @staticmethod
    def find_max(diff_rows, diff_cols):
        maximum_row = -1
        for i in diff_rows:
            flag = diff_rows[i]
            if flag > maximum_row:
                maximum_row = flag

        maximum_col = -1
        for i in diff_cols:
            temp = diff_cols[i]
            if temp > maximum_col:
                maximum_col = temp

        if maximum_col > maximum_row:
            return maximum_col
        else:
            return maximum_row

    @staticmethod
    def max_location_row(diff_rows, maximum):

        location_row = []
        for i in diff_rows:
            if maximum == diff_rows[i]:
                location_row.append(i)

        return location_row

    @staticmethod
    def max_location_cols(diff_cols, maximum):

        location_col = []
        for i in diff_cols:
            if maximum == diff_cols[i]:
                location_col.append(i)

        return location_col

    @staticmethod
    def find_pivot(location_row, location_col, rows_d, cols_d):
        minimum = 99999
        if len(location_row) > 0:
            for id in location_row:
                if min(rows_d[id]) <= minimum:
                    minimum = min(rows_d[id])
                    supply_pos = id
                    demand_pos = rows_d[id].index(minimum)

        if len(location_col) > 0:
            for id in location_col:
                if min(cols_d[id]) <= minimum:
                    minimum = min(cols_d[id])
                    supply_pos = cols_d[id].index(minimum)
                    demand_pos = id

        return supply_pos, demand_pos

    def implementation(self):

        rows_d = Vogel.rows_dict(ins)
        cols_d = Vogel.cols_dict(ins)
        # print rows_d
        # print cols_d
        score = 0
        while 1:
            counter = 0
            for i in range(len(self.demand)):
                if self.demand[i] == 0:
                    counter += 1
            # total demand = 0
            if counter == len(self.demand):
                break
            else:

                diff_rows = Vogel.diff_r(rows_d, self.supply, cols_d)
                diff_cols = Vogel.diff_c(cols_d, self.demand, rows_d)
                # print 'diff for rows:', diff_rows
                # print 'diff for cols:', diff_cols

                maximum = Vogel.find_max(diff_rows, diff_cols)
                # print 'maximum:', maximum

                location_row = Vogel.max_location_row(diff_rows, maximum)
                location_col = Vogel.max_location_cols(diff_cols, maximum)
                # print 'pivot location', Vogel.find_pivot(location_row, location_col, rows_d, cols_d)

                supply_pos = Vogel.find_pivot(location_row, location_col, rows_d, cols_d)[0]
                demand_pos = Vogel.find_pivot(location_row, location_col, rows_d, cols_d)[1]

                # cost Calculation
                if self.supply[supply_pos] == self.demand[demand_pos]:
                    score = score + self.demand[demand_pos] * self.cost[supply_pos][demand_pos]
                    self.supply[supply_pos] -= self.demand[demand_pos]
                    self.demand[demand_pos] = 0
                elif self.demand[demand_pos] > self.supply[supply_pos]:
                    score = score + self.supply[supply_pos] * self.cost[supply_pos][demand_pos]
                    self.demand[demand_pos] -= self.supply[supply_pos]
                    self.supply[supply_pos] = 0
                else:
                    score = score + self.demand[demand_pos] * self.cost[supply_pos][demand_pos]
                    self.supply[supply_pos] -= self.demand[demand_pos]
                    self.demand[demand_pos] = 0
                # print 'supply:', self.supply
                 #print 'demand:', self.demand
                 #print ''

        print ("The Vogel's cost is"), score

if __name__ == '__main__':
    # number of warehouses
    #w = warehouses_construction()
    w = 3
    # number of stores
    st = 4
    # supply array for example:([3, 4, 5])
    sup = ([3, 4, 5])
    # demand array for example:([2, 5, 2, 3])
    dem = ([2, 5, 2, 3])
    # cost array for example: ([[5, 3, 1 ,8],
    #                          [1, 7, 2 ,3],
    #                          [6, 2, 11 ,9]])
    cst = ([[5, 3, 1 ,8],
            [1, 7, 2 ,3],
            [6, 2, 11 ,9]])

    ins = Vogel(w, st, sup, dem, cst)
    Vogel.implementation(ins)