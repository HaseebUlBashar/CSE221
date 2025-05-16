#Task 1
N, M = map(int, input().split())
result_matrix=[]
for i in range(N):
    result_matrix.append([0]*N)
for j in range(M):
    p,q,r=map(int, input().split())
    result_matrix[p-1][q-1]=r
for row in result_matrix:
    print(' '.join(map(str, row)))
#task 2
N, M = map(int, input().split())
node1=list(map(int, input().split()))
node2=list(map(int, input().split()))
weight=list(map(int, input().split()))
result_list=[[] for i in range (N)]
 
for i in range(M):
    result_list[node1[i]-1].append((node2[i],weight[i]))
count=1
for j in result_list:
    print(f"{count}:{' '.join(map(str, j))}")
    count+=1
#Task 3
M = int(input())
result_matrix=[]
for i in range(M):
    result_matrix.append([0]*M)
for j in range(M):
   a=list(map(int, input().split()))
   n=a[0]
   for k in range(n):
       result_matrix[j][a[k+1]]=1
for row in result_matrix:
    print(' '.join(map(str, row)))
#Task 4
n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
 
degree = [0] * (n + 1)
 
for i in range(m):
    degree[u[i]] += 1
    degree[v[i]] += 1
 
odd_count = sum(1 for d in degree[1:] if d % 2 != 0)
 
if odd_count == 0 or odd_count == 2:
    print("YES")
else:
    print("NO")
#Task 5
n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
 
indegree = [0] * (n + 1)
outdegree = [0] * (n + 1)
 
for i in range(m):
    outdegree[u[i]] += 1
    indegree[v[i]] += 1
 
result = [indegree[i] - outdegree[i] for i in range(1, n + 1)]
print(' '.join(map(str, result)))
#Task 6
n = int(input())
x, y = map(int, input().split())
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),(0, 1),(1, -1),(1, 0), (1, 1)]
valid_moves = []
 
for i, j in directions:
    p, q = x + i, y + j
    if 1 <= p <= n and 1 <= q <= n:
        valid_moves.append((p, q))
 
valid_moves.sort()
 
print(len(valid_moves))
for move in valid_moves:
    print(move[0], move[1])
#Task 7
from math import gcd
x, y = map(int, input().split())
graph1=[[]]
for i in range(1,x+1):
    temp=[]
    for j in range(1,x+1):
        if i != j and gcd(i, j) == 1:
            temp.append(j)
    graph1.append(temp)
for p in range(y):
    a, b = map(int, input().split())
    count=0
    flag=True
    for q in graph1[a]:
        count+=1
        if count==b:
            print(q)
            flag=False
    if flag==True:
        print("-1")