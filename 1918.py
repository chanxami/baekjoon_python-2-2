x = input()
s = []
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

for i in x:
    if i.isalnum():
        print(i, end="")
    elif i in precedence:
        while s and s[-1] in precedence and precedence[s[-1]] >= precedence[i]:
            print(s.pop(), end="")
        s.append(i)
    elif i == '(':
        s.append(i)
    elif i == ')':
        while s and s[-1] != '(':
            print(s.pop(), end="")
        s.pop()

while s:
    print(s.pop(), end="")
