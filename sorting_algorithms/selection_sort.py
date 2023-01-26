lis = [56, 3, 2, 78]
for i in range(len(lis)):
    min_val = min(lis[i:])
    min_ind = lis.index(min_val)
    lis[i], lis[min_ind] = lis[min_ind], lis[i]
print(lis)