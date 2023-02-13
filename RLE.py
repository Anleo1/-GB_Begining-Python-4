str = input()
result = []
for i in range(len(str)-1):
    if str[i].isnumeric():
        n = str[i]
        i+=1
        while str[i].isnumeric():
            n += str[i]
            i+=1
        num = int(n)
        while num > 1:
            result.append(str[i])
            num-=1
    else:
        result.append(str[i])
print(result)