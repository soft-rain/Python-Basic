﻿n = int(input())
a = input().split()

arr = []

for i in range(24):
    arr.append(0)

for i in range(n):
    arr[int(a[i])] += 1

for i in range(1, 24):
    print(arr[i], end=" ")
