from collections import defaultdict
 
costs  = {'W': {'A': 30, 'B': 10, 'C': 25, 'D': 20}, #'E': 0},
          'X': {'A': 15, 'B': 25, 'C': 30, 'D': 10}, #'E': 0},
          'Y': {'A': 20, 'B': 30, 'C': 15, 'D': 20}, #'E': 0},
          'Z': {'A': 0, 'B': 0, 'C': 50, 'D': 15}} #'E': 0}}
demand = {'A': 1500, 'B': 1500, 'C': 1700}# 'D': 0,} #'E': 0}
cols = sorted(demand.iterkeys())
supply = {'W': 1000, 'X': 1200, 'Y': 1500, 'Z': 1000}
res = dict((k, defaultdict(int)) for k in costs)
g = {}
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
    print "\t", n,
print
cost = 0
for g in sorted(costs):
    print g, "\t",
    for n in cols:
        y = res[g][n]
        if y != 0:
            print y,
        cost += y * costs[g][n]
        print "\t",
    print
print "\n\nTotal Cost = ", cost
