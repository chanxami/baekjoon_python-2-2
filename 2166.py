n = int(input())
point = []

for _ in range(n):
    point.append(list(map(int, input().strip().split()))) 
point.append(point[0])

result=0
for i in range(n):
    result+=(point[i][0]*point[i+1][1]-point[i+1][0]*point[i][1])

print(abs(result/2))