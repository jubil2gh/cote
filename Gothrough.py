from heapq import heappop, heappush
 
def init(N, K, sCity, eCity, mLimit):
    global nn, kk, adj
    nn, kk = N, K
    adj = [[] for _ in range(nn)]
    for idx in range(kk):
        adj[sCity[idx]].append((eCity[idx], mLimit[idx]))
        adj[eCity[idx]].append((sCity[idx], mLimit[idx]))
    return
 
def add(sCity, eCity, mLimit):
    adj[sCity].append((eCity, mLimit))
    adj[eCity].append((sCity, mLimit))
    return
 
def calculate(sCity, eCity,    M, mStopover):
    pq = [(-30001, sCity)]
    dist = [-1]*nn
    dist[sCity] = 30001
 
    while pq:
        pcost, prev = map(abs, heappop(pq))
 
        if pcost != dist[prev]:
            continue
 
        for next, ncost in adj[prev]:
            newcost = min(ncost, pcost)
            if dist[next] < newcost:
                dist[next] = newcost
                heappush(pq, (-newcost, next))
 
    ans = dist[eCity]
    for m in mStopover:
        ans = min(ans, dist[m])
    return ans