import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
broken = set(sys.stdin.readline().split()) if M else set()

def possible(channel):
    return not set(str(channel)) & broken 
min_presses = abs(N - 100) 

for num in range(1000000):  
    if possible(num):  
        min_presses = min(min_presses, len(str(num)) + abs(num - N))

print(min_presses)
