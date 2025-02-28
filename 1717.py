import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n + 1))
result=[]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        parent[rootB] = rootA 

def check(a, b):
    if find(a) == find(b):
        result.append("YES")
    else:
        result.append("NO")

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    elif op == 1:
        check(a, b)

for item in result:
    print(item)