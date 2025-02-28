import sys
input = sys.stdin.readline

N,M= map(int, input().split())
num = list(map(int, input().split()))
sum = 0
prefix= [0] * M

for i in range(N):
  sum += num[i]
  prefix[sum % M] += 1

result = prefix[0]

for i in prefix:
  result += i*(i-1)//2
  
print(result)