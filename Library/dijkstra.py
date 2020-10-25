#! Dijkstra法
def dijkstra(g,n,s):
    '''
    input
        g: n x n　list
        n: int
        s: start index
    '''
    d = [float('inf')]*n
    U = [i for i in range(n)]
    d[s] = 0
    while len(U)>0:
        w = U[0]
        for u in U:
            if d[u]<d[w]:
                w = u
        U.pop(U.index(w))
        for v in U:
            d[v] = min(d[v],d[w]+g[w][v])
    return d
print(dijkstra(g,4,0))