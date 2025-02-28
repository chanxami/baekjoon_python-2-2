import sys
input = sys.stdin.readline

L, C = map(int, input().split())
word = list(map(str, input().split()))
word.sort()  
reuslt=[]

def check_vowel(code):
    cnt=0
    for i in code:
        if i in ['a','e','i','o','u']:
            cnt+=1
    return cnt
s
def dfs(n,code):
    if n>C-1:
        if (len(code)==L) and (check_vowel(code))>=1 and (L-check_vowel(code)>=2):
            print(code)
        return
    dfs(n+1,code+word[n])
    dfs(n+1,code)

dfs(0,'')
        
