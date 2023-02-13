def f(l, n):
    max = 0
    sum = 0
    for i in range(n):
        if i == 0:
            sum = int(l[i]) + int(l[i+1]) + int(l[n-1])
        elif i == n-1:
            sum = int(l[0]) + int(l[i-1]) + int(l[i])
        else:
            sum = int(l[i]) + int(l[i+1]) + int(l[i-1])
        if sum > max:
            max = sum
    return max


n = int(input("Введите количество кустов: "))
harvest = input("Количество ягод на кустах: ").split()
print("Ответ =",f(harvest, n))