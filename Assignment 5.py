#Task1:
from collections import deque
 
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
 
for j in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
visited = [0] * (n + 1)
queue = deque([])
queue.append(1)
visited[1] = 1
order = []
 
 
while queue:
    node = queue.popleft()
    order.append(node)
    for neighbor in graph[node]:
        if visited[neighbor]==0:
            visited[neighbor] = 1
            queue.append(neighbor)
 
 
print(*order)
#Task 2
import sys
 
 
sys.setrecursionlimit(2 * 10**5 + 5)
 
n, m = map(int, input().split())
 
 
graph = [[] for _ in range(n + 1)]
 
 
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
 
 
for i in range(m):
    u = u_list[i]
    v = v_list[i]
    graph[u].append(v)
    graph[v].append(u)
 
 
visited = [0] * (n + 1)
order = []
 
 
def dfs(node):
    visited[node] = 1  
    order.append(node)  
    for neighbor in graph[node]:
        if not visited[neighbor]:  
            dfs(neighbor)
 
 
dfs(1)
 
 
print(*order)
#Task 3
from collections import deque
 
n,m,s,d = map(int, input().split())
graph = [[] for i in range(n + 1)]
lst1=list(map(int, input().split()))
lst2=list(map(int, input().split()))
for j in range(m):
    graph[lst1[j]].append(lst2[j])
    graph[lst2[j]].append(lst1[j])
for neighbors in graph:
    neighbors.sort()
 
visited = [0] * (n + 1)
parent=[None] * (n + 1)
queue = deque([])
queue.append(s)
visited[s] = 1
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if visited[neighbor]==0:
            visited[neighbor] = 1
            parent[neighbor]=node
            queue.append(neighbor)
count=0
temp=d
lst1=[]
flag=False
while temp is not None:
    lst1.append(temp)
    if temp == s:
        flag=True
        break
    temp = parent[temp]
    count += 1
 
if flag==True:
    print(count)
    print(*lst1[::-1])
else:
    print("-1")
#Task 4
from collections import deque
 
n,m,s,d,k = map(int, input().split())
graph = [[] for i in range(n + 1)]
 
for j in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
 
 
def bfs (s,d,graph,n):
    visited = [0] * (n + 1)
    parent=[None] * (n + 1)
    queue = deque([])
    queue.append(s)
    visited[s] = 1
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor]==0:
                visited[neighbor]=1
                parent[neighbor]=node
                queue.append(neighbor)
 
    temp=d
    lst1=[]
    flag=False
    while temp is not None:
        lst1.append(temp)
        if temp == s:
            return lst1[::-1]
        temp = parent[temp]
    return []
path1 = bfs(s, k, graph, n)
 
path2 = bfs(k, d, graph, n) 
if not path1 or not path2:
    print(-1)
else:
    full_path = path1 + path2[1:]
    print(len(full_path) - 1)
    print(*full_path)
#Task 5

import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
 
for j in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
 
visited = [0] * (n + 1)
cycle=False
def dfs(k):
    global cycle 
    visited[k]=1 
    for neighbor in graph[k]:
 
        if visited[neighbor]==0:
            visited[neighbor]=1
            dfs(neighbor)
        elif visited[neighbor]==1:
            cycle=True
    visited[k]=2
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
    if cycle==True:
        print("YES")
        break
if cycle==False:
    print("NO")
#Task 6
def dfs(x, y, grid, visited):
    stack = [(x, y)]
    visited[x][y] = True
    diamond_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        cx, cy = stack.pop()
        if grid[cx][cy] == 'D':
            diamond_count += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                stack.append((nx, ny))
    
    return diamond_count
 
def max_diamonds(R, H, grid):
    visited = [[False] * H for _ in range(R)]
    max_diamonds = 0
    
    for i in range(R):
        for j in range(H):
            if not visited[i][j] and grid[i][j] != '#':
                max_diamonds = max(max_diamonds, dfs(i, j, grid, visited))
    
    return max_diamonds
 
 
R, H = map(int, input().split())
grid = [input().strip() for _ in range(R)]
 
 
print(max_diamonds(R, H, grid))

