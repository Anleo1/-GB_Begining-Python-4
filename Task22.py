def dele(l):
    res_list = []
    for i in l:
        if i not in res_list:
            res_list.append(i)
    return res_list

n = int(input("Введите количество элементов 1ого массива: "))
m = int(input("Введите количество элементов 2ого массива: "))
list1 = input("Введите элементы 1ого массива: ").split()
list2 = input("Введите элементы 2ого массива: ").split()
result = []
for i in range(n):
    for j in range(m):
        if list1[i]==list2[j]:
            result.append(list1[i])
print(dele(result))