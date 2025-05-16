import heapq
 
N, M, S, D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
 
adj = [[] for _ in range(N + 1)]
for i in range(M):
    adj[u[i]].append((v[i], w[i]))
 
dist = [float('inf')] * (N + 1)
parent = [-1] * (N + 1)
dist[S] = 0
heap = [(0, S)]
 
while heap:
    d, node = heapq.heappop(heap)
    if d > dist[node]: continue
    for nei, wt in adj[node]:
        if dist[nei] > d + wt:
            dist[nei] = d + wt
            parent[nei] = node
            heapq.heappush(heap, (dist[nei], nei))
 
if dist[D] == float('inf'):
    print(-1)
else:
    print(dist[D])
    path = []
    while D != -1:
        path.append(D)
        D = parent[D]
    print(*path[::-1])
#Task 2 
import heapq
 
def dijkstra(N, adj, start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist
 
N, M, S, T = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
 
dS = dijkstra(N, adj, S)
dT = dijkstra(N, adj, T)
 
res = (float('inf'), -1)
for i in range(1, N + 1):
    if dS[i] != float('inf') and dT[i] != float('inf'):
        t = max(dS[i], dT[i])
        if t < res[0] or (t == res[0] and i < res[1]):
            res = (t, i)
 
print(-1 if res[1] == -1 else f"{res[0]} {res[1]}")
#Task 3 
import heapq
 
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
 
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
 
cost = [float('inf')] * (N + 1)
cost[1] = 0
heap = [(0, 1)]  # (danger_level, node)
 
while heap:
    danger, u = heapq.heappop(heap)
    if danger > cost[u]:
        continue
    for v, w in adj[u]:
        new_danger = max(danger, w)
        if new_danger < cost[v]:
            cost[v] = new_danger
            heapq.heappush(heap, (cost[v], v))
 
for i in range(1, N + 1):
    print(-1 if cost[i] == float('inf') else cost[i], end=' ')
#Task 4
import heapq
 
N, M, S, D = map(int, input().split())
w = [0] + list(map(int, input().split()))  # 1-indexed
 
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
 
cost = [float('inf')] * (N + 1)
cost[S] = w[S]
hq = [(cost[S], S)]
 
while hq:
    c, u = heapq.heappop(hq)
    if c > cost[u]:
        continue
    for v in adj[u]:
        if cost[v] > c + w[v]:
            cost[v] = c + w[v]
            heapq.heappush(hq, (cost[v], v))
 
print(cost[D] if cost[D] != float('inf') else -1)
#Task 5
import heapq
 
N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
 
adj = [[] for _ in range(N + 1)]
for i in range(M):
    adj[u[i]].append((v[i], w[i]))
 
INF = float('inf')
dist = [[INF, INF] for _ in range(N + 1)]
heap = []
 
for nei, weight in adj[1]:
    p = weight % 2
    if dist[nei][p] > weight:
        dist[nei][p] = weight
        heapq.heappush(heap, (weight, nei, p))
 
while heap:
    d, u, parity = heapq.heappop(heap)
    if d > dist[u][parity]:
        continue
    for v, wght in adj[u]:
        next_parity = wght % 2
        if next_parity != parity:
            if dist[v][next_parity] > d + wght:
                dist[v][next_parity] = d + wght
                heapq.heappush(heap, (dist[v][next_parity], v, next_parity))
 
res = min(dist[N])
print(res if res != INF else -1)
