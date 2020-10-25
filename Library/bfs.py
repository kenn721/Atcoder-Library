
#! BFSアルゴリズム
import numpy as np
def bfs(g,n):
    dist = np.ones(n)*-1
    dist[0] = 0
    que = [0]
    while len(que) > 0:
        s = que.pop(0)
        for nv in g[s]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[s]+1
            que.append(nv)
    return dist