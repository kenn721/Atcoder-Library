
# !TSP dは重み付グラフのリスト(nxn)
def tsp(d):
    n = len(d)
    # DP[A] = {v: value}
    DP = dict()
    
    for A in range(1, 1 << n):
        if A & 1 << 0 == 0:# 集合Aが0を含まない
            continue
        if A not in DP:
            DP[A] = dict()

        # main
        for v in range(n):
            if A & 1 << v == 0:
                if A == 1 << 0:
                    DP[A][v] = d[0][v] if d[0][v] > 0 else float('inf')
                else:
                    DP[A][v] = min([DP[A ^ 1 << u][u] + d[u][v] for u in range(n) 
                                    if u != 0 and A & 1 << u != 0 and d[u][v] > 0]
                                  + [float('inf')])
    # 最後だけ例外処理
    V = 1 << n
    DP[V] = dict()
    DP[V][0] = min([DP[A ^ 1 << u][u] + d[u][0] for u in range(n) 
                    if u != 0 and A & 1 << u != 0 and d[u][0] > 0]
                    + [float('inf')]) 


    return DP[V][0]