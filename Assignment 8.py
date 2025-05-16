#Task 1
import sys
sys.setrecursionlimit(1 << 25)  
input = sys.stdin.readline
 
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) 
    return parent[x]
 
def union(x, y):
    x_root = find(x)
    y_root = find(y)
 
    if x_root != y_root:
        parent[y_root] = x_root
        size[x_root] += size[y_root]
 
    return size[find(x)]
 
 
n, k = map(int, input().split())
 
 
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)
 
for i in range(k):
    a, b = map(int, input().split())
    print(union(a, b))
#Task 2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)
 
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
 
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return False
    parent[y_root] = x_root
    return True
 
 
n, m = map(int, input().split())
edges = []
 
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
 
 
edges.sort()
 
parent = [i for i in range(n + 1)]
total_cost = 0
for w, u, v in edges:
    if union(u, v):
        total_cost += w
 
print(total_cost)