num = input()
length = len(num)

if (int(num) // 10) < 1:
    if (int(num) == 9):
        result = str(11)
    else:
        result = str(int(num)+1)
else:          
    if int(num[:length//2][::-1]) > int(num[length//2+length%2::]):
        result = num[:length//2+length%2] + num[:length//2][::-1]
    else:
        num = str(int(num[:length//2+length%2])+1)  
        num += num[length//2-1::-1]
        result = num

print(result)