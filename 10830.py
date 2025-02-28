import sys
input = sys.stdin.readline  
n, b = map(int, input().split())  
a = [list(map(int, input().split())) for _ in range(n)] 

def multi(a, b):
    x = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x[i][j] = (x[i][j] + a[i][k] * b[k][j]) % 1000
    return x

def square(a, b):
    if b == 1:
        return [[a[i][j] % 1000 for j in range(n)] for i in range(n)]
    tmp = square(a, b // 2)
    tmp = multi(tmp, tmp)
    return tmp if b % 2 == 0 else multi(tmp, a)

result = square(a, b)

for row in result:
    print(*row)
